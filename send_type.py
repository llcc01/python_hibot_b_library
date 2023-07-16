from frame import FrameOne, FrameTwo, FrameThree

# 底盘是否是有刷直流电机
brush = False

# 是否锁住底盘
lockClassic = False

class ClassicType:

    # 机身静止
    @staticmethod
    def motionless():
        bytes = bytearray()
        if brush:
            bytes1 = FrameTwo.two(0x0300, 0x0000, 0x0003, 0x0000, 0x0000, bytes, 1)
            output = FrameOne.output(bytes1, 0x00, 0x03)
            return output
        else:
            bytes1 = FrameTwo.two(0x0500, 0x0000, 0x0003, 0x0000, 0x0000, bytes, 1)
            output = FrameOne.output(bytes1, 0x00, 0x05)
            return output

    # 自由运动-不充电(1:开启      0：关闭)
    @staticmethod
    def libertyMoveNoCharge(control) -> bytearray:
        bytes = FrameThree.send18(control)
        if brush:
            bytes1 = FrameTwo.two(0x0300, 0x0000, 0x0003, 0x0001, 0x0000, bytes, 1)
            output = FrameOne.output(bytes1, 0x00, 0x03)
            if not lockClassic:
                return output
            else:
                if control == 0:
                    return output
                else:
                    return bytearray()
        else:
            bytes1 = FrameTwo.two(0x0500, 0x0000, 0x0003, 0x0001, 0x0000, bytes, 1)
            output = FrameOne.output(bytes1, 0x00, 0x05)
            if not lockClassic:
                return output
            else:
                if control == 0:
                    return output
                else:
                    return bytearray()

    # 自由运动-充电(1:开启      0：关闭)
    @staticmethod
    def libertyMoveCharge(control) -> bytearray:
        bytes = FrameThree.send18(control)
        if brush:
            bytes1 = FrameTwo.two(0x0300, 0x0000, 0x0003, 0x0002, 0x0000, bytes, 1)
            output = FrameOne.output(bytes1, 0x00, 0x03)
            if not lockClassic:
                return output
            else:
                if control == 0:
                    return output
                else:
                    return bytearray()
        else:
            bytes1 = FrameTwo.two(0x0500, 0x0000, 0x0003, 0x0002, 0x0000, bytes, 1)
            output = FrameOne.output(bytes1, 0x00, 0x05)
            if not lockClassic:
                return output
            else:
                if control == 0:
                    return output
                else:
                    return bytearray()
                
    # 角度旋转
    @staticmethod
    def stepRun(mode, degree) -> bytearray:
        bytes = FrameThree.send4(mode, degree)
        if brush:
            bytes1 = FrameTwo.two(0x0300, 0x0000, 0x0003, 0x0003, 0x0000, bytes, 1)
            output = FrameOne.output(bytes1, 0x00, 0x03)
            if not lockClassic:
                return output
            else:
                return bytearray()
        else:
            bytes1 = FrameTwo.two(0x0500, 0x0000, 0x0003, 0x0003, 0x0000, bytes, 1)
            output = FrameOne.output(bytes1, 0x00, 0x05)
            if not lockClassic:
                return output
            else:
                return bytearray()
            
    # 速度控制
    @staticmethod
    def runWithSpeed(left, right, time) -> bytearray:
        bytes = FrameThree.send5(left, right, time)
        if brush:
            bytes1 = FrameTwo.two(0x0300, 0x0000, 0x0003, 0x0004, bytes, 1)
            output = FrameOne.output(bytes1, 0x00, 0x03)
            if not lockClassic:
                return output
            else:
                if left == 0 and right == 0:
                    return output
                else:
                    return bytearray()
        else:
            bytes1 = FrameTwo.two(0x0500, 0x0000, 0x0003, 0x0004, bytes, 1)
            output = FrameOne.output(bytes1, 0x00, 0x05)
            if not lockClassic:
                return output
            else:
                if left == 0 and right == 0:
                    return output
                else:
                    return bytearray()
                
    # 数据反馈
    @staticmethod
    def getClassicData() -> bytearray:
        bytes = bytearray()
        if brush:
            bytes1 = FrameTwo.two(0x0300, 0x0000, 0x0003, 0x0005, bytes, 1)
            output = FrameOne.output(bytes1, 0x00, 0x03)
            return output
        else:
            bytes1 = FrameTwo.two(0x0500, 0x0000, 0x0003, 0x0005, bytes, 1)
            output = FrameOne.output(bytes1, 0x00, 0x05)
            return output
        
    # 结束指令
    @staticmethod
    def endOrder() -> bytearray:
        bytes = bytearray()
        bytes1 = FrameTwo.two(0x00FE, 0x0000, 0, 0, bytes, 1)
        output = FrameOne.output(bytes1, 0xFE, 0x00)
        return output
    
    # 自主避障运动
    @staticmethod
    def obsAvoidance(status) -> bytearray:
        bytes = FrameThree.send13(status)
        if brush:
            bytes1 = FrameTwo.two(0x0300, 0x0000, 0x0003, 0x0008, 0x0000, bytes, 1)
            output = FrameOne.output(bytes1, 0x00, 0x03)
            if not lockClassic:
                return output
            else:
                if status == 0:
                    return output
                else:
                    return bytearray()
        else:
            bytes1 = FrameTwo.two(0x0500, 0x0000, 0x0003, 0x0008, 0x0000, bytes, 1)
            output = FrameOne.output(bytes1, 0x00, 0x05)
            if not lockClassic:
                return output
            else:
                if status == 0:
                    return output
                else:
                    return bytearray()
                
    # 获取底盘控制固件版本号
    @staticmethod
    def getFwVersion() -> bytearray:
        bytes = bytearray()
        if brush:
            bytes1 = FrameTwo.two(0x0300, 0x0000, 0x0003, 0x0006, bytes, 1)
            output = FrameOne.output(bytes1, 0x00, 0x03)
            return output
        else:
            bytes1 = FrameTwo.two(0x0500, 0x0000, 0x0003, 0x0006, bytes, 1)
            output = FrameOne.output(bytes1, 0x00, 0x05)
            return output
        
    # 让底盘控制进入 bootloader 模式
    @staticmethod
    def intoBootloader() -> bytearray:
        bytes = bytearray()
        if brush:
            bytes1 = FrameTwo.two(0x0300, 0x0000, 0x0003, 0x0007, 0x0000, bytes, 1)
            output = FrameOne.output(bytes1, 0x00, 0x03)
            return output
        else:
            bytes1 = FrameTwo.two(0x0500, 0x0000, 0x0003, 0x0007, 0x0000, bytes, 1)
            output = FrameOne.output(bytes1, 0x00, 0x05)
            return output
        
    # 让底盘控制进入 UWB  定位 模式
    @staticmethod
    def classicIntoUWB(currentX, currentY, expectX, expectY, deflection) -> bytearray:
        bytes = FrameThree.send21(currentX, currentY, expectX, expectY, deflection)
        if brush:
            bytes1 = FrameTwo.two(0x0300, 0x0000, 0x0003, 0x0008, 0x0000, bytes, 1)
            output = FrameOne.output(bytes1, 0x00, 0x03)
            return output
        else:
            bytes1 = FrameTwo.two(0x0500, 0x0000, 0x0003, 0x0008, 0x0000, bytes, 1)
            output = FrameOne.output(bytes1, 0x00, 0x05)
            return output
        
    # 发送更新数据
    @staticmethod
    def sendUpdata(indexData, data) -> bytearray:
        bytes = FrameThree.send14(indexData, data)
        if brush:
            bytes1 = FrameTwo.two(0x0300, 0x0000, 0x00A0, 0x00A0, 0x0000, bytes, 1)
            output = FrameOne.output(bytes1, 0x00, 0x03)
            return output
        else:
            bytes1 = FrameTwo.two(0x0500, 0x0000, 0x00A0, 0x00A0, 0x0000, bytes, 1)
            output = FrameOne.output(bytes1, 0x00, 0x05)
            return output
        
    # 所有更新数据发送完毕指令
    @staticmethod
    def sendUdEnd(data) -> bytearray:
        bytes = FrameThree.send15(data)
        if brush:
            bytes1 = FrameTwo.two(0x0300, 0x0000, 0x00A0, 0x00A0, 0x0000, bytes, 1)
            output = FrameOne.output(bytes1, 0x00, 0x03)
            return output
        else:
            bytes1 = FrameTwo.two(0x0500, 0x0000, 0x00A0, 0x00A0, 0x0000, bytes, 1)
            output = FrameOne.output(bytes1, 0x00, 0x05)
            return output

