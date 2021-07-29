# Heat Transfer

import numpy # Numerical in python
from matplotlib import pyplot

T1 = 350
T2 = 325
x1 = 0.02
x2 = 0.035
k_Copper = 400
k_Aluminum = 250 

#for i in range(100)

D = numpy.arange(0.01, 0.11, 0.01)
A = (numpy.pi * D **2)/4

Q_Cop = (2 * k_Copper * A * (T1 - T2))/(x2 - x1)
Q_Alum = (2 * k_Aluminum * A * (T1 - T2))/(x2 - x1)

pyplot.plot(D, Q_Cop, label = "k_Copper", color = "r", marker = "*", linestyle = "-" )
pyplot.plot(D, Q_Alum, label = "k_Aluminum", color = "g", marker = "o", linestyle = "--" )
pyplot.xlabel("D (m) ", fontsize = 12)
pyplot.ylabel("Q (W)", fontsize = 12)
pyplot.legend(fontsize = 10)
pyplot.title("Heat Transfer", fontsize = 11)
pyplot.xlim(xmin = 0, xmax = 0.10)
pyplot.ylim(ymin = 0)
pyplot.grid()
pyplot.show()

#pyplot.figure("Heat")
#pyplot.savefig("Heat.png")

