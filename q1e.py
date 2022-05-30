import numpy as np
import matplotlib.pyplot as plt 

# Question 1 E 

vFinal = 1.0
vInit = 1.3
vThresh = 0.9
vStat = 5
interval = 0.001

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
    delayList.append(timeNew)

    # number of cores 
    coreList.append(timeNew/0.2)
    
    # energy
    energyNew = powerNew * timeNew
    energyTotal = energyNew + energySerial
    float("{:.2f}".format(energyTotal))
    energyTotal = energyList.append(energyTotal)
    

print("Least amount of energy required ",min(energyList)) #151.7
print("Minimum number of cores needed ", coreList[energyList.index(min(energyList))]) #27

plt.figure()
plt.plot(delayList, energyList, marker='o')
plt.title("Energy versus Time plot for Question 1E")
plt.xlabel("Time, s")
plt.ylabel("Energy, J")
plt.show() 

 