class EleType:

    # 电机电源断电
    @staticmethod
    def offPower() -> bytearray:
        bytes = bytearray()
        bytes1 = FrameTwo.two(0x0200, 0x0000, 0x0002, 0x0000, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x02)
        return output

    # 电机上电
    @staticmethod
    def onPower() -> bytearray:
        bytes = bytearray()
        bytes1 = FrameTwo.two(0x0200, 0x0000, 0x0002, 0x0001, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x02)
        return output

    # 读取电池状态
    @staticmethod
    def getBatteryData() -> bytearray:
        bytes = bytearray()
        bytes1 = FrameTwo.two(0x0200, 0x0000, 0x0002, 0x0002, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x02)
        return output

    # 获取电源控制固件版本号
    @staticmethod
    def getFwVersion() -> bytearray:
        bytes = bytearray()
        bytes1 = FrameTwo.two(0x0200, 0x0000, 0x0002, 0x0003, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x02)
        return output

    # 让电源控制进入 bootloader 模式
    @staticmethod
    def intoBootloader() -> bytearray:
        bytes = bytearray()
        bytes1 = FrameTwo.two(0x0200, 0x0000, 0x0002, 0x0004, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x02)
        return output

    # 复位电源
    @staticmethod
    def resetPower() -> bytearray:
        bytes = bytearray()
        bytes1 = FrameTwo.two(0x0200, 0x0000, 0x0002, 0x0006, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x02)
        return output
    
    # 设置电池信息
    @staticmethod
    def setBatteryInfo() -> bytearray:
        bytes = bytearray()
        bytes1 = FrameTwo.two(0x0200, 0x0000, 0x0002, 0x0007, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x02)
        return output
    
    # 开启风扇
    @staticmethod
    def openFan() -> bytearray:
        bytes = bytearray()
        bytes1 = FrameTwo.two(0x0200, 0x0000, 0x0002, 0x0008, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x02)
        return output
    
    # 关闭风扇
    @staticmethod
    def closeFan() -> bytearray:
        bytes = bytearray()
        bytes1 = FrameTwo.two(0x0200, 0x0000, 0x0002, 0x0009, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x02)
        return output
    
    # 打印数据
    @staticmethod
    def print(content: str) -> bytearray:
        bytes = bytearray()
        bytes = content.encode('gb2312')
        bytes1 = FrameTwo.two(0x0200, 0x0000, 0x0002, 0x000A, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x02)
        return output
    
    # 发送更新数据
    @staticmethod
    def sendUpdata(indexData, data) -> bytearray:
        bytes = FrameThree.send14(indexData, data)
        bytes1 = FrameTwo.two(0x0200, 0x0000, 0x00A0, 0x00A0, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x02)
        return output
    
    # 所有更新数据发送完毕指令
    @staticmethod
    def sendUdEnd(data) -> bytearray:
        bytes = FrameThree.send15(data)
        bytes1 = FrameTwo.two(0x0200, 0x0000, 0x00A0, 0x00A0, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x02)
        return output

