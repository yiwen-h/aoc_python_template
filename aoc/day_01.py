from load_data import get_data

def part_1(data):
    data_split = data.split('\n')
    increases = 0
    for i in range(len(data_split)):
        if i > 0 and data_split[i] != '':
            if data_split[i] > data_split[i-1]:
                increases += 1
    return increases

raw_data = get_data(1)
print(f'part 1 solution = {part_1(raw_data)}')

def part_2(data):
    pass


