def getData(path: str):
    lst = []
    input = open(path, 'r')
    for line in input.readlines():
        lst.append(line.strip().split(" "))
    input.close()
    return lst
