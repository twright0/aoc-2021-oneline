from aocd import get_data
data = list(map(int,get_data(day=7,year=2021).split(",")))

print(min(sum(int((n:=abs(j-i)) and (n*(n+1)/2)
              for j in data)
          for i in range(min(data), max(data)+1)))
