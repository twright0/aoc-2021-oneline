from aocd import get_data
from aocd.transforms import numbers
data = numbers(get_data(day=1,year=2021))

print(
    sum((1 if data[i] < data[i+1]
         else 0)
        for i in range(len(data)-1)
        )
)
