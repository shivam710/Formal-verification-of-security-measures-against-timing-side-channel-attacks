from z3 import *

s = Solver()

# Declaration of timing values
key = Int('key')
assign_time = Int('assign_time')
add_time = Int('add_time')
sub_time = Int('sub_time')
mult_time = Int('mult_time')
div_time = Int('div_time')
mod_time = Int('mod_time')
fixed_latency = Int('fixed_latency')

#For Prime no. 523 and 541
s.add(key  == 7)
s.add(assign_time == 577)
s.add(add_time == 9929)
s.add(sub_time == 7789)
s.add(mult_time == 997)
s.add(div_time == 2293)
s.add(mod_time == 1831)
s.add(fixed_latency == 15777857)

#Program 1

# initalize timer
timer1 = Int('timer1')
s.add(timer1 == 0)

# Secret key
msg1 = Int('msg1')
s.add(msg1 < 2147483647, msg1 >= 0) #INT_MAX value

timer_parallel1 = Int('timer_parallel1')
timer11 = Int('timer11')
timer12 = Int('timer12')
timer13 = Int('timer13')
timer14 = Int('timer14')
timer15 = Int('timer15')
timer16 = Int('timer16')
timer17 = Int('timer17')
timer18 = Int('timer18')
timer19 = Int('timer19')
timer110 = Int('timer110')
timer111 = Int('timer111')
timer112 = Int('timer112')
timer113 = Int('timer113')
timer114 = Int('timer114')
timer115 = Int('timer115')
timer116 = Int('timer116')
timer117 = Int('timer117')
timer118 = Int('timer118')
timer119 = Int('timer119')
timer120 = Int('timer120')
timer121 = Int('timer121')
timer122 = Int('timer122')
timer123 = Int('timer123')
timer124 = Int('timer124')
timer125 = Int('timer125')
timer126 = Int('timer126')
timer127 = Int('timer127')
timer128 = Int('timer128')
timer129 = Int('timer129')
timer130 = Int('timer130')
timer131 = Int('timer131')
timer132 = Int('timer132')
timer133 = Int('timer133')
timer134 = Int('timer134')
timer135 = Int('timer135')
timer136 = Int('timer136')
timer137 = Int('timer137')
timer138 = Int('timer138')
timer139 = Int('timer139')
timer140 = Int('timer140')
timer141 = Int('timer141')
timer142 = Int('timer142')
timer143 = Int('timer143')
timer144 = Int('timer144')
timer145 = Int('timer145')
timer146 = Int('timer146')
timer147 = Int('timer147')
timer148 = Int('timer148')
timer149 = Int('timer149')
timer150 = Int('timer150')
timer151 = Int('timer151')
timer152 = Int('timer152')
timer153 = Int('timer153')
timer154 = Int('timer154')
timer155 = Int('timer155')
timer156 = Int('timer156')
timer157 = Int('timer157')
timer158 = Int('timer158')
timer159 = Int('timer159')
timer160 = Int('timer160')
timer161 = Int('timer161')
timer162 = Int('timer162')
timer163 = Int('timer163')
timer164 = Int('timer164')
timer165 = Int('timer165')
timer166 = Int('timer166')
timer167 = Int('timer167')
timer168 = Int('timer168')
timer169 = Int('timer169')
timer170 = Int('timer170')
timer171 = Int('timer171')
timer172 = Int('timer172')
timer173 = Int('timer173')
timer174 = Int('timer174')
timer175 = Int('timer175')
timer176 = Int('timer176')
timer177 = Int('timer177')
timer178 = Int('timer178')
timer179 = Int('timer179')

# Latency for parallel compensation code.
s.add(timer_parallel1 == fixed_latency)


