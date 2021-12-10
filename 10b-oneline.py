from aocd import get_data
from aocd.transforms import lines
from functools import reduce
data = lines(get_data(year=2021,day=10))

print(
    (incompletes := list(filter(lambda x:x, list(map(lambda row: (
        ((scores := {'(': 1, '[': 2, '{': 3, '<': 4}) or True) and
        (row_state := [row]) and
        ((reduced := list(map(lambda r:
                 ((removable_char_idx := (
                     ((r.find('()')+1) or
                      (r.find('[]')+1) or
                      (r.find('{}')+1) or
                      (r.find('<>')+1) or 0)-1
                 )) or True) and
                 ((row_state.append(r[:removable_char_idx]+r[removable_char_idx+2:]) and None) if removable_char_idx >=0 else r),
                 row_state))[-1]
          ) or True) and
        (0 if any(c not in scores for c in reduced) else reduce(lambda total, c: (5 * total) + scores[c], reduced[::-1], 0))
    ),data))))) and
    sorted(incompletes)[int(len(incompletes)/2)]
)
