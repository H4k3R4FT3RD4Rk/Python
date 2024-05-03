with open('numbers.txt', 'w') as file:
    for number in range(1000000, 100000000):
        file.write(str(number) + '\n')
