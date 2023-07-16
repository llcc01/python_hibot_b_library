import crcmod

crc16 = crcmod.mkCrcFun(0x18005, initCrc=0xFFFF, xorOut=0x0000)

class FrameOne:
    FRAME_BEGIN = 0xB78C
    FRAME_END = 0xACBD
    FRAME_HEAD_LENGTH = 4
    FRAME_TAIL_LENGTH = 4

    @staticmethod
    def change(paramInt: int) -> bytes:
        return paramInt.to_bytes(2, byteorder='little')

    @staticmethod
    def output(paramArrayOfbyte: bytearray, paramInt1: int, paramInt2: int) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput+=FrameOne.FRAME_BEGIN.to_bytes(2, byteorder='big')
        byteArrayOutput+=FrameOne.change(len(paramArrayOfbyte))
        byteArrayOutput+=paramArrayOfbyte
        byteArrayOutput+=crc16(paramArrayOfbyte).to_bytes(2, byteorder='big')
        byteArrayOutput+=FrameOne.FRAME_END.to_bytes(2, byteorder='big')
        return byteArrayOutput

# 数据第二层
class FrameTwo:
    FRAME_HEAD_LENGTH = 10
    i = 7

    @staticmethod
    def change(paramInt: int) -> bytes:
        return paramInt.to_bytes(2, byteorder='little')

    @staticmethod
    def two(targetId: int, sendId: int, type: int, serial: int, data: bytearray, priority: int) -> bytearray:
        FrameTwo.i += 1
        FrameTwo.i &= 0xFF
        byteArrayOutput = bytearray()
        byteArrayOutput+=FrameTwo.change(targetId)
        byteArrayOutput+=FrameTwo.change(sendId)
        byteArrayOutput.append(priority)
        byteArrayOutput.append(FrameTwo.i)
        byteArrayOutput+=FrameTwo.change(type)
        byteArrayOutput+=FrameTwo.change(serial)
        byteArrayOutput+=data
        return byteArrayOutput

