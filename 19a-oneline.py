from aocd import get_data
from itertools import takewhile, repeat
from collections import deque
data = get_data(day=19,year=2021).split("\n\n")

print((pts_per_scanner := [[tuple(map(int, r.split(","))) for r in b.split("\n")[1:]]
                           for b in get_data(day=19,year=2021).split("\n\n")]) and
      (vec_sum := lambda v1, v2, mul: tuple((v + (mul*vv) for v,vv in zip(v1,v2)))) and
      (translate := lambda pts: ((rotate_x := lambda p: (p[0], p[2], -1 * p[1])) and
                                 (rotate_y := lambda p: (p[2], p[1], -1 * p[0])) and
                                 (rotate_z := lambda p: (-1 * p[1], p[0], p[2])) and
                                 (all_rotates := lambda pt,xs,ys,zs: (
                                     (p := pt) and
                                     (deque(((p := rotate_x(p)) for _ in range(xs)),maxlen=0) or True) and
                                     (deque(((p := rotate_y(p)) for _ in range(ys)),maxlen=0) or True) and
                                     (deque(((p := rotate_z(p)) for _ in range(zs)),maxlen=0) or True) and
                                     p)) and
                                 ((outs := []) or True) and
                                 ([outs.append([all_rotates(p,xs,ys,zs)
                                                for xs in range(4)
                                                for ys in range(4)
                                                for zs in range(4)])
                                   for p in pts]) and
                                 set(zip(*outs)))) and

      (matches := lambda new_pts, pts_set, scanner_locs: (
          (early_halt := False) or
          deque(((scanner_loc_vec := vec_sum(ref_pt,trans_pt,-1)) and
           (num_overlaps := 0 if scanner_loc_vec in scanner_locs else
            (sum(((trans_pt_2 := vec_sum(tp2,scanner_loc_vec,1)) and
                                  (
                 (1 if trans_pt_2 in pts_set else
                  float("-inf") if any((all([abs(v-vv)<=1000
                                             for v,vv in zip(vec_sum(trans_pt_2,scanner_loc_vec,1),scan_pt)])
                                        for scan_pt in scanner_locs)) else
                  0)
                                  )
                                  for tp2 in translated)))) and
           (((scanner_locs.add(scanner_loc_vec)) or True and
             (early_halt := True) and
             (pts_set.update((vec_sum(trans_pt_2,scanner_loc_vec,1) for trans_pt_2 in translated)) or True) and
             True) if num_overlaps >= 12 else False)
           for ref_pt in takewhile(lambda _: not early_halt, pts_set.copy())
           for translated in takewhile(lambda _: not early_halt, translate(new_pts))
           for trans_pt in takewhile(lambda _: not early_halt, translated )
                             ), maxlen=0)
          or early_halt
      )) and

      (all_pts := set(pts_per_scanner.pop(0))) and
      (scanner_locs := set([(0,0,0)])) and

      ([(to_pop := (
          [i if matches(pts,all_pts,scanner_locs) else None
           for i,pts in enumerate(pts_per_scanner)])) and
        all(True for _ in (pts_per_scanner.pop(i) for i in to_pop[::-1] if i is not None)) and
        True
        for _ in takewhile(lambda _: not not pts_per_scanner, repeat(0))]) and

      len(all_pts)
)
