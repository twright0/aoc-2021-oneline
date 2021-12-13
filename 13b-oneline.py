from aocd import get_data
from functools import reduce
data = get_data(day=13,year=2021).split("\n\n")

print((pts := reduce(lambda last_pts, fold: (
          (fold := fold.split(" ")[2].split("=")) and
          (set([
              ((x if x < int(fold[1]) else x-2*(x-int(fold[1]))),y)
              if fold[0] == 'x' else
              (x,(y if y < int(fold[1]) else y-2*(y-int(fold[1]))))
              for x,y in last_pts]))
      ), data[1].split("\n"), [tuple(map(int, pt.split(","))) for pt in data[0].split("\n")])) and
      ((min_j := min(i for i,_ in pts)) or True) and
      ((min_i := min(j for _,j in pts)) or True) and
      ((max_j := max(i for i,_ in pts)) or True) and
      ((max_i := max(j for _,j in pts)) or True) and
      (grid := {(i,j): "X" for j,i in pts}) and

      "\n".join(("".join(grid.get((i,j)," ")
                         for j in range(min_j,max_j+1)))
                for i in range(min_i,max_i+1))
)
