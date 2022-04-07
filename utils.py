#!/usr/bin/python3.7

import sys
import shutil
import os


def init(name: str):
    print(f"Initializing template for {name}")

    # Create sample file. Fails if the file exists
    with open(f"./{name}.sample", "x"):
        pass

    # Template code
    shutil.copy("./template/template.py", f"./{name}.py")

    # Test code
    with open(f"./template/template_test.py", "r") as template:
        with open(f"./{name}_test.py", "w") as dest:
            dest.writelines(
                line.replace("template", name) for line in template.readlines()
            )


def run(name: str):
    print(f"Running samples for {name}")
    os.system(f"cat {name}.sample | /usr/bin/python3.7 {name}.py")


if __name__ == "__main__":
    if sys.argv[1] == "init":
        init(sys.argv[2])
    elif sys.argv[1] == "run":
        run(sys.argv[2])