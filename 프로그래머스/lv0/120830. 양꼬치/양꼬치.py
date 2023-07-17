def solution(n, k):
    answer =0
    sumn,sumk=0,0
    
    nx=n//10
    if n>=10:
        k=k-nx

    sumn=12000*n
    sumk=2000*k

    answer=sumn+sumk
    
    return answer