N=input()
n=list(map(int,str(N)))
n.sort(reverse=True)

int_str = ''.join(map(str, n))
print(int_str)

# 숫자형을 리스트로 쪼개는 것과 다시 붙이는 것도 다 map