import queue
import threading
import template
import template_judge
from pytest_mock import mocker, MockerFixture  # type: ignore


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

    sol_read = mocker.patch("template.Input", wraps=Input(judge_sol_queue))
    sol_write = mocker.patch("template.Output", wraps=Output(sol_judge_queue))
    sol_read = mocker.patch("template.Finalize")
    judge_read = mocker.patch("template_judge.Input", wraps=Input(sol_judge_queue))
    judge_write = mocker.patch("template_judge.Output", wraps=Output(judge_sol_queue))

    # draupnir_judge.NUM_CASES = 2

    # judge_exceptions = []

    # def excepthook(args):
    #     judge_exceptions.append(args)

    # threading.excepthook = excepthook

    thread = threading.Thread(target=template_judge.RunCases)
    thread.start()

    template.main()
    done = True
    thread.join()
    # assert not judge_exceptions
