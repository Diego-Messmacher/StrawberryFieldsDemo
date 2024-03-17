import strawberryfields as sf
from strawberryfields.ops import *
from math import *

prog = sf.Program(1)

with prog.context as q:
    Rgate(pi / 2) | q[0]
    Dgate(sqrt(2) - 1) | q[0]
    Rgate(pi / 2) | q[0]
    MeasureFock() | q[0]
numshots = 1000
eng = sf.Engine("gaussian")
result = eng.run(prog, shots=numshots)

calcdiff = 0
# print(result.samples)
for i in range(numshots):
    if result.samples[i][0] == 0:
        calcdiff -= 1
    elif result.samples[i][0] == 1:
        calcdiff += 1
    else:
        print("unexpected output: " + str(result.samples[i][0]))

if calcdiff > 0:
    print("there were " + str(calcdiff) + " more 1s than 0s")
elif calcdiff < 0:
    print("there were " + str(abs(calcdiff)) + " more 0s than 1s")
else:
    print("same amount of 0s and 1s")