# Latency for multiplication part
if_condition11 = [ 
timer11 == If(And(msg1 >= 1073741824, msg1 <  2147483647), timer1 + 32 * mult_time, timer1),
timer12 == If(And(msg1 >= 536870912, msg1 <  1073741824), timer11 + 31 * mult_time, timer11),
timer13 == If(And(msg1 >= 268435456, msg1 <  536870912), timer12 + 30 * mult_time, timer12),
timer14 == If(And(msg1 >= 134217728, msg1 <  268435456), timer13 + 29 * mult_time, timer13),
timer15 == If(And(msg1 >= 67108864, msg1 <  134217728), timer14 + 28 * mult_time, timer14),
timer16 == If(And(msg1 >= 33554432, msg1 <  67108864), timer15 + 27 * mult_time, timer15),
timer17 == If(And(msg1 >= 16777216, msg1 <  33554432), timer16 + 26 * mult_time, timer16),
timer18 == If(And(msg1 >= 8388608, msg1 <  16777216), timer17 + 25 * mult_time, timer17),
timer19 == If(And(msg1 >= 4194304, msg1 <  8388608), timer18 + 24 * mult_time, timer18),
timer110 == If(And(msg1 >= 2097152, msg1 <  4194304), timer19 + 23 * mult_time, timer19),
timer111 == If(And(msg1 >= 1048576, msg1 <  2097152), timer110 + 22 * mult_time, timer110),
timer112 == If(And(msg1 >= 524288, msg1 <  1048576), timer111 + 21 * mult_time, timer111),
timer113 == If(And(msg1 >= 262144, msg1 <  524288), timer112 + 20 * mult_time, timer112),
timer114 == If(And(msg1 >= 131072, msg1 <  262144), timer113 + 19 * mult_time, timer113),
timer115 == If(And(msg1 >= 65536, msg1 <  131072), timer114 + 18 * mult_time, timer114),
timer116 == If(And(msg1 >= 32768, msg1 <  65536), timer115 + 17 * mult_time, timer115),
timer117 == If(And(msg1 >= 16384, msg1 <  32768), timer116 + 16 * mult_time, timer116),
timer118 == If(And(msg1 >= 8192, msg1 <  16384), timer117 + 15 * mult_time, timer117),
timer119 == If(And(msg1 >= 4096, msg1 <  8192), timer118 + 14 * mult_time, timer118),
timer120 == If(And(msg1 >= 2048, msg1 <  4096), timer119 + 13 * mult_time, timer119),
timer121 == If(And(msg1 >= 1024, msg1 <  2048), timer120 + 12 * mult_time, timer120),
timer122 == If(And(msg1 >= 512, msg1 <  1024), timer121 + 11 * mult_time, timer121),
timer123 == If(And(msg1 >= 256, msg1 <  512), timer122 + 10 * mult_time, timer122),
timer124 == If(And(msg1 >= 128, msg1 <  256), timer123 + 9 * mult_time, timer123),
timer125 == If(And(msg1 >= 64, msg1 <  128), timer124 + 8 * mult_time, timer124),
timer126 == If(And(msg1 >= 32, msg1 <  64), timer125 + 7 * mult_time, timer125),
timer127 == If(And(msg1 >= 16, msg1 <  32), timer126 + 6 * mult_time, timer126),
timer128 == If(And(msg1 >= 8, msg1 <  16), timer127 + 5 * mult_time, timer127),
timer129 == If(And(msg1 >= 4, msg1 <  8), timer128 + 4 * mult_time, timer128),
timer130 == If(And(msg1 >= 2, msg1 <  4), timer129 + 3 * mult_time, timer129),
timer131 == If(And(msg1 >= 1, msg1 <  2), timer130 + 2 * mult_time, timer130),
timer132 == If(And(msg1 >= 0, msg1 <  1), timer131 + 1 * mult_time, timer131),

]

