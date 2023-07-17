def solution(s):
    answer = ''
    a=len(s)//2
    if len(s)%2==1:
        answer=s[a]
    else:
        answer=s[a-1:a+1]
    return answer

