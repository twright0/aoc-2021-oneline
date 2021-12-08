from aocd import get_data
from aocd.transforms import lines
data = lines(get_data(day=8,year=2021))

print(sum(len([b for b in row.split("|")[1].strip().split(" ")
               if len(b) in (2,3,4,7)])
          for row in data))