#Latency for mod part
if_condition12 = [ 
timer141 == If(And(msg1 >= 1073741824, msg1 <  2147483647), timer132 + 32 * mod_time, timer132),
timer142 == If(And(msg1 >= 536870912, msg1 <  1073741824), timer141 + 31 * mod_time, timer141),
timer143 == If(And(msg1 >= 268435456, msg1 <  536870912), timer142 + 30 * mod_time, timer142),
timer144 == If(And(msg1 >= 134217728, msg1 <  268435456), timer143 + 29 * mod_time, timer143),
timer145 == If(And(msg1 >= 67108864, msg1 <  134217728), timer144 + 28 * mod_time, timer144),
timer146 == If(And(msg1 >= 33554432, msg1 <  67108864), timer145 + 27 * mod_time, timer145),
timer147 == If(And(msg1 >= 16777216, msg1 <  33554432), timer146 + 26 * mod_time, timer146),
timer148 == If(And(msg1 >= 8388608, msg1 <  16777216), timer147 + 25 * mod_time, timer147),
timer149 == If(And(msg1 >= 4194304, msg1 <  8388608), timer148 + 24 * mod_time, timer148),
timer150 == If(And(msg1 >= 2097152, msg1 <  4194304), timer149 + 23 * mod_time, timer149),
timer151 == If(And(msg1 >= 1048576, msg1 <  2097152), timer150 + 22 * mod_time, timer150),
timer152 == If(And(msg1 >= 524288, msg1 <  1048576), timer151 + 21 * mod_time, timer151),
timer153 == If(And(msg1 >= 262144, msg1 <  524288), timer152 + 20 * mod_time, timer152),
timer154 == If(And(msg1 >= 131072, msg1 <  262144), timer153 + 19 * mod_time, timer153),
timer155 == If(And(msg1 >= 65536, msg1 <  131072), timer154 + 18 * mod_time, timer154),
timer156 == If(And(msg1 >= 32768, msg1 <  65536), timer155 + 17 * mod_time, timer155),
timer157 == If(And(msg1 >= 16384, msg1 <  32768), timer156 + 16 * mod_time, timer156),
timer158 == If(And(msg1 >= 8192, msg1 <  16384), timer157 + 15 * mod_time, timer157),
timer159 == If(And(msg1 >= 4096, msg1 <  8192), timer158 + 14 * mod_time, timer158),
timer160 == If(And(msg1 >= 2048, msg1 <  4096), timer159 + 13 * mod_time, timer159),
timer161 == If(And(msg1 >= 1024, msg1 <  2048), timer160 + 12 * mod_time, timer160),
timer162 == If(And(msg1 >= 512, msg1 <  1024), timer161 + 11 * mod_time, timer161),
timer163 == If(And(msg1 >= 256, msg1 <  512), timer162 + 10 * mod_time, timer162),
timer164 == If(And(msg1 >= 128, msg1 <  256), timer163 + 9 * mod_time, timer163),
timer165 == If(And(msg1 >= 64, msg1 <  128), timer164 + 8 * mod_time, timer164),
timer166 == If(And(msg1 >= 32, msg1 <  64), timer165 + 7 * mod_time, timer165),
timer167 == If(And(msg1 >= 16, msg1 <  32), timer166 + 6 * mod_time, timer166),
timer168 == If(And(msg1 >= 8, msg1 <  16), timer167 + 5 * mod_time, timer167),
timer169 == If(And(msg1 >= 4, msg1 <  8), timer168 + 4 * mod_time, timer168),
timer170 == If(And(msg1 >= 2, msg1 <  4), timer129 + 3 * mod_time, timer129),
timer171 == If(And(msg1 >= 1, msg1 <  2), timer170 + 2 * mod_time, timer170),
timer172 == If(And(msg1 >= 0, msg1 <  1), timer171 + 1 * mod_time, timer171),

]


# Adding multiplication and mod part
s.add(if_condition11)
s.add(if_condition12)
timer1_final = Int('timer1_final')

# Getting final time.
s.add(timer1_final ==  If(timer_parallel1 > timer172, timer_parallel1, timer172))



#Program 2

# initalize timer
timer2 = Int('timer2')
s.add(timer2 == 0)

# secret key
msg2 = Int('msg2')
s.add(msg2 < 2147483647, msg2 >= 0) #INT_MAX value

timer_parallel2 = Int('timer_parallel2')
timer21 = Int('timer21')
timer22 = Int('timer22')
timer23 = Int('timer23')
timer24 = Int('timer24')
timer25 = Int('timer25')
timer26 = Int('timer26')
timer27 = Int('timer27')
timer28 = Int('timer28')
timer29 = Int('timer29')
timer210 = Int('timer210')
timer211 = Int('timer211')
timer212 = Int('timer212')
timer213 = Int('timer213')
timer214 = Int('timer214')
timer215 = Int('timer215')
timer216 = Int('timer216')
timer217 = Int('timer217')
timer218 = Int('timer218')
timer219 = Int('timer219')
timer220 = Int('timer220')
timer221 = Int('timer221')
timer222 = Int('timer222')
timer223 = Int('timer223')
timer224 = Int('timer224')
timer225 = Int('timer225')
timer226 = Int('timer226')
timer227 = Int('timer227')
timer228 = Int('timer228')
timer229 = Int('timer229')
timer230 = Int('timer230')
timer231 = Int('timer231')
timer232 = Int('timer232')
timer233 = Int('timer233')
timer234 = Int('timer234')
timer235 = Int('timer235')
timer236 = Int('timer236')
timer237 = Int('timer237')
timer238 = Int('timer238')
timer239 = Int('timer239')
timer240 = Int('timer240')
timer241 = Int('timer241')
timer242 = Int('timer242')
timer243 = Int('timer243')
timer244 = Int('timer244')
timer245 = Int('timer245')
timer246 = Int('timer246')
timer247 = Int('timer247')
timer248 = Int('timer248')
timer249 = Int('timer249')
timer250 = Int('timer250')
timer251 = Int('timer251')
timer252 = Int('timer252')
timer253 = Int('timer253')
timer254 = Int('timer254')
timer255 = Int('timer255')
timer256 = Int('timer256')
timer257 = Int('timer257')
timer258 = Int('timer258')
timer259 = Int('timer259')
timer260 = Int('timer260')
timer261 = Int('timer261')
timer262 = Int('timer262')
timer263 = Int('timer263')
timer264 = Int('timer264')
timer265 = Int('timer265')
timer266 = Int('timer266')
timer267 = Int('timer267')
timer268 = Int('timer268')
timer269 = Int('timer269')
timer270 = Int('timer270')
timer271 = Int('timer271')
timer272 = Int('timer272')
timer273 = Int('timer273')
timer274 = Int('timer274')
timer275 = Int('timer275')
timer276 = Int('timer276')
timer277 = Int('timer277')
timer278 = Int('timer278')
timer279 = Int('timer279')

