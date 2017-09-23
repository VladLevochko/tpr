if __name__ == '__main__':
    file = open('data_for_lab1.txt', 'r')
    lines = file.readlines()
    file.close()
    file = open('data_for_lab1.txt', 'w')
    print(lines)
    for line in lines:
        file.write(line[:(len(line) - 1)] + ' ')
    file.close()
