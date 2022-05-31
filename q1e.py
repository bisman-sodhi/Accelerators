import numpy as np
import matplotlib.pyplot as plt 

# Question 1 E 

vFinal = 1.0
vInit = 1.3
vThresh = 0.9
vStat = 5
interval = 0.01

powerInit = 50

parallelTimePrecent = 0.95
serialTimePercent = 0.5
timeOrig = 2

vList = np.arange(vInit, vFinal, -interval)


energyList = []
delayList = []
coreList = []

energySerial = 5.5


def frequencyRatio(f):
    f_ = ( (pow( (1.3 - 0.9), 2 ))/(1.3) )
    return ( (pow( f- 0.9, 2 )/f ) / f_   )


for vItem in vList:
    # freq ratio
    freq = frequencyRatio(vItem)

    # parallel power
    powerNew = pow(vItem,2) * freq * powerInit + vStat

    # time 
    time1  = 2/freq
    timeNew = (parallelTimePrecent)*time1
    float("{:.2f}".format(timeNew))
    delayList.append(timeNew/10)

    # number of cores 
    coreList.append(timeNew/0.2)
    
    # energy
    energyNew = powerNew * timeNew
    energyTotal = energyNew + energySerial
    float("{:.2f}".format(energyTotal))
    energyTotal = energyList.append(energyTotal)
    


ans = min(d for d in delayList if d <= 0.2)
print("Least amount of energy required ", energyList[delayList.index(ans)])
print("Minimum number of cores needed ", coreList[delayList.index(ans)]) 
print("Energy list ", len(energyList), "\n", energyList)
print("Time list ", len(delayList), "\n", delayList)
print("Core List", len(coreList), "\n", coreList)

plt.figure(1)
plt.plot(delayList, energyList)
plt.title("Energy versus Time plot for Question 1E")
plt.xlabel("Time, s")
plt.ylabel("Energy, J")
plt.show() 

