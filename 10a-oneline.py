from aocd import get_data
from aocd.transforms import lines
data = lines(get_data(year=2021,day=10))

print(sum(map(lambda row: (
    (scores := {')': 3, ']': 57, '}': 1197, '>': 25137}) and
    (row_state := [row]) and
    ((reduced := list(map(lambda r:
             ((removable_char_idx := (
                 ((r.find('()')+1) or
                  (r.find('[]')+1) or
                  (r.find('{}')+1) or
                  (r.find('<>')+1) or 0)-1
             )) or True) and
             ((row_state.pop() and row_state.append("") or row_state.append(r[:removable_char_idx]+r[removable_char_idx+2:]) and None)
              if removable_char_idx >=0
              else r),
             row_state))[-1]
      ) or True) and
    ((close_char_list := [c for c in reduced if c in scores]) or True) and
    (0 if not close_char_list else scores[close_char_list[0]])
),data)))
