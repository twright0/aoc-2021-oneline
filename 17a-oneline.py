from aocd import get_data
from functools import reduce

print(
    (bounds := tuple(map(lambda s: tuple(map(int, s.replace("x=","").replace("y=","").split(".."))),
                         get_data(year=2021,day=17).replace("target area: ","").split(", ")))) and
    ((xmin := bounds[0][0]) or True) and ((xmax := bounds[0][1]) or True) and
    ((ymin := bounds[1][0]) or True) and ((ymax := bounds[1][1]) or True) and
    (hits := lambda xv, yv: (
        (state := [(0,0,-10000000,xv,yv)]) and
        (list(map((lambda xym: (((x := xym[0] + xym[3]) or True) and ((y := xym[1] + xym[4]) or True) and
                                ((max_height := max(xym[2], y)) or True) and
                                ((yv := xym[4] - 1) or True) and ((xv := max(0, xym[3] - 1)) or True) and
                                (max_height if ((xmin <= x <= xmax) and (ymin <= y <= ymax)) else
                                 None if y < ymin else
                                 (state.append((x,y,max_height,xv,yv)))))),
                state))))) and
    max(list(map(lambda xvel: (
        ((yvel := ymax-1) or True) and
        max(([(
            ((v := hits(xvel, yvel)[-1]) or True) and
            (v if v is not None else 0))
              for yvel in range(-300,300)]))
    ),range(1,xmax+1))))
)
