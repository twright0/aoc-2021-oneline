from aocd import get_data
from aocd.transforms import lines
from functools import reduce

print(
    (m := {(i,j): int(v) for i,r in enumerate(lines(get_data(day=9,year=2021))) for j,v in enumerate(r)}) and
    (biggest := max(m.values()) + 1) and
    (reduce(lambda state, pt: (
        ((v := pt[1]) or True) and ((i := pt[0][0]) or True) and ((j := pt[0][1]) or True) and
        (state + ((v+1) if all(m.get((i+di,j+dj),biggest) > v for di, dj in ((-1,0),(1,0),(0,1),(0,-1))) else 0))
    ),m.items(),0))
)
