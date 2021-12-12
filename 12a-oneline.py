from aocd import get_data
from aocd.transforms import lines
data = lines(get_data(year=2021,day=12))

print((edges := [tuple(row.split('-')) for row in data]) and
      (edges.extend([(f,t) for (t,f) in edges])) or
      (dfs := lambda path: (
          1 if path[-1] == 'end' else
          sum([0 if
                ((f in path and f[0] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ') or t != path[-1])
                else (dfs(path[:] + [f])) for t,f in edges]))) and
      dfs(['start'])
)
