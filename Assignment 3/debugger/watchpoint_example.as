# initialize R0 as base address of an array
# initialize R1 as the array size
# initialize R2 as the item
ldc R0 100
ldc R1 5
ldc R2 10
loop:
prr R1
# store the value in R2 at the memory location pointed by R0
str R2 R0
prm R0
inc R0   
inc R2
dec R1
bne R1 @loop
# decrease index of R0 by 1 to the last index of the array
dec R0
# initialize R1 as the start of the memory location
ldc R1 100
reverse_loop:
# load the value of the start of the array to R2
ldr R2 R1
# load the value from the memory location pointed by R0 into R3
ldr R3 R0
# store the value from the end to the start
str R3 R1
# store the value from the start to end
str R2 R0
inc R1
dec R0
# copy the start pointer to R4
cpy R4 R1
sub R4 R0
# stop when both pointer meets
bne R4 @reverse_loop
hlt