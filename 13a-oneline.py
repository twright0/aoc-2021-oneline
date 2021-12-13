from aocd import get_data
data = get_data(day=13,year=2021).split("\n\n")

print((pts := [tuple(map(int, pt.split(","))) for pt in data[0].split("\n")]) and
      (fold := tuple(data[1].split("\n")[0].split(" ")[2].split("="))) and
      (len(set([
          ((x if x > int(fold[1]) else x-2*(x-int(fold[1]))),y)
          if fold[0] == 'x' else
          (x,(y if y > int(fold[1]) else y-2*(y-int(fold[1]))))
          for x,y in pts])))
)
