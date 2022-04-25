from z3 import *

s = Solver()

key = Int('key')
assign_time = Int('assign_time')
add_time = Int('add_time')
sub_time = Int('sub_time')
mult_time = Int('mult_time')
div_time = Int('div_time')
mod_time = Int('mod_time')
fixed_latency_part1 = Int('fixed_latency_part1')
fixed_latency_part2 = Int('fixed_latency_part2')

#For Prime no. 523 and 541
s.add(key  == 7)
s.add(assign_time == 577)
s.add(add_time == 9929)
s.add(sub_time == 7789)
s.add(mult_time == 997)
s.add(div_time == 2293)
s.add(mod_time == 1831)
s.add(fixed_latency_part1 == 15777857)
s.add(fixed_latency_part2 == 110446153)

#Program 1

timer1 = Int('timer1')
timer1_final = Int('timer1_final')
s.add(timer1 == 0)

msg_len1 = Int('msg_len1')
s.add(msg_len1 < 100, msg_len1 >= 0)


s.add(timer1_final == timer1 + 100 * fixed_latency_part2)



#Program 2

timer2 = Int('timer2')
timer2_final = Int('timer2_final')
s.add(timer2 == 0)

msg_len2 = Int('msg_len2')
s.add(msg_len2 < 100, msg_len2 >= 0)

s.add(timer2_final == timer2 + 100 * fixed_latency_part2)

s.add(Not(timer1_final == timer2_final))

print("Getting results for part-3")
print()
print(s.check())
# print(s.model())

print()
print("Printing statistics for the solver")
print(s.statistics())
print("-----------------------------------------------------------------")
print()
