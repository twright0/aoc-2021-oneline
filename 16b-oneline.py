from aocd import get_data
from itertools import takewhile, repeat
from functools import reduce

print((parse := lambda bs: (
          (
              (size := 6) and
              (int("".join(((size := size+5) and bs[ptr+1:ptr+5]
                            for ptr in takewhile(lambda i: (i == 6 or bs[i-5] == '1'),
                                                 range(6,len(bs),5)))),2),
               size)
          ) if (int(bs[3:6],2) == 4) else (
              (operator := lambda l: ((tid := int(bs[3:6],2)) or True) and (
                  sum(l) if tid == 0 else
                  reduce(lambda x,y: x*y, l) if tid == 1 else
                  min(l) if tid == 2 else
                  max(l) if tid == 3 else
                  int(l[0] > l[1]) if tid == 5 else
                  int(l[0] < l[1]) if tid == 6 else
                  int(l[0] == l[1]) if tid == 7 else
                  None)
               ) and (
              (
                  (to_consume := bs[7+15:]) and
                  (operator(list((
                      (parsed := parse(to_consume)) and
                      ((to_consume := to_consume[parsed[1]:]) or True) and
                      (parsed[0]))
                      for _ in takewhile(lambda _:
                                         len(bs[7+15:]) - len(to_consume) < int(bs[7:7+15],2),
                                         repeat(0)))),
                   len(bs) - len(to_consume))
              ) if bs[6] == '0' else (
                  (to_consume := bs[7+11:]) and
                  (operator(list(((
                      (parsed := parse(to_consume)) and
                      ((to_consume := to_consume[parsed[1]:]) or True) and
                      (parsed[0])) for _ in range(int(bs[7:7+11],2))))),
                   len(bs) - len(to_consume))
              ))
          )
      )) and
      (parse("".join({hex(i)[2:]: format(i, "04b")
                      for i in range(16)}[c.lower()]
                     for c in get_data(year=2021,day=16)))[0])
)
