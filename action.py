from time import sleep

from driver import HibotDriver
from send_type import MotorPType


class HandAction:
    @staticmethod
    def allStepToZero(d: HibotDriver):
        bytesHA1 = MotorPType.stepMpZero(0x010A, 4000)
        bytesHB1 = MotorPType.stepMpZero(0x010B, 4000)
        bytesL01 = MotorPType.stepMpZero(0x0100, 5000)
        bytesL11 = MotorPType.stepMpZero(0x0101, 3000)
        bytesL21 = MotorPType.stepMpZero(0x0102, 7000)
        bytesL31 = MotorPType.stepMpZero(0x0103, 5000)
        bytesR51 = MotorPType.stepMpZero(0x0105, 5000)
        bytesR61 = MotorPType.stepMpZero(0x0106, 3000)
        bytesR71 = MotorPType.stepMpZero(0x0107, 7000)
        bytesR81 = MotorPType.stepMpZero(0x0108, 5000)
        bytesL01 = MotorPType.stepMpToEndLoc(0x0100, -2500, 2000, 0)
        bytesL21 = MotorPType.stepMpToEndLoc(0x0102, 3000, 2000, 0)
        bytesR51 = MotorPType.stepMpToEndLoc(0x0105, 2500, 2000, 0)
        bytesR71 = MotorPType.stepMpToEndLoc(0x0107, -3000, 2000, 0)

        d.serial_send(bytesHA1+bytesHB1+bytesL01+bytesL11 +
                           bytesL21+bytesL31+bytesR51+bytesR61+bytesR71+bytesR81)

    @staticmethod
    def zhaoshouNow(d: HibotDriver):
        # 左臂
        bytesl = MotorPType.stepMpToEndLoc(0x0100, -7000, 1400, 0)
        bytesl1 = MotorPType.stepMpToEndLoc(0x0101, -2000, 400, 0)
        bytes2l = MotorPType.stepMpToEndLoc(0x0103, -5000, 1000, 0)
        d.serial_send(bytesl+bytesl1+bytes2l)
        sleep(1.8)

        bytes31 = MotorPType.stepMpToEndLoc(0x0102, 8000, 1000, 0)
        d.serial_send(bytes31)
        sleep(1.1)

        bytes32 = MotorPType.stepMpToEndLoc(0x0102, 0, 1000, 0)
        d.serial_send(bytes32)
        sleep(1.1)

        bytes33 = MotorPType.stepMpToEndLoc(0x0102, 8000, 1000, 1)
        d.serial_send(bytes33)
        sleep(1.1)

        bytes34 = MotorPType.stepMpZero(0x0102, 8000)
        d.serial_send(bytes34)
        sleep(1.1)

        HandAction.allStepToZero()
        sleep(1.9)
