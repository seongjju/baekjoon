def solution(n):
    answer = ''
    for i in range(n):
        if n%2==1:
            if i%2==1:
                answer+="박"
            else:
                answer+="수"
        else:
            if i%2==1:
                answer+="박"
            else:
                answer+="수"
                    
    return answer