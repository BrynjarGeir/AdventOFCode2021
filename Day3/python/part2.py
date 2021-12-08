def bit_counter(array, idx, mode):
    zeroes, ones = 0, 0
    for line in array:
        if line[idx] == "0":
            zeroes += 1
        if line[idx] == "1":
            ones += 1
    if mode == 'most':
        current_column = most(zeroes, ones)
    else: current_column = least(zeroes, ones)
    return current_column
    
def most(zeroes, ones):
    if ones >= zeroes: return '1'
    else: return '0'

def least(zeroes, ones):
    if ones >= zeroes: return '0'
    else: return '1'
 
def recursive_search(data, idx, mode):
    if len(data) == 1:
        return data[0]
    else:
        current_column = bit_counter(data, idx, mode)
        new_data = []
        for item in data:
            if item[idx] == current_column:
                new_data.append(item)
        idx += 1
        return recursive_search(new_data, idx, mode)

arr = []
with open("example", 'r+') as in_file:
    for line in in_file:
        arr.append(line.strip('\n'))       
print(int(recursive_search(arr,0, 'most'), 2) * int(recursive_search(arr,0, 'least'), 2))