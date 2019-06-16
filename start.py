import math
import stepper
import threading
DIR_M1 = 5       # Direction GPIO Pin
STEP_M1 = 6      # Step GPIO Pin
DIR_M2 = 13       # Direction GPIO Pin
STEP_M2 = 19      # Step GPIO Pin

def square(x):
    return x*x
d = float(input('D value: '))
r = float(input('R value: '))
L1 = (5 * d)/(2 * math.pi * r)
L2 = (math.sqrt(50) * d)/(2 * math.pi * r)
N1 = ((6 - L1) * d)/(2 * math.pi * r)
N2 = ((6 - L2) * d)/(2 * math.pi * r)
while True: 
    x = float(input('X value: '))
    y = float(input('Y value: '))
    l1 = math.sqrt(square(x) + square(y-5))
    l2 = math.sqrt(square(5-x) + square(y-5))
    n1 = ((6 - l1) * d)/(2 * math.pi * r)
    n2 = ((6 - l2) * d)/(2 * math.pi * r)
    n1_diff = N1-n1
    n2_diff = N2-n2
    m1_dir = True
    m2_dir = True
    if N1-n1>0 :
        t1 = threading.Thread(target=stepper.clockwise, args=(n1_diff, DIR_M1, STEP_M1, ))
        t1.start()
    else: 
        t1 = threading.Thread(target=stepper.counterclockwise, args=(n1_diff, DIR_M1, STEP_M1, ))
        m1_dir = False
        t1.start()
    if N2-n2>0 :
        t2 = threading.Thread(target=stepper.clockwise, args=(n2_diff, DIR_M2, STEP_M2, ))
        t2.start()
    else: 
        t2 = threading.Thread(target=stepper.counterclockwise, args=(n2_diff, DIR_M2, STEP_M2, ))
        m2_dir = False
        t2.start()
    t1.join()
    t2.join()
    time.sleep(8)
    if(m1_dir) :
        t1 = threading.Thread(target=stepper.counterclockwise, args=(n1_diff, DIR_M1, STEP_M1, ))
        t1.start()
    else:
        t1 = threading.Thread(target=stepper.clockwise, args=(n1_diff, DIR_M1, STEP_M1, ))
        t1.start()
    if(m2_dir) :
        t2 = threading.Thread(target=stepper.counterclockwise, args=(n2_diff, DIR_M1, STEP_M1, ))
        t2.start()
    else:
        t2 = threading.Thread(target=stepper.clockwise, args=(n2_diff, DIR_M1, STEP_M1, ))
        t2.start()
    time.sleep(8)


