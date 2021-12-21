from aocd import get_data
from aocd.transforms import lines
from functools import reduce
import json

nums = lines(get_data(year=2021,day=18))

print((init := (lambda v,d,up: (((i := {}) or True) and
                                i.update({'v': v, 'depth': d, 'up': up, 'right': None, 'left': None}
                                         if type(v) != list else
                                         {'v': None, 'depth': d, 'up': up,
                                          'left': init(v[0],d+1,i), 'right': init(v[1],d+1,i)}) or i)
                )) and
      (first_parent := (lambda last, curr, direction: (curr
                                                       if ((not curr) or
                                                           curr[direction] is not last) else
                                                       first_parent(curr, curr['up'], direction)))) and
      (descendent := (lambda curr, direction: (curr
                                               if curr['v'] is not None else
                                               descendent(curr[direction],direction)))) and
      (left_inorder := (lambda n: (
          (parent := first_parent(n, n['up'], 'left')) and
          (descendent(parent['left'], 'right'))
      ))) and
      (right_inorder := (lambda n: (
          (parent := first_parent(n, n['up'], 'right')) and
          (descendent(parent['right'], 'left'))
      ))) and
      (explode := (lambda n: ((
          (
               ((nl := left_inorder(n)) or True) and
               ((nr := right_inorder(n)) or True) and
               (nl.update({'v': nl['v'] + n['left']['v']}) if nl is not None else None) or
               (nr.update({'v': nr['v'] + n['right']['v']}) if nr is not None else None) or
               (n.update({'v': 0, 'right': None, 'left': None})) or
               True
           ) if n['v'] is None and n['depth'] == 4 else
          ((explode(n['left']) or explode(n['right']) or False)
           if n['v'] is None else
           (False)))
      ))) and
      (split := (lambda n: (
          (False if n['v'] < 10 else (
              n.update({'left': init(int(n['v']/2), n['depth']+1, n)}) or
              n.update({'right': init((int(n['v']/2)
                                       if n['v'] % 2 == 0 else
                                       int(n['v']/2)+1),
                                      n['depth']+1,n)}) or
              n.update({'v': None}) or
              True)
           )
          if n['v'] is not None else
          (split(n['left']) or split(n['right']) or False)
      ))) and

      (run_reduction := lambda n: (
          (state := [n]) and
          reduce(lambda _, n: (state.append(n)
                               if explode(n) or split(n) else
                               n),
                 state, None))) and

      (magnitude := (lambda n: n['v'] if n['v'] is not None else (3 * magnitude(n['left']) +
                                                                  2 * magnitude(n['right'])))) and
      (incr := (lambda n: (n.update({'depth': n['depth']+1}) or
                           (incr(n['right']) if n['right'] is not None else True) and
                           (incr(n['left']) if n['left'] is not None else True)) and True)) and

      magnitude(reduce(lambda state, num: (
          incr(state) and
          (n2 := init(json.loads(num),0,None)) and
          incr(n2) and
          (new_state := init(0,0,None)) and
          (new_state.update({'right': n2, 'left': state, 'v': None}) or True) and
          (n2.update({'up': new_state}) or True) and
          (state.update({'up': new_state}) or True) and
          run_reduction(new_state) and
          new_state
      ), nums[1:], init(json.loads(nums[0]),0,None)))
)
