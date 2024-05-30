import sys
from pprint import pprint
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
pprint(arr)

