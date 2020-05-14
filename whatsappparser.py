with open('chatdata\mushuchat2.txt', 'r') as f:
    for line in f:
        print(line[line.index(': ') + 2:])
