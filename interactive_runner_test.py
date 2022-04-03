import asyncio
import queue
import threading
import pytest
import passages
import passages_judge
from pytest_mock import mocker, MockerFixture  # type: ignore


@pytest.mark.asyncio
async def test_asyncio(mocker: MockerFixture):
    def Input(queue: asyncio.Queue):
        async def f():
            return await queue.get()

        return f

    def Output(queue: asyncio.Queue):
        async def f(s):
            await queue.put(s)

        return f

    sol_judge_queue = asyncio.Queue()
    judge_sol_queue = asyncio.Queue()

    sol_read = mocker.patch("passages.Input", wraps=Input(judge_sol_queue))
    judge_read = mocker.patch("passages_judge.Input", wraps=Input(sol_judge_queue))
    sol_write = mocker.patch("passages.Output", wraps=Output(sol_judge_queue))
    judge_write = mocker.patch("passages_judge.Output", wraps=Output(judge_sol_queue))

    async def run_sol():
        print("hola")
        passages.main()

    async def run_judge():
        passages_judge.RunCases()

    await asyncio.gather(run_sol(), run_judge())


def test_threads(mocker: MockerFixture):
    done = False

    def Input(queue: queue.Queue):
        def f():
            if done:
                raise EOFError
            return queue.get()

        return f

    def Output(queue: queue.Queue):
        def f(s):
            return queue.put(s)

        return f

    sol_judge_queue = queue.Queue()
    judge_sol_queue = queue.Queue()

    sol_read = mocker.patch("passages.Input", wraps=Input(judge_sol_queue))
    judge_read = mocker.patch("passages_judge.Input", wraps=Input(sol_judge_queue))
    sol_write = mocker.patch("passages.Output", wraps=Output(sol_judge_queue))
    judge_write = mocker.patch("passages_judge.Output", wraps=Output(judge_sol_queue))

    passages_judge.NUM_CASES = 2

    # judge_exceptions = []

    # def excepthook(args):
    #     judge_exceptions.append(args)

    # threading.excepthook = excepthook

    thread = threading.Thread(target=passages_judge.RunCases)
    thread.start()

    passages.main()
    done = True
    thread.join()
    # assert not judge_exceptions
