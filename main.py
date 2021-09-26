import getData
import createVlan

lst = getData.getData("input/vlans.txt")
createVlan.createVlan(lst, "output/resultCmdList.txt")
