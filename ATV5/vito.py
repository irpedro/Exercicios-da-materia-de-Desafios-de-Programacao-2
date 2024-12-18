def sum_houses(houses):
    total = 0
    for i in range(1, len(houses)):
        total += houses[i]
    return find_best_house(houses, total)

def find_best_house(houses, total):
    temp = 0
    best_house = 0
    best_sum = 0

    for i in range(1, houses[len(houses)-1]):
        temp = total-i*houses[0]
        if temp < 0:
            temp *= -1
        if temp<best_sum or i == 1:
            best_sum = temp
            best_house = i

    return find_best_distance(houses, best_house)

def find_best_distance(houses, best_house):
    temp = 0
    distance = 0
    for i in range(1, len(houses)):
        temp = houses[i]-best_house
        if temp < 0:
            temp *= -1
        distance += temp
    return distance

times = int(input())
for i in range(times):

    houses = list(map(int, input().split()))
    print(sum_houses(houses))