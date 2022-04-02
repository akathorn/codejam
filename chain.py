import itertools
import functools
import sys
from typing import Any, Callable, List, NamedTuple, Tuple, TypeVar, Union


Module = NamedTuple(
    "Module",
    [("id", int), ("fun", int), ("parents", List[int]), ("children", List[int])],
)
Path = NamedTuple(
    "Path", [("modules", List[int]), ("max_fun", int), ("total_fun", int)]
)


class Model:
    def __init__(self, modules: List[Module]) -> None:
        self.modules = modules

    @functools.lru_cache()
    def max_children(self, id: int) -> int:
        mod = self.modules[id]
        return max(mod.fun, *[self.max_children(c) for c in mod.children])

    def combine_paths(self, a: Path, b: Path) -> Path:
        return Path(
            modules=a.modules + b.modules,
            max_fun=a.max_fun,
            total_fun=a.total_fun + b.total_fun + b.max_fun,
        )

    def solve_rec(self, id: int) -> List[Path]:
        mod = self.modules[id]

        # Base case (initiator)
        if not mod.parents:
            return [Path([id], max_fun=mod.fun, total_fun=0)]

        parent_paths: List[List[Path]] = [self.solve_rec(id) for id in mod.parents]

        new_paths: List[Path] = []
        for i in range(len(parent_paths)):
            first: List[Path] = [
                Path(
                    modules=path.modules,
                    max_fun=max(mod.fun, path.max_fun),
                    total_fun=path.total_fun,
                )
                for path in parent_paths[i]
            ]
            paths: List[List[Path]] = [first] + parent_paths[:i] + parent_paths[i + 1 :]

            for product in itertools.product(*paths):
                new_paths.append(functools.reduce(self.combine_paths, product))

        return new_paths

    def solve(self) -> int:
        abyss = self.solve_rec(0)
        total_fun = max(path.total_fun + path.max_fun for path in abyss)
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
    modules: List[Module] = [Module(id=0, fun=0, parents=[], children=[])]

    for i, f in enumerate(funs, 1):
        mod = Module(i, f, [], [])
        modules.append(mod)

    for mod, p in enumerate(pointers, 1):
        modules[p].parents.append(mod)
        modules[mod].children.append(p)

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