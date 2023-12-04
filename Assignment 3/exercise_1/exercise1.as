# Subtract down to 2
# - R2: loop index
# - R3: loop limit
ldc R2 5
ldc R3 2
loop:
prr R2
ldc R1 1
sub R2 R1
cpy R1 R3
sub R1 R2
bne R1 @loop
hlt
