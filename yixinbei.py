from time import sleep
import random
import threading

from driver import HibotDriver
from action import HandAction
from send_type import EleType, ClassicType, LightType, MotorPType

last_look = 0

def look(hibot: HibotDriver, loc: int, speed: float = 2):
    global last_look
    t = int(abs(loc - last_look) / speed)
    hibot.lock()
    hibot.serial_send(MotorPType.stepMpToEndLoc(0x010B, loc, t, 0))
    hibot.serial_send(ClassicType.endOrder())
    hibot.unlock()
    sleep(t / 1000 + 0.3)
    last_look = loc


BLINK_LIST = [[5], [6, 4], [7, 3], [0, 2], [1]]


# 眨眼
def blink(hibot: HibotDriver, r, g, b):
    hibot.lock()
    hibot.serial_send(LightType.eyeCTSingleColor(2, r, g, b))
    hibot.serial_send(ClassicType.endOrder())
    hibot.unlock()


def set_head_light(hibot: HibotDriver, r, g, b):
    hibot.serial_send(LightType.topHeadControll(0, r, g, b))
    hibot.serial_send(ClassicType.endOrder())

look_random_running = False
look_random_thread = None

def look_random(hibot: HibotDriver):
    global look_random_running
    while look_random_running:
        look(hibot, random.randint(-6000, 6000), 1)
        sleep(1)

def look_random_start(hibot: HibotDriver):
    global look_random_running, look_random_thread
    if look_random_running:
        return
    look_random_running = True
    look_random_thread = threading.Thread(target=look_random, args=(hibot,))
    look_random_thread.start()

def look_random_stop(_):
    global look_random_running, look_random_thread
    if not look_random_running:
        return
    look_random_running = False
    look_random_thread.join()


dance_running = False
dance_thread = None

def dance(hibot: HibotDriver):
    global dance_running
    while dance_running:
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

def dance_start(hibot: HibotDriver):
    global dance_running, dance_thread
    if dance_running:
        return
    dance_running = True
    dance_thread = threading.Thread(target=dance, args=(hibot,))
    dance_thread.start()

def dance_stop(hibot: HibotDriver):
    global dance_running, dance_thread
    if not dance_running:
        return
    dance_running = False
    dance_thread.join()
    hibot.do_action(HandAction.allStepToZero)

def action1(hibot: HibotDriver):
    hibot.do_action(HandAction.waving)
    hibot.do_action(HandAction.point_look)
    hibot.serial_send(ClassicType.runWithSpeed(15, -15, 15))
    hibot.serial_send(ClassicType.endOrder())
    hibot.do_action(HandAction.please)
    sleep(2)

    hibot.serial_send(ClassicType.runWithSpeed(-15, 15, 15))
    hibot.serial_send(ClassicType.endOrder())
    sleep(2)

    hibot.do_action(HandAction.allStepToZero)

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

    for _ in range(3):
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

