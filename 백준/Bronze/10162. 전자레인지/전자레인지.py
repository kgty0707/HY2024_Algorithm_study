import sys

T = int(sys.stdin.readline().strip())

A_mo = 300
B_mo = 60
C_mo = 10

A_control_count = 0
B_control_count = 0
C_control_count = 0
remain_time = 0

A_control_count += T // A_mo
remain_time = T % A_mo
B_control_count += remain_time // B_mo
remain_time = remain_time % B_mo
C_control_count = remain_time // C_mo
remain_time = remain_time % C_mo

if not remain_time:
    print(A_control_count, B_control_count, C_control_count)
else: print(-1)