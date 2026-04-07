from pybricks.parameters import Button, Direction, Port
from pybricks.pupdevices import Motor, Remote
from pybricks.robotics import Car
from pybricks.tools import wait

driveFront = Motor(Port.A, Direction.COUNTERCLOCKWISE)
driveRear = Motor(Port.B, Direction.COUNTERCLOCKWISE)
steering = Motor(Port.C, Direction.COUNTERCLOCKWISE)

car = Car(steering, (driveFront, driveRear), 100)
remote = Remote(timeout=None)

STEER_INCREMENT = 10
DRIVE_INCREMENT = 10

iDrive = 0
iSteer = 0

def quarterTurn(steerAngle, driveSpeed, timeToRun, direction):
   car.steer(steerAngle * direction)
   car.drive_power(driveSpeed * direction)
   wait(timeToRun)   

   car.drive_power(0)
   wait(700)

def turnAround():
   steerAngle = 100
   driveSpeed = 100
   timeToRun = 1000

   quarterTurn(steerAngle, driveSpeed, timeToRun, 1)
   quarterTurn(steerAngle, driveSpeed, timeToRun, -1)
   quarterTurn(steerAngle, driveSpeed, timeToRun, 1)
   quarterTurn(steerAngle, driveSpeed, timeToRun, -1)

   car.steer(0)

   wait(1000)

def jiggle():
   car.steer(500)
   wait(800)
   car.steer(-500)
   wait(800)
   car.steer(0)

   wait(400)

   car.drive_power(100)
   wait(300)
   car.drive_power(-100)
   wait(300)
   car.drive_power(0)

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

