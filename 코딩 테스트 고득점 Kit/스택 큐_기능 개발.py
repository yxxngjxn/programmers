"""
import math

def solution(progresses, speeds):
    completiones = []
    answer = []
    
    for progress, speed in zip(progresses, speeds):
        completion = math.ceil((100 - progress) / speed)
        completiones.append(completion)
    
    for i in range(len(completiones)):
        if (i == 0) or (i > 0 and completiones[i] > completiones[i-1]):
            answer.append(1)
        else:
            answer[-1] += 1
    
    return answer
"""

def solution(progresses, speeds):
    answer = []
    
    # 작업이 끝날 때까지 반복
    while speeds:
        for index, speed in enumerate(speeds):
            progresses[index] += speed
        
        count = 0 # 배포할 작업 개수
        
        # 첫 번째 작업의 진도가 100% 이상이 될 경우
        # progresses, speeds에서 해당 작업 삭제 및 배포할 작업 개수 증가
        while progresses and progresses[0] >= 100:
            del progresses[0], speeds[0]
            count += 1
        
        # 배포할 작업의 개수를 결과 리스트에 추가
        if count > 0:
            answer.append(count)
    
    return answer
