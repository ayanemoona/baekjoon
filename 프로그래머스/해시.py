from collections import Counter
def solution(participant, completion):
    result=Counter(participant)-Counter(completion)
    A=list(result.keys())
    return A[0]

### 리스트의 빼기를 위해선 counter를 사용해야 함 for문보다 빠르다