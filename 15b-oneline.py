from aocd import get_data
from aocd.transforms import lines
from itertools import takewhile, repeat
from functools import reduce
import heapq
data = lines(get_data(year=2021,day=15))

print((edge_i := len(data)) and (edge_j := len(data[0])) and
      (graph := dict(((i+(mi*edge_i),j+(mj*edge_j)), reduce(lambda c,_: (1 if c > 8 else c+1),
                                                            range(mi+mj), int(c)))
                     for mj in range(5)
                     for mi in range(5)
                     for i,r in enumerate(data)
                     for j,c in enumerate(r)
                     )) and
      (unvisited := set(graph.keys())) and
      (tent_dists := {k: (0 if k == (0,0) else 100000) for k in unvisited}) and
      (frontier := [(0,(0,0))]) and
      (list(map(lambda n: (
          (((i := n[1][0]) or True) and ((j := n[1][1]) or True)) and
          (None if (i,j) not in unvisited else (
              unvisited.remove((i,j)) or
              list(map(lambda ds: (
                  ((neighbor_i := i+ds[0]) or True) and ((neighbor_j := j+ds[1]) or True) and
                  (neighbor := (neighbor_i, neighbor_j)) and
                  (((tent_dists.update({neighbor: min(tent_dists[neighbor],
                                                     tent_dists[(i,j)]+graph[neighbor])})) or
                   (heapq.heappush(frontier, (tent_dists[neighbor], neighbor))))
                  if neighbor in unvisited else None)
              ), ((0,1),(0,-1),(1,0),(-1,0)))) and None
          ))
      ),(heapq.heappop(frontier) for _ in takewhile(lambda _: not not frontier, repeat(0)))))) and
      tent_dists[max(graph.keys())]
)
