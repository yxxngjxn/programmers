from collections import deque

def solution(priorities, location):
    # priorities_queue: 대기 중인 프로세스의 기존 순서(location)와 우선순위(priority) 리스트
    # count: 프로세스 실행 횟수
    priorities_queue = deque(enumerate(priorities))
    count = 0
    priorities.sort()
    
    while priorities_queue:
        # max_priority: 가장 높은 우선순위
        max_priority = priorities[-1]
        
        # 실행될 차례인 프로세스의 우선순위가 가장 높은 경우 → 실행 O
        if priorities_queue[0][1] == max_priority:
            count += 1
            priorities.pop()
            # 해당 프로세스가 특정 프로세스(location)인 경우 → 정답 return
            if priorities_queue[0][0] == location:
                return count
            else:
                priorities_queue.popleft()
        # 실행될 차례인 프로세스의 우선순위보다 더 높은 우선순위의 프로세스가 있는 경우 → 실행 X
        else:
            priorities_queue.rotate(-1)
