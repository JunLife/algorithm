from collections import deque

# 다리 위 최대 트럭 수 (1초에 1칸 전진), 다리가 버티는 최대 무게, 트럭들 무게, 순서는 못바꿈
def solution(bridge_length, weight, truck_weights):
    answer = 0
    left_trucks = deque(truck_weights)
    on_bridge_truck_time = deque()
    on_bridge = deque()
    
    while left_trucks:
        if sum(on_bridge) + left_trucks[0] <= weight:
            next_truck = left_trucks.popleft()
            on_bridge.append(next_truck)
            on_bridge_truck_time.append(1)
        for i in range(len(on_bridge)):
            on_bridge_truck_time[i] += 1
        if on_bridge_truck_time[0] > bridge_length:
            on_bridge.popleft()
            on_bridge_truck_time.popleft()
        answer += 1

    while on_bridge:
        for i in range(len(on_bridge)):
            on_bridge_truck_time[i] += 1
        
        if on_bridge_truck_time[0] > bridge_length:
            on_bridge.popleft()
            on_bridge_truck_time.popleft()
        answer += 1
    return answer + 1