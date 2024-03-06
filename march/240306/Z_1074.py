'''
1. 4개로 나누었을 때 어디 있는지 파악
2. 반복
'''

import sys

n, r, c = map(int, sys.stdin.readline().strip().split())

quotient = (2**n) * (2**n) // 4
remainder = (2**n) * (2**n) % 4

