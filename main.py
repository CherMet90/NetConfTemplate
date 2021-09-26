from common.getData import getData
from common.createVlan import createVlan

lst = getData("input/vlans.txt")
createVlan(lst, "output/resultCmdList.txt")
