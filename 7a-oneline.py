from aocd import get_data
data = get_data(day=7,year=2021)
#data = list(map(int,get_data(day=7,year=2021).split(",")))

print((nums := list(map(int,data.split(",")))) and
      min(sum(abs(j-i) for j in nums)
          for i in range(min(nums), max(nums)+1)))