# Latency for parallel compensation code.
s.add(timer_parallel2 == fixed_latency)

#Latency for multiplication part
if_condition21 = [ 
timer21 == If(And(msg2 >= 1073741824, msg2 <  2147483647), timer2 + 32 * mult_time, timer2),
timer22 == If(And(msg2 >= 536870912, msg2 <  1073741824), timer21 + 31 * mult_time, timer21),
timer23 == If(And(msg2 >= 268435456, msg2 <  536870912), timer22 + 30 * mult_time, timer22),
timer24 == If(And(msg2 >= 134217728, msg2 <  268435456), timer23 + 29 * mult_time, timer23),
timer25 == If(And(msg2 >= 67108864, msg2 <  134217728), timer24 + 28 * mult_time, timer24),
timer26 == If(And(msg2 >= 33554432, msg2 <  67108864), timer25 + 27 * mult_time, timer25),
timer27 == If(And(msg2 >= 16777216, msg2 <  33554432), timer26 + 26 * mult_time, timer26),
timer28 == If(And(msg2 >= 8388608, msg2 <  16777216), timer27 + 25 * mult_time, timer27),
timer29 == If(And(msg2 >= 4194304, msg2 <  8388608), timer28 + 24 * mult_time, timer28),
timer210 == If(And(msg2 >= 2097152, msg2 <  4194304), timer29 + 23 * mult_time, timer29),
timer211 == If(And(msg2 >= 1048576, msg2 <  2097152), timer210 + 22 * mult_time, timer210),
timer212 == If(And(msg2 >= 524288, msg2 <  1048576), timer211 + 21 * mult_time, timer211),
timer213 == If(And(msg2 >= 262144, msg2 <  524288), timer212 + 20 * mult_time, timer212),
timer214 == If(And(msg2 >= 131072, msg2 <  262144), timer213 + 19 * mult_time, timer213),
timer215 == If(And(msg2 >= 65536, msg2 <  131072), timer214 + 18 * mult_time, timer214),
timer216 == If(And(msg2 >= 32768, msg2 <  65536), timer215 + 17 * mult_time, timer215),
timer217 == If(And(msg2 >= 16384, msg2 <  32768), timer216 + 16 * mult_time, timer216),
timer218 == If(And(msg2 >= 8192, msg2 <  16384), timer217 + 15 * mult_time, timer217),
timer219 == If(And(msg2 >= 4096, msg2 <  8192), timer218 + 14 * mult_time, timer218),
timer220 == If(And(msg2 >= 2048, msg2 <  4096), timer219 + 13 * mult_time, timer219),
timer221 == If(And(msg2 >= 1024, msg2 <  2048), timer220 + 12 * mult_time, timer220),
timer222 == If(And(msg2 >= 512, msg2 <  1024), timer221 + 11 * mult_time, timer221),
timer223 == If(And(msg2 >= 256, msg2 <  512), timer222 + 10 * mult_time, timer222),
timer224 == If(And(msg2 >= 128, msg2 <  256), timer223 + 9 * mult_time, timer223),
timer225 == If(And(msg2 >= 64, msg2 <  128), timer224 + 8 * mult_time, timer224),
timer226 == If(And(msg2 >= 32, msg2 <  64), timer225 + 7 * mult_time, timer225),
timer227 == If(And(msg2 >= 16, msg2 <  32), timer226 + 6 * mult_time, timer226),
timer228 == If(And(msg2 >= 8, msg2 <  16), timer227 + 5 * mult_time, timer227),
timer229 == If(And(msg2 >= 4, msg2 <  8), timer228 + 4 * mult_time, timer228),
timer230 == If(And(msg2 >= 2, msg2 <  4), timer229 + 3 * mult_time, timer229),
timer231 == If(And(msg2 >= 1, msg2 <  2), timer230 + 2 * mult_time, timer230),
timer232 == If(And(msg2 >= 0, msg2 <  1), timer231 + 1 * mult_time, timer231),

]

