# Hardware Test 3
# author: Rami Chaari
# -90 Grad im Uhrzeigersinn drehen

from MoveRobot import MoveRobot

bot = MoveRobot()
bot.setSpeed(200)
bot.turn(-90)
