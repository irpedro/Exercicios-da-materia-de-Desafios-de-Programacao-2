def count_ways_to_sum(value):

    times = [0] * (value + 1)
    
    times[0] = 1
    
    for i in range(1, value + 1):

        if i >= 1:
            times[i] += times[i - 1] * 2

        if i >= 2:
            times[i] += times[i - 2]

        if i >= 3:
            times[i] += times[i - 3]

    return times[value]

while True:
    inp = input()
    if inp == '':
        break
    value = int(inp)
    print(count_ways_to_sum(value))