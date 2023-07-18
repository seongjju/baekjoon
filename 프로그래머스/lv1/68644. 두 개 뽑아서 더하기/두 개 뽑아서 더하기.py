def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i!=j:
                answer.append(numbers[i]+numbers[j])
    a=list(set(answer))
    x=sorted(a)
            
    return x