class FrameThree:
    @staticmethod
    def change(paramInt: int) -> bytes:
        return paramInt.to_bytes(2, byteorder='little',signed=True)

    @staticmethod
    def changeD(paramDouble: float) -> bytearray:
        l = int(1.0E10 * paramDouble)
        arrayOfByte = bytearray(8)
        arrayOfByte[0] = (l & 0xFF)
        arrayOfByte[1] = (l >> 8 & 0xFF)
        arrayOfByte[2] = (l >> 16 & 0xFF)
        arrayOfByte[3] = (l >> 24 & 0xFF)
        arrayOfByte[4] = (l >> 32 & 0xFF)
        arrayOfByte[5] = (l >> 40 & 0xFF)
        arrayOfByte[6] = (l >> 48 & 0xFF)
        arrayOfByte[7] = (l >> 56 & 0xFF)
        return arrayOfByte

    @staticmethod
    def changeFourBytes(paramInt: int) -> bytes:
        return paramInt.to_bytes(4, byteorder='little')

    @staticmethod
    def send1(paramInt1: int, paramInt2: int, paramInt3: int) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput+=FrameThree.change(paramInt1)
        byteArrayOutput+=FrameThree.change(paramInt2)
        byteArrayOutput.append(paramInt3)
        return byteArrayOutput

    @staticmethod
    def send10(paramInt1: int, paramInt2: int, paramInt3: int) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput.append(paramInt1)
        byteArrayOutput+=FrameThree.change(paramInt2)
        byteArrayOutput+=FrameThree.change(paramInt3)
        return byteArrayOutput

    @staticmethod
    def send11(paramInt1: int, paramInt2: int, paramInt3: int, paramDouble1:
                float, paramDouble2: float, paramDouble3: float, paramInt4: int) -> bytearray:
          byteArrayOutput = bytearray()
          byteArrayOutput+=FrameThree.change(paramInt1 * 10)
          byteArrayOutput+=FrameThree.change(paramInt2 * 10)
          byteArrayOutput+=FrameThree.change(paramInt3)
          byteArrayOutput+=FrameThree.change(paramDouble1)
          byteArrayOutput+=FrameThree.change(paramDouble2)
          byteArrayOutput+=FrameThree.change(paramDouble3)
          byteArrayOutput.append(paramInt4)
          return byteArrayOutput
    
    @staticmethod
    def send12(paramInt: int) -> bytearray:
        return FrameThree.change(paramInt)
    
    @staticmethod
    def send13(paramInt: int) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput.append(paramInt)
        return byteArrayOutput
    
    @staticmethod
    def send14(paramInt: int, paramArrayOfbyte: bytearray) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput.append(int(115))
        byteArrayOutput.append(int(116))
        byteArrayOutput.append(int(97))
        byteArrayOutput.append(int(114))
        byteArrayOutput.append(int(116))
        byteArrayOutput+=crc16(paramArrayOfbyte).to_bytes(2, byteorder='big')
        byteArrayOutput+=FrameThree.change(paramInt)
        byteArrayOutput+=FrameThree.change(len(paramArrayOfbyte))
        byteArrayOutput+=paramArrayOfbyte
        return byteArrayOutput
    
    @staticmethod
    def send15(paramArrayOfbyte: bytearray) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput.append(int(115))
        byteArrayOutput.append(int(116))
        byteArrayOutput.append(int(97))
        byteArrayOutput.append(int(114))
        byteArrayOutput.append(int(116))
        byteArrayOutput.append(int(101))
        byteArrayOutput.append(int(110))
        byteArrayOutput.append(int(100))
        byteArrayOutput+=crc16(paramArrayOfbyte).to_bytes(2, byteorder='big')
        return byteArrayOutput
    
    @staticmethod
    def send16(paramInt1: int, paramInt2: int, paramInt3: int) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput+=FrameThree.change(paramInt1)
        byteArrayOutput+=FrameThree.change(paramInt2)
        byteArrayOutput.append(paramInt3)
        return byteArrayOutput
    
    @staticmethod
    def send17(paramInt: int) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput.append(paramInt)
        return byteArrayOutput
    
    @staticmethod
    def send18(paramInt: int) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput.append(paramInt)
        return byteArrayOutput
    
    @staticmethod
    def send19(paramInt: int) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput.append(paramInt.to_bytes(2, byteorder='big'))
        byteArrayOutput.append(bytearray(10))
        return byteArrayOutput
    
    @staticmethod
    def send2(paramInt1: int, paramInt2: int, paramInt3: int) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput+=FrameThree.change(paramInt1)
        byteArrayOutput+=FrameThree.change(paramInt2)
        byteArrayOutput.append(paramInt3)
        return byteArrayOutput
    
    @staticmethod
    def send20(paramInt1: int, paramInt2: int) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput.append(paramInt1.to_bytes(4, byteorder='big'))
        byteArrayOutput.append(paramInt2.to_bytes(4, byteorder='big'))
        return byteArrayOutput
    
    @staticmethod
    def send21(paramInt1: int, paramInt2: int, paramInt3: int, paramInt4: int, paramInt5: int) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput+=FrameThree.changeFourBytes(paramInt1)
        byteArrayOutput+=FrameThree.changeFourBytes(paramInt2)
        byteArrayOutput+=FrameThree.changeFourBytes(paramInt3)
        byteArrayOutput+=FrameThree.changeFourBytes(paramInt4)
        byteArrayOutput+=FrameThree.change(paramInt5)
        return byteArrayOutput
    
    @staticmethod
    def send3(paramInt: int, paramArrayOfint: bytearray) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput.append(paramInt)
        for i in range(len(paramArrayOfint)):
            byteArrayOutput+=FrameThree.change(paramArrayOfint[i])
        return byteArrayOutput
    
    @staticmethod
    def send4(paramInt1: int, paramInt2: int) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput.append(paramInt1)
        byteArrayOutput+=FrameThree.change(paramInt2)
        return byteArrayOutput
    
    @staticmethod
    def send5(paramInt1: int, paramInt2: int, paramInt3: int) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput+=FrameThree.change(paramInt1)
        byteArrayOutput+=FrameThree.change(paramInt2)
        byteArrayOutput+=FrameThree.change(paramInt3)
        return byteArrayOutput
    
    @staticmethod
    def send6(paramInt1: int, paramInt2: int, paramInt3: int, paramInt4: int, paramInt5: int, paramInt6: int, paramInt7: int, paramInt8: int, paramInt9: int, paramInt10: int, paramInt11: int, paramInt12: int, paramInt13: int, paramInt14: int, paramInt15: int, paramInt16: int, paramInt17: int, paramInt18: int, paramInt19: int, paramInt20: int, paramInt21: int, paramInt22: int, paramInt23: int, paramInt24: int, paramInt25: int) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput.append(paramInt1)
        byteArrayOutput.append(paramInt2)
        byteArrayOutput.append(paramInt3)
        byteArrayOutput.append(paramInt4)
        byteArrayOutput.append(paramInt5)
        byteArrayOutput.append(paramInt6)
        byteArrayOutput.append(paramInt7)
        byteArrayOutput.append(paramInt8)
        byteArrayOutput.append(paramInt9)
        byteArrayOutput.append(paramInt10)
        byteArrayOutput.append(paramInt11)
        byteArrayOutput.append(paramInt12)
        byteArrayOutput.append(paramInt13)
        byteArrayOutput.append(paramInt14)
        byteArrayOutput.append(paramInt15)
        byteArrayOutput.append(paramInt16)
        byteArrayOutput.append(paramInt17)
        byteArrayOutput.append(paramInt18)
        byteArrayOutput.append(paramInt19)
        byteArrayOutput.append(paramInt20)
        byteArrayOutput.append(paramInt21)
        byteArrayOutput.append(paramInt22)
        byteArrayOutput.append(paramInt23)
        byteArrayOutput.append(paramInt24)
        byteArrayOutput.append(paramInt25)
        return byteArrayOutput
    
    @staticmethod
    def send7(paramInt1: int, paramInt2: int, paramInt3: int, paramInt4: int) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput.append(paramInt1)
        byteArrayOutput.append(paramInt2)
        byteArrayOutput.append(paramInt3)
        byteArrayOutput.append(paramInt4)
        return byteArrayOutput
    
    @staticmethod
    def send8(paramInt1: int, paramInt2: int, paramInt3: int, paramInt4: int) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput.append(paramInt1)
        byteArrayOutput.append(paramInt2)
        byteArrayOutput.append(paramInt3)
        byteArrayOutput.append(paramInt4)
        return byteArrayOutput
    
    @staticmethod
    def send9(paramInt: int) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput.append(paramInt)
        return byteArrayOutput
    
    @staticmethod
    def sendLong(paramDouble: float) -> bytearray:
        dataOutputStream = bytearray()
        l = int(1.0E10 * paramDouble)
        arrayOfByte = bytearray(8)
        arrayOfByte[0] = (l & 0xFF)
        arrayOfByte[1] = (l >> 8 & 0xFF)
        arrayOfByte[2] = (l >> 16 & 0xFF)
        arrayOfByte[3] = (l >> 24 & 0xFF)
        arrayOfByte[4] = (l >> 32 & 0xFF)
        arrayOfByte[5] = (l >> 40 & 0xFF)
        arrayOfByte[6] = (l >> 48 & 0xFF)
        arrayOfByte[7] = (l >> 56 & 0xFF)
        dataOutputStream.append(arrayOfByte[0])
        dataOutputStream.append(arrayOfByte[1])
        dataOutputStream.append(arrayOfByte[2])
        dataOutputStream.append(arrayOfByte[3])
        dataOutputStream.append(arrayOfByte[4])
        dataOutputStream.append(arrayOfByte[5])
        dataOutputStream.append(arrayOfByte[6])
        dataOutputStream.append(arrayOfByte[7])
        return dataOutputStream