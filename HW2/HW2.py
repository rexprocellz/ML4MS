import numpy as np
import math
import cmath
import matplotlib.pyplot as plt

CONST = 25

xList = np.linspace(-1*math.pi, math.pi, CONST)
yList = xList
fList = []
fConList = []
matrixList = []
eigenValList = []
eigenVecList = []

######################################
##### 1. Matrix Diagonalization ######
######################################

for x in xList:
    for y in yList:
        f = cmath.exp(complex(0,y)) + 2*cmath.exp(complex(0,(-0.5*y)))*math.cos((math.sqrt(3)/2)*x)
        fList.append(f)
        fCon = np.conj(f)
        fConList.append(fCon)

for i in range(0, len(fList), 1) :
    matrix = np.array([[0, fList[i]], [fConList[i], 0]])
    matrixList.append(matrix)

for matrix in matrixList:
    eigenVal, eigenVec = np.linalg.eig(matrix)
    eigenValList.append(eigenVal)
    eigenVecList.append(eigenVec)

######################################
###### 2. Eigenvalues Plotting #######
######################################

realFirstEigenValList = []
realSecondEigenValList = []
imagFirstEigenValList = []
imagSecondEigenValList = []

for eigenVal in eigenValList:
    realFirstEigenValList.append(eigenVal[0].real)
    realSecondEigenValList.append(eigenVal[1].real)
    imagFirstEigenValList.append(eigenVal[0].imag)
    imagSecondEigenValList.append(eigenVal[1].imag)

realFirstEigenValArray = np.array(realFirstEigenValList).reshape(CONST,CONST)
realSecondEigenValArray = np.array(realSecondEigenValList).reshape(CONST,CONST)
imagFirstEigenValArray =np.array(imagFirstEigenValList).reshape(CONST,CONST)
imagSecondEigenValArray = np.array(imagSecondEigenValList).reshape(CONST,CONST)
X, Y = np.meshgrid(xList, yList)

fig = plt.figure()
ax1 = fig.add_subplot(121,projection='3d')
realFirstPlot = ax1.plot_surface(X, Y, realFirstEigenValArray, cmap='Purples', alpha=1,
                        rstride=1, cstride=1, linewidth=1, antialiased=True)
realSecondPlot = ax1.plot_surface(X, Y, realSecondEigenValArray,cmap='Purples', alpha=1,
                        rstride=1, cstride=1, linewidth=1, antialiased=True)

ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_zlabel("Real", rotation=90)

ax2=fig.add_subplot(122,projection='3d')
imagFirstPlot = ax2.plot_surface(X, Y, imagFirstEigenValArray, cmap='Purples', alpha=1,
                        rstride=1, cstride=1, linewidth=1, antialiased=True)
imagSecondPlot = ax2.plot_surface(X, Y, imagSecondEigenValArray, cmap='Purples', alpha=1,
                        rstride=1, cstride=1, linewidth=1, antialiased=True)

ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_zlabel("Imag", rotation=90)

plt.tight_layout()
plt.show()

