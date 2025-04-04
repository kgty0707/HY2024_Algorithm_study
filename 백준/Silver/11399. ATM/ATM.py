import sys

num = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))

a.sort()

def search_for_minimum_time(a, num):
    min_time = 0
    wait_time = 0
    for i in range(num):
        wait_time = wait_time + a[i]
        min_time += wait_time
    return min_time

print(search_for_minimum_time(a, num))