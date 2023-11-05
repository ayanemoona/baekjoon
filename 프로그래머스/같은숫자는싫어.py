def no_continuous(s):
    # 함수를 완성하세요
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( no_continuous( "133303" ))

# [-1:]은 빈칸일 때도 비교가 가능
# [i]는 리스트 i는 int i로 비교하면 의미 없음