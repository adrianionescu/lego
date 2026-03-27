from pybricks.parameters import Button, Direction, Port
from pybricks.pupdevices import Motor, Remote
from pybricks.robotics import Car
from pybricks.tools import wait

# Set up all devices.
driveFront = Motor(Port.A, Direction.COUNTERCLOCKWISE)
driveRear = Motor(Port.B, Direction.COUNTERCLOCKWISE)
steering = Motor(Port.C, Direction.COUNTERCLOCKWISE)

drive = (driveFront, driveRear)
car = Car(steering, drive)
remote = Remote(timeout=None)

STEER_INCREMENT = 10
DRIVE_INCREMENT = 10

iDrive = 0
iSteer = 0

def turnAround():
    steerIncrement = 100
    driveIncrement = 100

    car.steer(steerIncrement)
    car.drive_power(driveIncrement)
    
    car.steer(-steerIncrement)
    car.drive_power(-driveIncrement)

    car.drive_power(driveIncrement)
    car.drive_power(driveIncrement)
    car.drive_power(driveIncrement)
    car.drive_power(driveIncrement)


def jiggle():
    print("Hello from jiggle")

# The main program starts here.
while True:    
    pressed = remote.buttons.pressed()

    if Button.LEFT in pressed:
        turnAround()
    elif Button.LEFT_PLUS in pressed:
        iSteer += STEER_INCREMENT
    elif Button.LEFT_MINUS in pressed:
        iSteer -= STEER_INCREMENT
    else:
        iSteer = 0
    
    if Button.RIGHT in pressed:
        jiggle()
    elif Button.RIGHT_PLUS in pressed:
        iDrive += DRIVE_INCREMENT
    elif Button.RIGHT_MINUS in pressed:
        iDrive -= DRIVE_INCREMENT
    else:
        iDrive = 0

    car.steer(iSteer)
    car.drive_power(iDrive)

    wait(50)
