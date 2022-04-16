#!/usr/bin/python3.7

import pstats
import sys
import shutil
import os

PYTHON_PATH = "/usr/bin/python3.7"


def init(name: str, interactive: bool):
    print(f"Initializing {'interactive ' if interactive else ''}template for {name}")
    if os.path.exists(f"./{name}.py"):
        raise FileExistsError("The module has been initialized already!")

    # Copy template code
    shutil.copy("./template/template.py", f"./{name}.py")

    if not interactive:
        # Create sample file
        print("Paste sample input")
        sample_input = []
        line = input()
        while line:
            sample_input.append(line + "\n")
            line = input()

        with open(f"./{name}.sample", "w") as sample:
            sample.writelines(sample_input)

        # Create test file
        print("Paste sample output")
        sample_output = []
        line = input()
        while line:
            sample_output.append(line + "\n")
            line = input()

        with open(f"./template/template_test.py", "r") as template:
            with open(f"./{name}_test.py", "w") as dest:
                for line in template.readlines():
                    if line.find("[INPUT]") >= 0:
                        dest.writelines(sample_input)
                    elif line.find("[OUTPUT]") >= 0:
                        dest.writelines(sample_output)
                    else:
                        dest.write(line.replace("template", name))
    else:
        with open(f"./template/template_interactive_test.py", "r") as template:
            with open(f"./{name}_test.py", "w") as dest:
                for line in template.readlines():
                    dest.write(line.replace("template", name))

    print(f"Template for {name} initialized")
    if interactive:
        print(f"Download testing tool and rename to {name}_judge.py")
        print(
            f"-If the Input/Output functions of the judge are nested, bring them to global scope"
        )


def run(name: str, interactive: bool):
    if not interactive:
        print(f"Running samples for {name}")
        os.system(f"cat {name}.sample | {PYTHON_PATH} {name}.py --log")
    else:
        if len(sys.argv) > 4:
            args = sys.argv[4:]
        else:
            args = []
        print(f"Invoking interactive runner for {name}. Extra args for judge: {args}")
        os.system(
            f"{PYTHON_PATH} interactive_runner.py "
            f"{PYTHON_PATH} {name}_judge.py {' '.join(args)} -- "
            f"{PYTHON_PATH} {name}.py --log"
        )


def test(name: str, interactive: bool):
    os.system(f'{PYTHON_PATH} -m pytest {name}_test.py -k "not test_profiling"')


def profile(name: str, interactive: bool):
    os.system(f"{PYTHON_PATH} -m pytest --profile {name}_test.py -k test_profiling")

    stats = pstats.Stats("prof/combined.prof")
    stats.sort_stats("cumulative")
    stats.print_stats(0.2, "^((?!pytest|pluggy).)*$")

    if len(sys.argv) > 3:
        stats.print_callees(sys.argv[3])


def profile_svg(name: str, interactive: bool):
    profile(name, interactive)
    os.system(
        f"gprof2dot -f pstats prof/combined.prof | dot -Tsvg -o prof/combined.svg"
    )


if __name__ == "__main__":
    if len(sys.argv) > 3 and sys.argv[3] == "--interactive":
        interactive = True
    else:
        interactive = False

    if sys.argv[2] == "init":
        init(sys.argv[1], interactive)
    elif sys.argv[2] == "run":
        run(sys.argv[1], interactive)
    elif sys.argv[2] == "test":
        test(sys.argv[1], interactive)
    elif sys.argv[2] == "profile":
        profile(sys.argv[1], interactive)
    elif sys.argv[2] == "profile_svg":
        profile_svg(sys.argv[1], interactive)