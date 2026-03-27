from pybricks.pupdevices import Remote, Motor
from pybricks.parameters import Port, Button
from pybricks.tools import wait

from pybricks.pupdevices import Remote, Motor
from pybricks.parameters import Port, Button
from pybricks.tools import wait

rem = Remote()
mFront = Motor(Port.A) # front wheels
mRear = Motor(Port.B) # rear wheels
mSteer = Motor(Port.C) # steering

sDrive = 0
sSteer = 0

while True:
    pressed = rem.buttons.pressed()

    if Button.LEFT in pressed:
        sSteer = 0
    elif Button.LEFT_PLUS in pressed:
        sSteer += 10
    elif Button.LEFT_MINUS in pressed:
        sSteer -= 10

    if Button.RIGHT in pressed:
        sDrive = 0        
    elif Button.RIGHT_PLUS in pressed:
        sDrive -= 100 # motor turns anti-clockwise for the car to go forward
    elif Button.RIGHT_MINUS in pressed:
        sDrive += 100        

    mFront.run(sDrive)
    mRear.run(sDrive)
    mSteer.run(sSteer)

    wait(100)
