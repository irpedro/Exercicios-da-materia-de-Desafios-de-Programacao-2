def LIS(elephants):

    elephants.sort(key=lambda x: (x[0], -x[1]))
    
    eleph_size = len(elephants)
    eleph_list = [1] * eleph_size
    last = [-1] * eleph_size
    
    #O(n²)
    for weight_count in range(eleph_size):
        for iq_count in range(weight_count):
            if elephants[weight_count][0] > elephants[iq_count][0] and elephants[weight_count][1] < elephants[iq_count][1]:
                if eleph_list[weight_count] < eleph_list[iq_count] + 1:
                    eleph_list[weight_count] = eleph_list[iq_count] + 1
                    last[weight_count] = iq_count

    max_len = max(eleph_list)
    last_index = eleph_list.index(max_len)

    end_sequence = []
    while last_index != -1:
        end_sequence.append(elephants[last_index][2])
        last_index = last[last_index]
    
    end_sequence.reverse()
    print(max_len)
    for ele in end_sequence:
        print(ele + 1)

if __name__ == "__main__":
    data = []
    while True:
        try:
            inp = input()
        except EOFError:
            break
        data.append(inp)

    elephants = []
    for i, line in enumerate(data):
        weight, iq = map(int, line.split())
        elephants.append((weight, iq, i))
    
    LIS(elephants)