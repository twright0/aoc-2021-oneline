from aocd import get_data
data = get_data(day=7,year=2021)
print((nums := list(map(int,data.split(",")))) and
      min(sum(int((n:=abs(j-i)) and (n*(n+1)/2))
              for j in nums)
          for i in range(min(nums), max(nums)+1)))
