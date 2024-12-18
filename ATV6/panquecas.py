from sys import stdin

def sort_pancakes(pancakes):
    last = pancakes[0]
    end = test_end(pancakes)
    if end:
        print('0', end=' ')
        exit()
    for i in range(1, len(pancakes)):
        if pancakes[i] > last:
            pancakes = flip_pancakes(pancakes, i-1)
            sort_pancakes(pancakes)
        else:
            last = pancakes[i]
    if end != True:
        print('1 0', end=' ')
    return

def flip_pancakes(pancakes, i):
    new_pancakes = []
    if i == 1:
        print(i,  end=' ')
        for j in range(len(pancakes)-i, -1, -1):
            new_pancakes.append(pancakes[j])
        for j in range(len(pancakes)-i+1, len(pancakes)):
            new_pancakes.append(pancakes[j])
    else:
        print(i-1,  end=' ')
        for j in range(i, -1, -1):
            new_pancakes.append(pancakes[j])
        for j in range(len(pancakes)-i+2, len(pancakes)):
            new_pancakes.append(pancakes[j])
        
    return new_pancakes

def test_end(pancakes):
    for i in range(1, len(pancakes)):
        if pancakes[i] < pancakes[i-1]:
            return False
    return True

# Main code
i=0
while i != 3:
    pancakes = list(map(int, input().split()))
    sort_pancakes(pancakes)
    i += 1

