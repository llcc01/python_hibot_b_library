from time import sleep
import os

# dotenv
from dotenv import load_dotenv
from driver import HibotDriver
from action import HandAction
from send_type import EleType, ClassicType, LightType, MotorPType


import webapi


load_dotenv()

if __name__ == "__main__":
    

    hibot = HibotDriver(os.environ.get("HIBOT_PORT", "COM3"), 1152000)

    # for i in range(5):
    #     hibot.serial_send(EleType.getBatteryData())
    #     hibot.serial_send(ClassicType.getClassicData())
    #     hibot.serial_send(ClassicType.endOrder())
    #     sleep(1)

    hibot.serial_send(EleType.onPower())
    hibot.serial_send(ClassicType.endOrder())
    sleep(0.1)

    hibot.serial_send(EleType.getBatteryData())
    hibot.serial_send(ClassicType.getClassicData())
    hibot.serial_send(ClassicType.getFwVersion())
    hibot.serial_send(MotorPType.stepMpStatus(0x010A))
    hibot.serial_send(MotorPType.stepMpStatus(0x010B))
    hibot.serial_send(MotorPType.stepMpStatus(0x0100))
    hibot.serial_send(MotorPType.stepMpStatus(0x0101))
    hibot.serial_send(MotorPType.stepMpStatus(0x0102))
    hibot.serial_send(MotorPType.stepMpStatus(0x0103))
    hibot.serial_send(MotorPType.stepMpStatus(0x0104))
    hibot.serial_send(MotorPType.stepMpStatus(0x0105))
    hibot.serial_send(MotorPType.stepMpStatus(0x0106))
    hibot.serial_send(MotorPType.stepMpStatus(0x0107))
    hibot.serial_send(MotorPType.stepMpStatus(0x0108))
    hibot.serial_send(MotorPType.stepMpStatus(0x0109))
    hibot.serial_send(ClassicType.endOrder())

    hibot.do_action(HandAction.allStepToZero)

    hibot.serial_send(LightType.eyeCTSingleColor(0, 0, 0, 0xFF))
    hibot.serial_send(LightType.topHeadControll(0, 0, 0, 0xFF))
    hibot.serial_send(ClassicType.endOrder())

    sleep(2)

    webapi.init(hibot)

    # yixinbei.run(hibot)

    # hibot.do_action(HandAction.allStepToZero)


    # while True:
    #     hibot.do_action(HandAction.handSeeYouNow)
    #     hibot.serial_send(ClassicType.endOrder())
    #     sleep(0.5)
    #     # hibot.serial_send(ClassicType.runWithSpeed(15, -15, 15))
    #     # hibot.serial_send(ClassicType.endOrder())
    #     # sleep(0.5)
    #     hibot.do_action(HandAction.zhaoshouNow)
    #     hibot.serial_send(ClassicType.endOrder())
    #     sleep(0.5)
    #     # hibot.serial_send(ClassicType.runWithSpeed(-15, 15, 15))
    #     # hibot.serial_send(ClassicType.endOrder())
    #     # sleep(0.5)

    #     sleep(5)


    # while True:
    #     dat = hibot.ser.read(1000)
    #     if dat:
    #         print(dat.hex().replace('acbd','acbd\n'),end='')
    #     else:
    #         print('----')
