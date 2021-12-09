from aocd import get_data
from aocd.transforms import lines
from functools import reduce

print(
    (m := {(i,j): int(v) for i,r in enumerate(lines(get_data(day=9,year=2021))) for j,v in enumerate(r)}) and
    (biggest := max(m.values()) + 1) and
    (get_size := lambda pt: (((i := pt[0]) or True) and
                             ((j := pt[1]) or True) and
                             (0 if (m.get((i,j),biggest) in (9, biggest)) else (
                                 m.update({(i,j):9}) or (1 + sum(map(get_size, ((i+di,j+dj)
                                                                                for di,dj
                                                                                in [(-1,0),(1,0),(0,1),(0,-1)])))))))) and
    (
        reduce(lambda x,y: x*y,
               list(sorted(list(map(get_size, reduce(lambda state, pt: (
            ((v := pt[1]) or True) and ((i := pt[0][0]) or True) and ((j := pt[0][1]) or True) and
            (state + ([(i,j)] if all(m.get((i+di,j+dj),biggest) > v for di, dj in ((-1,0),(1,0),(0,1),(0,-1))) else []))
        ),m.items(),[])
    ))))[-3:]))
)
