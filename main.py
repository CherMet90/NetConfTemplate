def getVlan(path: str):
    lst = []
    input = open(path, 'r')
    for line in input.readlines():
        lst.append(line.strip().split(" "))
    input.close()
    return lst


def createVlan(vlans: list, pathout: str):
    output = open(pathout, 'w')
    for vlan in vlans:
        output.write("create vlan " + vlan[0] + " tag " + vlan[1] + "\n")
        output.write("config vlan " + vlan[0] + " add tagged " + vlan[2] + "\n")
    output.close()


lst = getVlan("input/vlans.txt")
createVlan(lst, "output/resultCmdList.txt")
print(lst)
