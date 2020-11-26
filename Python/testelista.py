with open('dados', 'r') as f:
    results = [[str(entry) for entry in line.split(';')] for line in f.readlines()]

print(results[0][0])