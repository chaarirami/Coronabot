from Motor import Motor

stepper = Motor(200,2)
print(stepper.rpm)
stepper.setSpeed(10)
print(stepper.rpm)
stepper.drive(10)
