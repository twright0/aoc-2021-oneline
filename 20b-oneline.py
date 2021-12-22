from aocd import get_data
from collections import defaultdict
data = get_data(day=20,year=2021).split("\n\n")

print((algo := data[0]) and
      (image := data[1]) and
      ((min_x := 0) or (min_y := 0) or (max_x := 0) or (max_y := 0) or True) and
      ((image_data := defaultdict(lambda: '.')) or True) and
      all(((max_x := max(max_x, x)) or True) and ((max_y := max(max_y, y)) or True) and
          (image_data.update({(x,y): c}) or True) and
          True
          for y, row in enumerate(image.split("\n"))
          for x, c in enumerate(row)) and
      all((((next_image_data := defaultdict(lambda: '#' if n % 2 else '.')) or True) and
           ((min_x := min_x - 2) or True) and ((min_y := min_y - 2) or True) and
           ((max_x := max_x + 2) or True) and ((max_y := max_y + 2) or True) and
           all(((v := "".join((('1' if image_data[(x+dx,y+dy)] == '#' else '0')
                               for dy in range(-1,2)
                               for dx in range(-1,2)))) and
                (next_image_data.update({(x,y): algo[int(v, 2)]}) or True) and
                True)
               for y in range(min_y, max_y+1)
               for x in range(min_x, max_x+1)) and
           (image_data := next_image_data) and
           True)
          for n in range(50)) and

      sum(1 if v == '#' else 0 for v in next_image_data.values())
)
