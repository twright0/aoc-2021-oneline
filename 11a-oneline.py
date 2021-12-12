from aocd import get_data
from aocd.transforms import lines
from functools import reduce
data = lines(get_data(year=2021,day=11))

print(
    (grid := {(i,j): int(c) for i,row in enumerate(data) for j,c in enumerate(row)}) and
    (reduce(lambda total,_: (
        ((flashes := reduce(lambda state,k: (grid.update({k:grid[k]+1}) or (state.append(k) if grid[k] == 10 else None) or state), grid, [])) or total) and
        ((flashed := set()) or True) and
        ((list(map((lambda k: (None if k in flashed else ((flashed.add(k)) or ((i := k[0]) or True) and ((j := k[1]) or True) and (
            list(map(lambda dk: ((di := dk[0]) or True) and ((dj := dk[1]) or True) and
                                (grid.update({(i+di,j+dj): grid[(i+di,j+dj)]+1})
                                 if (i+di,j+dj) in grid else None) or
                                ((flashes.append((i+di,j+dj)))
                                 if grid.get((i+di,j+dj),0) > 9
                                 else None),
                     ((0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)))))))),
                   flashes)))
         or total) and
        total + reduce(lambda state, k: ((grid.update({k: 0}) or state+1) if grid.get(k,0) > 9 else state), grid, 0)),
    range(100),0))
)