class LightType:

    # 眼睛灯光的效果控制
    @staticmethod
    def eyeControll(controlMode, r1, g1, b1, r2, g2, b2, r3, g3, b3, r4, g4, b4,
                    r5, g5, b5, r6, g6, b6, r7, g7, b7, r8, g8, b8) -> bytearray:
        bytes = FrameThree.send6(controlMode, r1, g1, b1, r2, g2, b2, r3, g3, b3, r4, g4, b4,
                                 r5, g5, b5, r6, g6, b6, r7, g7, b7, r8, g8, b8)
        bytes1 = FrameTwo.two(0x0400, 0x0000, 0x0004, 0x0000, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x05)
        return output

    # 耳朵灯光控制效果
    @staticmethod
    def earControll(controlMode, r1, g1, b1) -> bytearray:
        bytes = FrameThree.send7(controlMode, r1, g1, b1)
        bytes1 = FrameTwo.two(0x0400, 0x0000, 0x0004, 0x0001, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x05)
        return output

    # 头顶灯光效果控制
    @staticmethod
    def topHeadControll(controlMode, r1, g1, b1) -> bytearray:
        bytes = FrameThree.send8(controlMode, r1, g1, b1)
        bytes1 = FrameTwo.two(0x0400, 0x0000, 0x0004, 0x0002, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x05)
        return output

    # 头部参数读取
    @staticmethod
    def headStatus() -> bytearray:
        bytes = bytearray()
        bytes1 = FrameTwo.two(0x0400, 0x0000, 0x0004, 0x0003, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x05)
        return output
    
    # 声源增强
    @staticmethod
    def headVoice(number) -> bytearray:
        bytes = FrameThree.send9(number)
        bytes1 = FrameTwo.two(0x0400, 0x0000, 0x0004, 0x0004, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x05)
        return output
    
    # 获取头部固件版本号
    @staticmethod
    def getHeadFwVersion() -> bytearray:
        bytes = bytearray()
        bytes1 = FrameTwo.two(0x0400, 0x0000, 0x0004, 0x0005, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x05)
        return output
    
    # 让头部进入 bootloader 模式
    @staticmethod
    def intoBootloader() -> bytearray:
        bytes = bytearray()
        bytes1 = FrameTwo.two(0x0400, 0x0000, 0x0004, 0x0006, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x05)
        return output
    
    # 让讯飞语音模块复位
    @staticmethod
    def resetModule() -> bytearray:
        bytes = bytearray()
        bytes1 = FrameTwo.two(0x0400, 0x0000, 0x0004, 0x0007, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x05)
        return output
    
    # 获取 uwb 数据
    @staticmethod
    def getUWBData() -> bytearray:
        bytes = bytearray()
        bytes1 = FrameTwo.two(0x0400, 0x0000, 0x0004, 0x0008, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x05)
        return output
    
    # 无线麦开关控制
    @staticmethod
    def wirelessMicControll(on_off) -> bytearray:
        bytes = FrameThree.send17(on_off)
        bytes1 = FrameTwo.two(0x0400, 0x0000, 0x0004, 0x0009, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x01)
        return output
    
    # 获取 uwb C帧数据
    @staticmethod
    def getUWBDataC() -> bytearray:
        bytes = bytearray()
        bytes1 = FrameTwo.two(0x0400, 0x0000, 0x0004, 0x000A, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x05)
        return output
    
    # 发送更新数据
    @staticmethod
    def sendUpdata(indexData, data) -> bytearray:
        bytes = FrameThree.send14(indexData, data)
        bytes1 = FrameTwo.two(0x0400, 0x0000, 0x00A0, 0x00A0, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x05)
        return output
    
    # 所有更新数据发送完毕指令
    @staticmethod
    def sendUdEnd(data) -> bytearray:
        bytes = FrameThree.send15(data)
        bytes1 = FrameTwo.two(0x0400, 0x0000, 0x00A0, 0x00A0, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x05)
        return output

