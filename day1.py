
col1 = []
col2 = []

with open('day1_input.txt', 'r') as input_file:
    for line in input_file.readlines():
        # print(line.strip())
        values = line.split()
        col1.append(int(values[0].strip()))
        col2.append(int(values[1].strip()))

col1.sort()
col2.sort()

sum_abs = 0
for i in range(len(col1)):
    sum_abs += abs(col1[i] - col2[i])
print(f'sum_abs: {sum_abs}')

# similarity score
score = 0
for val in col1:
    count = col2.count(val)
    score += val * count
print(f'similarity score: {score}')
