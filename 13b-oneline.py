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
      (grid := {(i,j): "X" for j,i in pts}) and
      "\n".join(("".join(grid.get((i,j)," ")
                         for j in range(min(i for i,_ in pts),max(i for i,_ in pts)+1)))
                for i in range(min(j for _,j in pts),max(j for _,j in pts)+1))
)
