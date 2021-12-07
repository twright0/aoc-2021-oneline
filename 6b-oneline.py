from aocd import get_data
from functools import reduce
data = get_data(year=2021,day=6)

print(
    (fish := reduce(lambda s, f: (s.update({f:s.get(f,0)+1}) or s),
                    map(int, data.split(",")),
                    {})) and
    (sum(reduce(lambda s, gen: (
        reduce(lambda si, kv: (
            ((si.update({kv[0]-1: si.get(kv[0]-1,0)+kv[1]}) or si)
             if kv[0]>0 else
             ((si.update({8: si.get(8,0)+kv[1]}) or
               si.update({6: si.get(6,0)+kv[1]})) or
              si)
             )), s.items(), {})
        ),
                range(256),
                fish).values()))
)
