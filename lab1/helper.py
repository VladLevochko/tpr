if __name__ == '__main__':
    path = '/home/vlad/PycharmProjects/tpr_labs/lab1/data_for_lab3.txt'
    file = open(path, 'r')
    lines = file.readlines()
    file.close()
    file = open(path, 'w')
    print(lines)
    for line in lines:
        file.write(line[:(len(line) - 1)] + ' ')
    file.close()
