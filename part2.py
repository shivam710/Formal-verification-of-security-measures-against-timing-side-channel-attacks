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

#For Prime no. 523 and 541
s.add(key  == 7)
s.add(assign_time == 577)
s.add(add_time == 9929)
s.add(sub_time == 7789)
s.add(mult_time == 997)
s.add(div_time == 2293)
s.add(mod_time == 1831)
s.add(fixed_latency_part1 == 15777857)

#Program 1

timer1 = Int('timer1')
s.add(timer1 == 0)

msg_len1 = Int('msg_len1')
s.add(msg_len1 < 100, msg_len1 >= 0)

itr1 = Int('itr1')
timer11 = Int('timer11')
timer12 = Int('timer12')
timer13 = Int('timer13')
timer14 = Int('timer14')
timer15 = Int('timer15')
timer16 = Int('timer16')
timer1_final = Int('timer1_final')

fixed_latency_parallel1 = Int('fixed_latency_parallel1')
s.add(fixed_latency_parallel1 == 15777857)


s.add(itr1 < 100, itr1 >= 0)

if_condition11 = [ 
timer11 == If(itr1 < msg_len1, timer1 + assign_time, timer1),
timer12 == If(itr1 < msg_len1, timer11 + assign_time, timer11),
timer13 == If(itr1 < msg_len1, timer12 + key * fixed_latency_part1, timer12)
]


if_condition12 = [ 
timer14 == If(itr1 >= msg_len1, timer1 + assign_time, timer1),
timer15 == If(itr1 >= msg_len1, timer14 + assign_time, timer14),
timer16 == If(itr1 >= msg_len1, timer15 + key * fixed_latency_parallel1, timer15)
]

s.add(if_condition11)
s.add(if_condition12)
s.add(timer1_final ==  If(itr1 < msg_len1, timer13, timer16))



#Program 2

timer2 = Int('timer2')
s.add(timer2 == 0)

msg_len2 = Int('msg_len2')
s.add(msg_len2 < 100, msg_len2 >= 0)

itr2 = Int('itr2')
timer21 = Int('timer21')
timer22 = Int('timer22')
timer23 = Int('timer23')
timer24 = Int('timer24')
timer25 = Int('timer25')
timer26 = Int('timer26')
timer2_final = Int('timer2_final')

fixed_latency_parallel2 = Int('fixed_latency_parallel2')
s.add(fixed_latency_parallel2 == 15777857)

s.add(itr2 < 100, itr2 >= 0)

if_condition21 = [ 
timer21 == If(itr2 < msg_len2, timer2 + assign_time, timer2),
timer22 == If(itr2 < msg_len2, timer21 + assign_time, timer21),
timer23 == If(itr2 < msg_len2, timer22 + key * fixed_latency_part1, timer22)
]


if_condition22 = [ 
timer24 == If(itr2 >= msg_len2, timer2 + assign_time, timer2),
timer25 == If(itr2 >= msg_len2, timer24 + assign_time, timer24),
timer26 == If(itr2 >= msg_len2, timer25 + key * fixed_latency_parallel2, timer25)
]

s.add(if_condition21)
s.add(if_condition22)
s.add(timer2_final == If(itr2 < msg_len2, timer23, timer26))


s.add(Not(timer1_final == timer2_final)) #110446153

print("Getting results for part-2")
print()
print(s.check())
# print(s.model())

print()
print("Printing statistics for the solver")
print(s.statistics())
print("-----------------------------------------------------------------")
print()