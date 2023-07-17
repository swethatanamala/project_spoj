def can_reorder(n, trucks):
    status = True
    need = 1
    lane = []
    for truck in trucks:
        while (len(lane) > 0) and (lane[-1] == need):
            lane.pop()
            need += 1
        if truck == need:
            need += 1
        elif (len(lane) > 0) and (truck > lane[-1]):
            status = False
            return status
        else:
            lane.append(truck)
    return status

while True:
    num = int(input())
    if num == 0:
        break
    order = []
    input_str = input()
    order = [int(x) for x in input_str.split()]
    status = can_reorder(num, order)
    if status:
        print("yes")
    else:
        print("no")
    