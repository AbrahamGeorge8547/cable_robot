import math
import stepper
import threading

def square(x):
    return x*x
d = float(input('D value: '))
r = float(input('R value: '))
L1 = (5 * d)/(2 * math.pi * r)
L2 = (math.sqrt(50) * d)/(2 * math.pi * r)
N1 = ((6 - L1) * d)/(2 * math.pi * r)
N2 = ((6 - L2) * d)/(2 * math.pi * r)
while True: 
    x = int(input('X value: '))
    y = int(input('Y value: '))
    l1 = math.sqrt(square(x) + square(y-5))
    l2 = math.sqrt(square(5-x) + square(y-5))
    n1 = ((6 - l1) * d)/(2 * math.pi * r)
    n2 = ((6 - l2) * d)/(2 * math.pi * r)
    n1_diff = N1-n1
    n2_diff = N2-n2
    if N1-n1>0 :
        t1 = threading.Thread(target=stepper.clockwise, args=(n1_diff,))
        t1.start()
    else: 
        t1 = threading.Thread(target=stepper.counterclockwise, args=(n1_diff,))
        t1.start()
