import sys
from pprint import pprint
input = sys.stdin.readline
n = int(input())

for test_case in range(n):
    arr = [list(input().strip()) for _ in range(5)]
    input()
    pprint(arr)

