from MotorWrapper import Motor
from MoveRobotWrapper import MoveRobot
from ConveyorBeltWrapper import ConveyorBelt

class test():
    def assertTrue(self, argument):
        if argument:
            print('Test ok')
        else:
            print ('Test failed')

myTest=test()
testMyMotor=Motor(200,5)
testMyMoveRobot=MoveRobot()
testMyConveyorBelt= ConveyorBelt()

class testMotor():
    def testDriveForward(self):
        print('***testMotor::testDriveForward***')
        distance = 20
        testMyMotor.drive(distance)
        myTest.assertTrue(testMyMotor.getDistance()==distance)
    def testDriveBackward(self):
        print('***testMotor::testDriveBackward***')
        distance = -20
        testMyMotor.drive(distance)
        myTest.assertTrue(testMyMotor.getDistance()==distance)
    def testStop(self):
        print('***testMotor::testStop***')
        testMyMotor.stop()
        myTest.assertTrue(testMyMotor.getDistance()==0)

class testMoveRobot():
    def testDriveForward(self):
        print('***testMoveRobot::testDriveForward***')
        distance = 20
        testMyMoveRobot.drive(distance)
        myTest.assertTrue(testMyMoveRobot.getDistance()==distance)
    def testDriveBackward(self):
        print('***testMoveRobot::testDriveBackward***')
        distance = -20
        testMyMoveRobot.drive(distance)
        myTest.assertTrue(testMyMoveRobot.getDistance()== distance)
    def testTurn(self):
        print('***testMoveRobot::testTurn***')
        angle = 90
        testMyMoveRobot.turn(angle)
        myTest.assertTrue(testMyMoveRobot.getAngle()== angle)

class testConveyorBelt():
    def testDriveForward(self):
        print('***testConveyorBelt::testDriveForward***')
        testMyConveyorBelt.driveForward()
        myTest.assertTrue(testMyConveyorBelt.getDistance()>0)
    def testDriveBackward(self):
        print('***testConveyorBelt::testDriveBackward***')
        testMyConveyorBelt.driveBackward()
        myTest.assertTrue(testMyConveyorBelt.getDistance()<0)
    def testStop(self):
        print('***testConveyorBelt::testStop***')
        testMyConveyorBelt.stop()
        myTest.assertTrue(testMyConveyorBelt.getDistance()==0)

#Motor testen:
testMotor = testMotor()
testMotor.testDriveForward()
testMotor.testDriveBackward()
testMotor.testStop()

#MoveRobot testen:
testMoveRobot = testMoveRobot()
testMoveRobot.testDriveForward()
testMoveRobot.testDriveBackward()
testMoveRobot.testTurn()

#ConveyorBelt:
testConveyorBelt = testConveyorBelt()
testConveyorBelt.testDriveForward()
testConveyorBelt.testDriveBackward()
testConveyorBelt.testStop()