def getVlan(path: str):
    lst = []
    input = open(path, 'r')
    for line in input.readlines():
        lst.append(line.strip().split(" "))
    input.close()
    return lst


def createVlan(vlans: list, pathout: str):
    cmdCreateVl = ["create vlan ", " tag "]
    cmdConfVl = ["config vlan ", " add tagged "]
    output = open(pathout, 'w')
    for vlan in vlans:
        output.write(cmdCreateVl[0] + vlan[0] + cmdCreateVl[1] + vlan[1] + "\n")
        output.write(cmdConfVl[0] + vlan[0] + cmdConfVl[1] + vlan[2] + "\n")
    output.close()


lst = getVlan("vlans.txt")
createVlan(lst, "resultCmdList.txt")
print(lst)