#Latency for mod part
if_condition22 = [ 
timer241 == If(And(msg2 >= 1073741824, msg2 <  2147483647), timer232 + 32 * mod_time, timer232),
timer242 == If(And(msg2 >= 536870912, msg2 <  1073741824), timer241 + 31 * mod_time, timer241),
timer243 == If(And(msg2 >= 268435456, msg2 <  536870912), timer242 + 30 * mod_time, timer242),
timer244 == If(And(msg2 >= 134217728, msg2 <  268435456), timer243 + 29 * mod_time, timer243),
timer245 == If(And(msg2 >= 67108864, msg2 <  134217728), timer244 + 28 * mod_time, timer244),
timer246 == If(And(msg2 >= 33554432, msg2 <  67108864), timer245 + 27 * mod_time, timer245),
timer247 == If(And(msg2 >= 16777216, msg2 <  33554432), timer246 + 26 * mod_time, timer246),
timer248 == If(And(msg2 >= 8388608, msg2 <  16777216), timer247 + 25 * mod_time, timer247),
timer249 == If(And(msg2 >= 4194304, msg2 <  8388608), timer248 + 24 * mod_time, timer248),
timer250 == If(And(msg2 >= 2097152, msg2 <  4194304), timer249 + 23 * mod_time, timer249),
timer251 == If(And(msg2 >= 1048576, msg2 <  2097152), timer250 + 22 * mod_time, timer250),
timer252 == If(And(msg2 >= 524288, msg2 <  1048576), timer251 + 21 * mod_time, timer251),
timer253 == If(And(msg2 >= 262144, msg2 <  524288), timer252 + 20 * mod_time, timer252),
timer254 == If(And(msg2 >= 131072, msg2 <  262144), timer253 + 19 * mod_time, timer253),
timer255 == If(And(msg2 >= 65536, msg2 <  131072), timer254 + 18 * mod_time, timer254),
timer256 == If(And(msg2 >= 32768, msg2 <  65536), timer255 + 17 * mod_time, timer255),
timer257 == If(And(msg2 >= 16384, msg2 <  32768), timer256 + 16 * mod_time, timer256),
timer258 == If(And(msg2 >= 8192, msg2 <  16384), timer257 + 15 * mod_time, timer257),
timer259 == If(And(msg2 >= 4096, msg2 <  8192), timer258 + 14 * mod_time, timer258),
timer260 == If(And(msg2 >= 2048, msg2 <  4096), timer259 + 13 * mod_time, timer259),
timer261 == If(And(msg2 >= 1024, msg2 <  2048), timer260 + 12 * mod_time, timer260),
timer262 == If(And(msg2 >= 512, msg2 <  1024), timer261 + 11 * mod_time, timer261),
timer263 == If(And(msg2 >= 256, msg2 <  512), timer262 + 10 * mod_time, timer262),
timer264 == If(And(msg2 >= 128, msg2 <  256), timer263 + 9 * mod_time, timer263),
timer265 == If(And(msg2 >= 64, msg2 <  128), timer264 + 8 * mod_time, timer264),
timer266 == If(And(msg2 >= 32, msg2 <  64), timer265 + 7 * mod_time, timer265),
timer267 == If(And(msg2 >= 16, msg2 <  32), timer266 + 6 * mod_time, timer266),
timer268 == If(And(msg2 >= 8, msg2 <  16), timer267 + 5 * mod_time, timer267),
timer269 == If(And(msg2 >= 4, msg2 <  8), timer268 + 4 * mod_time, timer268),
timer270 == If(And(msg2 >= 2, msg2 <  4), timer229 + 3 * mod_time, timer229),
timer271 == If(And(msg2 >= 1, msg2 <  2), timer270 + 2 * mod_time, timer270),
timer272 == If(And(msg2 >= 0, msg2 <  1), timer271 + 1 * mod_time, timer271),

]


# Adding multiplication and mod part
s.add(if_condition21)
s.add(if_condition22)
timer2_final = Int('timer2_final')

# Getting final time.
s.add(timer2_final ==  If(timer_parallel2 > timer272, timer_parallel2, timer272))

# Check using sat problem.
s.add(Not(timer1_final == timer2_final))

print("Getting results for part-1")
print()
print(s.check())
# print(s.model())

print()
print("Printing statistics for the solver")
print(s.statistics())
print("-----------------------------------------------------------------")
print()









