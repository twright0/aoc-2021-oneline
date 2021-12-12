from aocd import get_data
from aocd.transforms import lines
data = lines(get_data(year=2021,day=12))

print((edges := [tuple(row.split('-')) for row in data]) and
      (edges.extend([(f,t) for (t,f) in edges])) or
      (can_repeat := lambda path, node: (False if node in ('start', 'end') else
                                         True if node[-1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' else
                                         ((small_caves := [p for p in path if p[0] in 'abcdefghijklmnopqrstuvwxyz']) and
                                          len(small_caves) == len(set(small_caves))))) and
      (dfs := lambda path: (
          1 if path[-1] == 'end' else
          sum([0 if (t != path[-1] or (f in path and not can_repeat(path, f))) else (dfs(path[:] + [f])) for t,f in edges]))) and
      dfs(['start'])
)
