def solution(arr):
    answer = []
    
    for i in range(len(arr)):
        if (i == 0) or (i > 0 and arr[i-1] != arr[i]):
            answer.append(arr[i])
    
    return answer
