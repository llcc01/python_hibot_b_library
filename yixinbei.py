from time import sleep
import random

from driver import HibotDriver
from action import HandAction
from send_type import EleType, ClassicType, LightType, MotorPType


last_look = 0


def look(hibot: HibotDriver, loc: int, speed: float = 2):
    t = int(abs(loc - last_look) / speed)
    hibot.serial_send(MotorPType.stepMpToEndLoc(0x010B, loc, t, 0))
    hibot.serial_send(ClassicType.endOrder())
    sleep(t / 1000 + 0.3)


BLINK_LIST = [[5], [6, 4], [7, 3], [0, 2], [1]]


# 眨眼
def blink(hibot: HibotDriver, r, g, b):
    hibot.serial_send(LightType.eyeCTSingleColor(2, r, g, b))
    hibot.serial_send(ClassicType.endOrder())


def set_head_light(hibot: HibotDriver, r, g, b):
    hibot.serial_send(LightType.topHeadControll(0, r, g, b))
    hibot.serial_send(ClassicType.endOrder())


def run(hibot: HibotDriver):
    # hibot.do_action(HandAction.waving)
    # hibot.do_action(HandAction.point_look)
    # hibot.serial_send(ClassicType.runWithSpeed(15, -15, 15))
    # hibot.serial_send(ClassicType.endOrder())
    # hibot.do_action(HandAction.please)
    # sleep(2)

    # hibot.serial_send(ClassicType.runWithSpeed(-15, 15, 15))
    # hibot.serial_send(ClassicType.endOrder())
    # sleep(2)

    # look random
    # look(hibot, 0)
    # for _ in range(10):
    #     look(hibot, random.randint(-6000, 6000), 1)
    #     sleep(0.5)
    #     set_head_light(hibot, 0xff, 0, 0)
    #     sleep(1)
    #     for _ in range(3):
    #         blink(hibot, 0, 0, 0xFF)
    #         sleep(1)
    #     set_head_light(hibot, 0xff, 0xff, 0xFF)
    #     hibot.serial_send(ClassicType.endOrder())
    #     sleep(2)

    for _ in range(10):
        hibot.do_action(HandAction.speakActionLeftUp)
        sleep(0.3)
        hibot.do_action(HandAction.speakActionRightUp)
        sleep(0.3)
        hibot.do_action(HandAction.stepToSpeachBaseAction)
        sleep(0.3)
        hibot.do_action(HandAction.please)
        sleep(0.3)
        hibot.do_action(HandAction.stepToSpeachBaseAction)
        sleep(1)

