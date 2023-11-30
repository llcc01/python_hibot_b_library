from time import sleep

from driver import HibotDriver
from send_type import MotorPType, ClassicType


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

        d.serial_send(
            bytesHA1
            + bytesHB1
            + bytesL01
            + bytesL11
            + bytesL21
            + bytesL31
            + bytesR51
            + bytesR61
            + bytesR71
            + bytesR81
        )

        d.serial_send(ClassicType.endOrder())

    @staticmethod
    def zhaoshouNow(d: HibotDriver):
        # 左臂
        bytesl = MotorPType.stepMpToEndLoc(0x0100, -7000, 1400, 0)
        bytesl1 = MotorPType.stepMpToEndLoc(0x0101, -2000, 400, 0)
        bytes2l = MotorPType.stepMpToEndLoc(0x0103, -5000, 1000, 0)
        d.serial_send(bytesl + bytesl1 + bytes2l)
        d.serial_send(ClassicType.endOrder())
        sleep(1.8)

        bytes31 = MotorPType.stepMpToEndLoc(0x0102, 8000, 1000, 0)
        d.serial_send(bytes31)
        d.serial_send(ClassicType.endOrder())
        sleep(1.1)

        bytes32 = MotorPType.stepMpToEndLoc(0x0102, 0, 1000, 0)
        d.serial_send(bytes32)
        d.serial_send(ClassicType.endOrder())
        sleep(1.1)

        bytes33 = MotorPType.stepMpToEndLoc(0x0102, 8000, 1000, 1)
        d.serial_send(bytes33)
        d.serial_send(ClassicType.endOrder())
        sleep(1.1)

        bytes34 = MotorPType.stepMpZero(0x0102, 8000)
        d.serial_send(bytes34)
        d.serial_send(ClassicType.endOrder())
        sleep(1.1)

        HandAction.allStepToZero(d)
        d.serial_send(ClassicType.endOrder())
        sleep(1.9)

    @staticmethod
    def handSeeYouNow(d: HibotDriver):
        bytes = MotorPType.stepMpToEndLoc(0x0105, 18000, 2600, 0)
        bytes1 = MotorPType.stepMpToEndLoc(0x0106, -2000, 400, 0)
        bytes2 = MotorPType.stepMpToEndLoc(0x0108, -7000, 1400, 0)
        bytes3 = MotorPType.stepMpZero(0x0107, 5000)
        d.serial_send(bytes + bytes1 + bytes2 + bytes3)
        d.serial_send(ClassicType.endOrder())
        sleep(2.8)

    @staticmethod
    def please(d: HibotDriver):
        bytes = MotorPType.stepMpToEndLoc(0x0105, 15000, 2000, 0)
        bytes1 = MotorPType.stepMpToEndLoc(0x0106, -3000, 800, 0)
        bytes2 = MotorPType.stepMpToEndLoc(0x0108, 7000, 1400, 0)
        bytes3 = MotorPType.stepMpZero(0x0107, 5000)
        bytes_head_h = MotorPType.stepMpToEndLoc(0x010B, -3000, 1000, 0)
        bytes_head_v = MotorPType.stepMpToEndLoc(0x010A, 1000, 1000, 0)
        d.serial_send(bytes + bytes1 + bytes2 + bytes3 + bytes_head_h + bytes_head_v)
        d.serial_send(ClassicType.endOrder())
        sleep(2.5)

        # HandAction.allStepToZero(d)
        # d.serial_send(ClassicType.endOrder())
        # sleep(2)

    @staticmethod
    def point_look(d: HibotDriver):
        bytes = MotorPType.stepMpToEndLoc(0x0105, 5000, 2000, 0)
        bytes1 = MotorPType.stepMpToEndLoc(0x0106, 1000, 400, 0)
        bytes3 = MotorPType.stepMpToEndLoc(0x0107, -7000, 1000, 0)
        bytes2 = MotorPType.stepMpToEndLoc(0x0108, 7000, 1400, 0)
        bytes_head_v = MotorPType.stepMpToEndLoc(0x010A, -4000, 1000, 0)
        d.serial_send(bytes + bytes1 + bytes2 + bytes3 + bytes_head_v)
        d.serial_send(ClassicType.endOrder())
        sleep(2.5)

        # HandAction.allStepToZero(d)
        # d.serial_send(ClassicType.endOrder())
        # sleep(2)

    @staticmethod
    def waving(d: HibotDriver):
        bytes = MotorPType.stepMpToEndLoc(0x0105, 22000, 3000, 0)
        bytes1 = MotorPType.stepMpToEndLoc(0x0106, -2000, 400, 0)
        bytes2 = MotorPType.stepMpToEndLoc(0x0108, -7000, 1400, 0)
        bytes3 = MotorPType.stepMpZero(0x0107, 5000)
        d.serial_send(bytes + bytes1 + bytes2 + bytes3)
        d.serial_send(ClassicType.endOrder())
        sleep(3.2)

        bytes31 = MotorPType.stepMpToEndLoc(0x0106, -5000, 500, 0)
        d.serial_send(bytes31)
        d.serial_send(ClassicType.endOrder())
        sleep(0.5)

        bytes32 = MotorPType.stepMpToEndLoc(0x0106, -500, 500, 0)
        d.serial_send(bytes32)
        d.serial_send(ClassicType.endOrder())
        sleep(1.5)

        bytes31 = MotorPType.stepMpToEndLoc(0x0106, -5000, 500, 0)
        d.serial_send(bytes31)
        d.serial_send(ClassicType.endOrder())
        sleep(1)

        bytes32 = MotorPType.stepMpToEndLoc(0x0106, -500, 500, 0)
        d.serial_send(bytes32)
        d.serial_send(ClassicType.endOrder())
        sleep(1.5)

        # HandAction.allStepToZero(d)
        # d.serial_send(ClassicType.endOrder())
        # sleep(2)

    # 演讲的时候基本动作
    @staticmethod
    def stepToSpeachBaseAction(d: HibotDriver):
        bytesHA1 = MotorPType.stepMpZero(0x010A, 4000)
        bytesHB1 = MotorPType.stepMpZero(0x010B, 4000)
        # 左臂
        bytesL01 = MotorPType.stepMpToEndLoc(0x0100, -4000, 800, 0)
        bytesL11 = MotorPType.stepMpZero(0x0101, 5000)
        bytesL21 = MotorPType.stepMpToEndLoc(0x0102, 8000, 800, 0)
        bytesL31 = MotorPType.stepMpToEndLoc(0x0103, -8000, 800, 0)
        # 右臂
        bytesR5 = MotorPType.stepMpToEndLoc(0x0105, 4000, 800, 0)
        bytesR6 = MotorPType.stepMpZero(0x0106, 5000)
        bytesR7 = MotorPType.stepMpToEndLoc(0x0107, -8000, 500, 0)
        bytesR8 = MotorPType.stepMpToEndLoc(0x0108, 8000, 800, 0)

        d.serial_send(
            bytesHA1
            + bytesHB1
            + bytesL01
            + bytesL11
            + bytesL21
            + bytesL31
            + bytesR5
            + bytesR6
            + bytesR7
            + bytesR8
        )

        d.serial_send(ClassicType.endOrder())
        sleep(2.5)

    # 演讲的左上右下
    @staticmethod
    def speakActionLeftUpRightDown(d: HibotDriver):
        # 左臂
        bytesL0 = MotorPType.stepMpToEndLoc(0x0100, -11000, 2200, 0)
        bytesL1 = MotorPType.stepMpToEndLoc(0x0101, -8000, 1600, 0)
        bytesL2 = MotorPType.stepMpToEndLoc(0x0102, 9000, 1800, 0)
        bytesL3 = MotorPType.stepMpToEndLoc(0x0103, -5000, 1000, 0)
        # 头部
        bytesHR1 = MotorPType.stepMpToEndLoc(0x010B, 3000, 600, 0)
        # 右臂
        bytesR5 = MotorPType.stepMpToEndLoc(0x0105, 4000, 800, 0)
        bytesR6 = MotorPType.stepMpToEndLoc(0x0106, -5000, 1000, 0)
        bytesR7 = MotorPType.stepMpToEndLoc(0x0107, -6000, 1200, 0)

        d.serial_send(
            bytesL0
            + bytesL1
            + bytesL2
            + bytesL3
            + bytesHR1
            + bytesR5
            + bytesR6
            + bytesR7
        )
        d.serial_send(ClassicType.endOrder())
        sleep(2.5)

    # 演讲动作右上
    @staticmethod
    def speakActionRightUp(d: HibotDriver):
        # 头部
        bytesHR1 = MotorPType.stepMpToEndLoc(0x010B, -3000, 600, 0)
        # 右臂
        bytesR5 = MotorPType.stepMpToEndLoc(0x0105, 11000, 2200, 0)
        bytesR6 = MotorPType.stepMpToEndLoc(0x0106, -8000, 1600, 0)
        bytesR7 = MotorPType.stepMpToEndLoc(0x0107, -9000, 1800, 0)
        bytesR8 = MotorPType.stepMpToEndLoc(0x0108, 5000, 1000, 0)

        d.serial_send(bytesHR1 + bytesR5 + bytesR6 + bytesR7 + bytesR8)
        d.serial_send(ClassicType.endOrder())
        sleep(2.5)

    # 演讲的左上
    @staticmethod
    def speakActionLeftUp(d: HibotDriver):
        # 左臂
        bytesL0 = MotorPType.stepMpToEndLoc(0x0100, -11000, 2200, 0)
        bytesL1 = MotorPType.stepMpToEndLoc(0x0101, -8000, 1600, 0)
        bytesL2 = MotorPType.stepMpToEndLoc(0x0102, 9000, 1800, 0)
        bytesL3 = MotorPType.stepMpToEndLoc(0x0103, -5000, 1000, 0)
        # 头部
        bytesHR1 = MotorPType.stepMpToEndLoc(0x010B, 3000, 600, 0)

        d.serial_send(bytesL0 + bytesL1 + bytesL2 + bytesL3 + bytesHR1)
        d.serial_send(ClassicType.endOrder())
        sleep(2.5)
