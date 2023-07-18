def solution(array, commands):
    answer = []
    for cmd in commands:
        i = cmd[0] - 1  
        j = cmd[1]
        k = cmd[2]
        
        sub_array = array[i:j]  
        sub_array.sort()  
        answer.append(sub_array[k - 1]) 

    return answer
