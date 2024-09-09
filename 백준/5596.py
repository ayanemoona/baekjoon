A,B,C,D=map(int,input().split())
E,F,G,H=map(int,input().split())
S=A+B+C+D
T=E+F+G+H
if S>=T:
    print(S)
elif S<T:
    print(T)