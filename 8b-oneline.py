from aocd import get_data
from aocd.transforms import lines
from functools import reduce
data = lines(get_data(day=8,year=2021))

print(reduce(lambda state, row: (
    ((row := row.split("|")) and
     (inp := row[0]) and
     (out := row[1]) and
     (out_bits := list(map(lambda s: "".join(sorted(s)), out.strip().split(" ")))) and
     (bits := list(map(lambda s: "".join(sorted(s)), inp.strip().split(" "))) + out_bits) and
     (one := [b for b in bits if len(b) == 2][0]) and
     (four := [b for b in bits if len(b) == 4][0]) and
     (seven := [b for b in bits if len(b) == 3][0]) and
     (eight := [b for b in bits if len(b) == 7][0]) and
     (seg_zero := [c for c in seven if c not in one][0]) and
     (seg_one_and_three := [c for c in four if c not in one]) and
     (zero := [b for b in bits if len(b) == 6 and seg_zero in b and
               ((seg_one_and_three[0] in b and seg_one_and_three[1] not in b) or
                (seg_one_and_three[1] in b and seg_one_and_three[0] not in b))][0]) and
     (seg_three := [c for c in eight if c not in zero][0]) and
     (seg_one := [c for c in seg_one_and_three if c != seg_three][0]) and
     (five := [b for b in bits if len(b) == 5 and seg_zero in b and seg_one in b and seg_three in b][0]) and
     (seg_five := [c for c in five if c in one][0]) and
     (seg_two := [c for c in one if c not in five][0]) and
     (six := [b for b in bits if len(b) == 6 and seg_two not in b][0]) and
     (two := [b for b in bits if len(b) == 5 and seg_two in b and seg_five not in b][0]) and
     (three := [b for b in bits if len(b) == 5 and seg_two in b and seg_five in b][0]) and
     (nine := [b for b in bits if len(b) == 6 and seg_two in b and b != zero][0]) and
     (mapping := {c: i
                  for i,c in enumerate([zero, one, two, three, four, five, six, seven, eight, nine])}) and
     (state + int(''.join(str(mapping[bit]) for bit in out_bits)))
    )),
             data,0))

"""
for some reason I decided to reference segments by number instead of letter

 0
1 2
 3
4 5
 6
"""
