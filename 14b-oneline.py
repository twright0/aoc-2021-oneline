from aocd import get_data
from aocd.transforms import lines
from collections import defaultdict
from functools import reduce

print((data := get_data(year=2021,day=14).split("\n\n")) and (start := data[0]) and
      (rules := dict((tuple(r.split(" -> ")) for r in data[1].split("\n")))) and
      (bigrams := reduce(lambda state, _: (
          ((next_bigrams := {}) or True) and
          (list(map(lambda kv: ((k := kv[0]) and (v := kv[1]) and (c := rules[k]) and
                                (k1 := k[0]+c) and (k2 := c+k[1]) and
                                (next_bigrams.update({k1: next_bigrams.get(k1,0)+v})) or
                                (next_bigrams.update({k2: next_bigrams.get(k2,0)+v})) or
                                None),
                    state.items()))) and next_bigrams
      ), range(40), (((bigrams := {}) or True) and
                     (list(map(lambda i: (
                         bigrams.update(
                             {start[i:i+2]: bigrams.get(start[i:i+2],0)+1})),
                         range(len(start)-1)))) and bigrams))) and
      ((stats := {}) or True) and
      (list(map(lambda kv: (
          (k1 := kv[0][0]) and (k2 := kv[0][1]) and (v := kv[1]) and (
              stats.update({k1: stats.get(k1,0)+v}) or stats.update({k2: stats.get(k2,0)+v}))
      ), bigrams.items()))) and
      (stats := {k: (v+1 if k in (start[0],start[-1]) else v) for k,v in stats.items()}) and
      (l := sorted(list(stats.items()), key=lambda kv: kv[1])) and
      (int((l[-1][1] - l[0][1]) / 2))
)
