import sys
input=sys.stdin.readline
N=int(input())
score=0

for i in range(N):
    a=int(input())
    score+=a
print(score-(N-1))
    