class MainCtl:
    
        # 获取407控制固件版本号
        @staticmethod
        def getFwVersion() -> bytearray:
            bytes = bytearray()
            bytes1 = FrameTwo.two(0x00FC, 0x0000, 0x0004, 0x0005, bytes, 1)
            output = FrameOne.output(bytes1, 0x00, 0x05)
            return output
    
        # 让f407进入 bootloader 模式
        @staticmethod
        def intoBootloader() -> bytearray:
            bytes = bytearray()
            bytes1 = FrameTwo.two(0x00FD, 0x0000, 0x0004, 0x0006, bytes, 1)
            output = FrameOne.output(bytes1, 0x00, 0x05)
            return output
    
        # 发送更新数据
        @staticmethod
        def sendUpdata(indexData, data) -> bytearray:
            bytes = FrameThree.send14(indexData, data)
            return bytes
    
        # 所有更新数据发送完毕指令
        @staticmethod
        def sendUdEnd(data) -> bytearray:
            bytes = FrameThree.send15(data)
            return bytes

class MotorPType:
    # 步进电机强制断电
    @staticmethod
    def stepMpOutage() -> bytearray:
        bytes = bytearray()
        bytes1 = FrameTwo.two(0x0100, 0x0000, 0x0001, 0x0000, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x01)
        return output

    # 步进电机强制停止运动
    @staticmethod
    def stepMpStop() -> bytearray:
        bytes = bytearray()
        bytes1 = FrameTwo.two(0x0100, 0x0000, 0x0001, 0x0001, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x01)
        return output

    # 读取步进电机的状态
    @staticmethod
    def stepMpStatus(targetId) -> bytearray:
        bytes = bytearray()
        bytes1 = FrameTwo.two(targetId, 0x0000, 0x0001, 0x0002, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x01)
        return output

    # 设置步进电机返回零点运动
    @staticmethod
    def stepMpZero(targetId, speed) -> bytearray:
        bytes = FrameThree.send12(speed)
        bytes1 = FrameTwo.two(targetId, 0x0000, 0x0001, 0x0003, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x01)
        return output

    # 设置步进电机根据设定参数运动
    @staticmethod
    def stepMpParamsRun(targetId, rSpeed, rJourney, endMode) -> bytearray:
        bytes = FrameThree.send1(rSpeed, rJourney, endMode)
        bytes1 = FrameTwo.two(targetId, 0x0000, 0x0001, 0x0004, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x01)
        return output

    # 设置步进电机进行位置缓存运动
    @staticmethod
    def stepMpLocation(rSpeed, rJourney, endMode) -> bytearray:
        bytes = FrameThree.send2(rSpeed, rJourney, endMode)
        bytes1 = FrameTwo.two(0x0100, 0x0000, 0x0001, 0x0005, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x01)
        return output
    
    # 设置步进电机运行位置表发送
    @staticmethod
    def stepMpLoc(way, ints) -> bytearray:
        bytes = FrameThree.send3(way, ints)
        bytes1 = FrameTwo.two(0x0100, 0x0000, 0x0001, 0x0006, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x01)
        return output
    
    # 设置步进电机 电机运行目标位置运动
    @staticmethod
    def stepMpToEndLoc(targetId, endLoc, time, endMode) -> bytearray:
        bytes = FrameThree.send16(endLoc, time, endMode)
        bytes1 = FrameTwo.two(targetId, 0x0000, 0x0001, 0x0007, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x01)
        return output
    
    # 设置电机传感器校准参数采集
    @staticmethod
    def stepMpJiaoZhun(targetId, way, maiChong, degree) -> bytearray:
        bytes = FrameThree.send10(way, maiChong, degree)
        bytes1 = FrameTwo.two(targetId, 0x0000, 0x0001, 0x0008, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x01)
        return output
    
    # 配置电机控制参数
    @staticmethod
    def stepMpSetting(targetId, maxDegree, minDegee, maiChong, p1, p2, p3, way) -> bytearray:
        bytes = FrameThree.send11(maxDegree, minDegee, maiChong, p1, p2, p3, way)
        bytes1 = FrameTwo.two(targetId, 0x0000, 0x0001, 0x0009, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x01)
        return output
    
    # 获取电机控制固件版本号
    @staticmethod
    def getFwVersion(targetId) -> bytearray:
        bytes = bytearray()
        bytes1 = FrameTwo.two(targetId, 0x0000, 0x0001, 0x000A, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x01)
        return output
    
    # 让电机控制进入 bootloader 模式
    @staticmethod
    def intoBootloader(targetId) -> bytearray:
        bytes = bytearray()
        bytes1 = FrameTwo.two(targetId, 0x0000, 0x0001, 0x000B, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x01)
        return output
    
    @staticmethod
    def setElectricity(targetId, electricity) -> bytearray:
        bytes = FrameThree.send19(electricity)
        bytes1 = FrameTwo.two(targetId, 0x0000, 0x0001, 0x000C, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x01)
        return output
    
    # 发送更新数据
    @staticmethod
    def sendUpdata(targetId, indexData, data) -> bytearray:
        bytes = FrameThree.send14(indexData, data)
        bytes1 = FrameTwo.two(targetId, 0x0000, 0x00A0, 0x00A0, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x01)
        return output
    
    # 所有更新数据发送完毕指令
    @staticmethod
    def sendUdEnd(targetId, data) -> bytearray:
        bytes = FrameThree.send15(data)
        bytes1 = FrameTwo.two(targetId, 0x0000, 0x00A0, 0x00A0, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x01)
        return output
    
    # 设置步进电机根据设定参数运动
    @staticmethod
    def stepMpParamsRunNotEndDegree(targetId, rSpeed, rJourney, endMode) -> bytearray:
        bytes = FrameThree.send1(rSpeed, rJourney, endMode)
        bytes1 = FrameTwo.two(targetId, 0x0000, 0x0001, 0x000D, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x01)
        return output
    
    # 设置加速度
    @staticmethod
    def setAcceleratedSpeed(targetId, acceleratedSpeed, acceleratedAcceleratedSpeed) -> bytearray:
        bytes = FrameThree.send20(acceleratedSpeed, acceleratedAcceleratedSpeed)
        bytes1 = FrameTwo.two(targetId, 0x0000, 0x0001, 0x000E, bytes, 1)
        output = FrameOne.output(bytes1, 0x00, 0x01)
        return output