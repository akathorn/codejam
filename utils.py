#!/usr/bin/python3.7

import pstats
import sys
import shutil
import os


def init(name: str):
    print(f"Initializing template for {name}")
    if os.path.exists(f"./{name}.py"):
        raise FileExistsError("The module has been initialized already!")

    # Copy template code
    shutil.copy("./template/template.py", f"./{name}.py")

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

    print(f"Template for {name} initialized")


def run(name: str):
    print(f"Running samples for {name}")
    os.system(f"cat {name}.sample | /usr/bin/python3.7 {name}.py --log")


def test(name: str):
    os.system(f'python3.7 -m pytest {name}_test.py -k "not test_profiling"')


def profile(name: str):
    os.system(f"python3.7 -m pytest --profile {name}_test.py -k test_profiling")

    stats = pstats.Stats("prof/combined.prof")
    stats.sort_stats("cumulative")
    stats.print_stats(0.2, "^((?!pytest|pluggy).)*$")

    if len(sys.argv) > 3:
        stats.print_callees(sys.argv[3])


if __name__ == "__main__":
    if sys.argv[1] == "init":
        init(sys.argv[2])
    elif sys.argv[1] == "run":
        run(sys.argv[2])
    elif sys.argv[1] == "test":
        test(sys.argv[2])
    elif sys.argv[1] == "profile":
        profile(sys.argv[2])