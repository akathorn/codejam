import itertools
import functools
import sys
from typing import Any, Callable, List, NamedTuple, Tuple, TypeVar, Union


Module = NamedTuple(
    "Module",
    [("id", int), ("fun", int), ("parents", List[int])],
)
Path = NamedTuple("Path", [("max_fun", int), ("total_fun", int)])


class Model:
    def __init__(self, modules: List[Module]) -> None:
        self.modules = modules
        self.solutions = {}

    def close_path(self, path: Path) -> int:
        return path.max_fun + path.total_fun

    def resolve(self, id: int) -> None:
        mod = self.modules[id]

        # Base case (initiator)
        if not mod.parents:
            self.solutions[id] = [Path(max_fun=mod.fun, total_fun=0)]
            return

        parent_paths: List[List[Path]] = [
            self.solutions[parent_id] for parent_id in mod.parents
        ]

        new_paths: List[Path] = []
        for i in range(len(parent_paths)):
            first = parent_paths[i]
            rest = parent_paths[:i] + parent_paths[i + 1 :]
            rest_total_fun = sum(
                max(self.close_path(p) for p in paths) for paths in rest
            )
            new_paths.extend(
                [
                    Path(
                        max_fun=max(mod.fun, path.max_fun),
                        total_fun=path.total_fun + rest_total_fun,
                    )
                    for path in first
                ]
            )
        self.solutions[id] = new_paths

    def solve_all(self):
        for id in reversed(range(len(self.modules))):
            self.resolve(id)

    def solve(self) -> int:
        self.solve_all()
        abyss = self.solutions[0]
        total_fun = max(self.close_path(path) for path in abyss)
        return total_fun


def solve_case(case: int):
    # Read data
    _ = read(int)
    funs = readmany(int)
    pointers = readmany(int)
    model = create_model(funs, pointers)

    # Solve
    result = model.solve()

    # Write solution
    writesolution(case, result)


def create_model(funs, pointers) -> Model:
    modules: List[Module] = [Module(id=0, fun=0, parents=[])]

    for i, f in enumerate(funs, 1):
        mod = Module(i, f, [])
        modules.append(mod)

    for mod, p in enumerate(pointers, 1):
        modules[p].parents.append(mod)

    return Model(modules)


############################ Template code ###############################

T = TypeVar("T")


def read(typ: Callable[[str], T] = str) -> T:
    return typ(sys.stdin.readline().strip())


def readmany(typ: Callable[[str], T] = str) -> List[T]:
    return [typ(s) for s in sys.stdin.readline().split()]


def readlines(rows: int, typ: Callable[[str], T] = str) -> List[List[T]]:
    return [readmany(typ) for _ in range(rows)]


def writesolution(case: int, result: Union[Any, List[Any], None]) -> None:
    if isinstance(result, list):
        if isinstance(result[0], list):
            out_string = ""
            for row in result:
                out_values = map(str, row)
                out_string += "\n" + " ".join(out_values)
        else:
            out_string = " ".join(str(value) for value in result)
    elif result is None:
        out_string = "IMPOSSIBLE"
    else:
        out_string = str(result)

    sys.stdout.write(f"Case #%d: %s\n" % (case, out_string))


def main():
    T = read(int)
    for case in range(1, T + 1):
        solve_case(case)


if __name__ == "__main__":
    main()