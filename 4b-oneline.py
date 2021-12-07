from aocd import get_data
from functools import reduce

print(
 (data := get_data(day=4,year=2021).split("\n\n")) and
 (nums := map(int, data[0].split(","))) and
 (boards := list(map(lambda b: list(map(lambda s: list(map(int, s.split())), b.split("\n"))),
                     data[1:]))) and
 (is_done := lambda b: (any(all(c == None for c in row) for row in (b + list(zip(*b)))))) and
 (total := lambda b: sum(sum(d for d in r if d is not None) for r in b)) and
 (reduce(lambda state, num: (state if state[0] is not None else (
     (next_boards := [[[None if d == num else d for d in row]
                       for row in board]
                      for board in state[1]]) and
     (done_boards := ([b for b in next_boards if is_done(b)] or True)) and
     (((num * total(done_boards[0])), []) if (done_boards is not True and len(done_boards) == len(next_boards)) else (None, [b for b in next_boards if not is_done(b)]))
         )),
         nums,
         (None, boards)))[0]
)
