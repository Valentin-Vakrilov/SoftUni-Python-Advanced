from collections import deque

number_of_pumps = int(input())

original_queue = deque()

rotated_queue = deque()

for pump in range(number_of_pumps):
    current_pump = [int(x) for x in input().split()]
    original_queue.append(current_pump)
    rotated_queue.append(current_pump)

total_petrol = 0
stops_counter = 0

while rotated_queue:
    if stops_counter == len(rotated_queue):
        start = rotated_queue[0]
        start_position = original_queue.index(start)
        print(start_position)
        break

    for petrol_pump in range(number_of_pumps):
        petrol = rotated_queue[petrol_pump][0]
        distance = rotated_queue[petrol_pump][1]
        total_petrol += int(petrol)
        if total_petrol >= int(distance):
            total_petrol -= int(distance)
            stops_counter += 1
        else:
            rotated_queue.append(rotated_queue.popleft())
            total_petrol = 0
            stops_counter = 0
            break
