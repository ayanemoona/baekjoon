# 알파벳 횟수세기
# 하나하나 알파벳을 if문으로 물어볼라고 했는데  중복 for문으로 짧게 해결
# 숫자형 리스트 join쓰기 str로 문자열로 바꾼다음에 하기
sample=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
result=[0]*26
s=list(input())
for i in s:
    for j in range(len(sample)):
        if i ==sample[j]:
            result[j]+=1
        else:
            continue
result1=[str(a)for a in result]
print(" ".join(result1))