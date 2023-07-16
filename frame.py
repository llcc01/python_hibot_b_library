class FrameOne:
    FRAME_BEGIN = 0xB78C
    FRAME_END = 0xACBD
    FRAME_HEAD_LENGTH = 4
    FRAME_TAIL_LENGTH = 4

    @staticmethod
    def change(paramInt: int) -> bytearray:
        return bytearray(paramInt.to_bytes(2, byteorder='big'))

    @staticmethod
    def crc16(paramArrayOfbyte, paramInt):
        i = 0x0000A001
        for j in range(paramInt):
            i ^= paramArrayOfbyte[j] & 0xFF
            k = 0
            while k < 8:
                n = i >> 1
                m = n
                if 1 == (i & 0x1):
                    m = n ^ 0xA001
                k += 1
                i = m
        return i

    @staticmethod
    def output(paramArrayOfbyte: bytearray, paramInt1: int, paramInt2: int) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput.append(FrameOne.FRAME_BEGIN.to_bytes(2, byteorder='big'))
        byteArrayOutput.append(FrameOne.change(len(paramArrayOfbyte)))
        byteArrayOutput.append(paramArrayOfbyte)
        byteArrayOutput.append(FrameOne.crc16(paramArrayOfbyte, len(paramArrayOfbyte)))
        byteArrayOutput.append(FrameOne.FRAME_END.to_bytes(2, byteorder='big'))
        return byteArrayOutput

class FrameTwo:
    FRAME_HEAD_LENGTH = 10
    i = 0

    @staticmethod
    def change(paramInt: int) -> bytearray:
        return bytearray(paramInt.to_bytes(2, byteorder='big'))

    @staticmethod
    def two(paramInt1: int, paramInt2: int, paramInt3: int, paramInt4: int, paramArrayOfbyte: bytearray, paramInt5: int) -> bytearray:
        FrameTwo.i += 1
        byteArrayOutput = bytearray()
        byteArrayOutput.append(FrameTwo.change(paramInt1))
        byteArrayOutput.append(FrameTwo.change(paramInt2))
        byteArrayOutput.append(paramInt5.to_bytes(1, byteorder='big'))
        byteArrayOutput.append(FrameTwo.i.to_bytes(1, byteorder='big'))
        byteArrayOutput.append(FrameTwo.change(paramInt3))
        byteArrayOutput.append(FrameTwo.change(paramInt4))
        byteArrayOutput.append(paramArrayOfbyte)
        return byteArrayOutput

class FrameThree:
    @staticmethod
    def change(paramInt: int) -> bytearray:
        return bytearray(paramInt.to_bytes(2, byteorder='big'))

    @staticmethod
    def change(paramDouble: float) -> bytearray:
        l = int(1.0E10 * paramDouble)
        arrayOfByte = bytearray(8)
        arrayOfByte[0] = (l & 0xFF).to_bytes(1, byteorder='big')
        arrayOfByte[1] = (l >> 8 & 0xFF).to_bytes(1, byteorder='big')
        arrayOfByte[2] = (l >> 16 & 0xFF).to_bytes(1, byteorder='big')
        arrayOfByte[3] = (l >> 24 & 0xFF).to_bytes(1, byteorder='big')
        arrayOfByte[4] = (l >> 32 & 0xFF).to_bytes(1, byteorder='big')
        arrayOfByte[5] = (l >> 40 & 0xFF).to_bytes(1, byteorder='big')
        arrayOfByte[6] = (l >> 48 & 0xFF).to_bytes(1, byteorder='big')
        arrayOfByte[7] = (l >> 56 & 0xFF).to_bytes(1, byteorder='big')
        return arrayOfByte

    @staticmethod
    def changeFourBytes(paramInt: int) -> bytearray:
        return bytearray(paramInt.to_bytes(4, byteorder='big'))

    @staticmethod
    def send1(paramInt1: int, paramInt2: int, paramInt3: int) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput.append(FrameThree.change(paramInt1))
        byteArrayOutput.append(FrameThree.change(paramInt2))
        byteArrayOutput.append(paramInt3.to_bytes(1, byteorder='big'))
        return byteArrayOutput

    @staticmethod
    def send10(paramInt1: int, paramInt2: int, paramInt3: int) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput.append(paramInt1.to_bytes(1, byteorder='big'))
        byteArrayOutput.append(FrameThree.change(paramInt2))
        byteArrayOutput.append(FrameThree.change(paramInt3))
        return byteArrayOutput

    @staticmethod
    def send11(paramInt1: int, paramInt2: int, paramInt3: int, paramDouble1:
                float, paramDouble2: float, paramDouble3: float, paramInt4: int) -> bytearray:
          byteArrayOutput = bytearray()
          byteArrayOutput.append(FrameThree.change(paramInt1 * 10))
          byteArrayOutput.append(FrameThree.change(paramInt2 * 10))
          byteArrayOutput.append(FrameThree.change(paramInt3))
          byteArrayOutput.append(FrameThree.change(paramDouble1))
          byteArrayOutput.append(FrameThree.change(paramDouble2))
          byteArrayOutput.append(FrameThree.change(paramDouble3))
          byteArrayOutput.append(paramInt4.to_bytes(1, byteorder='big'))
          return byteArrayOutput
    
    @staticmethod
    def send12(paramInt: int) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput.append(FrameThree.change(paramInt))
        return byteArrayOutput
    
    @staticmethod
    def send13(paramInt: int) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput.append(paramInt.to_bytes(1, byteorder='big'))
        return byteArrayOutput
    
    @staticmethod
    def send14(paramInt: int, paramArrayOfbyte: bytearray) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput.append(int(115).to_bytes(1, byteorder='big'))
        byteArrayOutput.append(int(116).to_bytes(1, byteorder='big'))
        byteArrayOutput.append(int(97).to_bytes(1, byteorder='big'))
        byteArrayOutput.append(int(114).to_bytes(1, byteorder='big'))
        byteArrayOutput.append(int(116).to_bytes(1, byteorder='big'))
        byteArrayOutput.append(FrameOne.crc16(paramArrayOfbyte, len(paramArrayOfbyte)).to_bytes(2, byteorder='big'))
        byteArrayOutput.append(FrameThree.change(paramInt))
        byteArrayOutput.append(FrameThree.change(len(paramArrayOfbyte)))
        byteArrayOutput.append(paramArrayOfbyte)
        return byteArrayOutput
    
    @staticmethod
    def send15(paramArrayOfbyte: bytearray) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput.append(int(115).to_bytes(1, byteorder='big'))
        byteArrayOutput.append(int(116).to_bytes(1, byteorder='big'))
        byteArrayOutput.append(int(97).to_bytes(1, byteorder='big'))
        byteArrayOutput.append(int(114).to_bytes(1, byteorder='big'))
        byteArrayOutput.append(int(116).to_bytes(1, byteorder='big'))
        byteArrayOutput.append(int(101).to_bytes(1, byteorder='big'))
        byteArrayOutput.append(int(110).to_bytes(1, byteorder='big'))
        byteArrayOutput.append(int(100).to_bytes(1, byteorder='big'))
        byteArrayOutput.append(FrameOne.crc16(paramArrayOfbyte, len(paramArrayOfbyte)).to_bytes(2, byteorder='big'))
        return byteArrayOutput
    
    @staticmethod
    def send16(paramInt1: int, paramInt2: int, paramInt3: int) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput.append(FrameThree.change(paramInt1))
        byteArrayOutput.append(FrameThree.change(paramInt2))
        byteArrayOutput.append(paramInt3.to_bytes(1, byteorder='big'))
        return byteArrayOutput
    
    @staticmethod
    def send17(paramInt: int) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput.append(paramInt.to_bytes(1, byteorder='big'))
        return byteArrayOutput
    
    @staticmethod
    def send18(paramInt: int) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput.append(paramInt.to_bytes(1, byteorder='big'))
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
        byteArrayOutput.append(FrameThree.change(paramInt1))
        byteArrayOutput.append(FrameThree.change(paramInt2))
        byteArrayOutput.append(paramInt3.to_bytes(1, byteorder='big'))
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
        byteArrayOutput.append(FrameThree.changeFourBytes(paramInt1))
        byteArrayOutput.append(FrameThree.changeFourBytes(paramInt2))
        byteArrayOutput.append(FrameThree.changeFourBytes(paramInt3))
        byteArrayOutput.append(FrameThree.changeFourBytes(paramInt4))
        byteArrayOutput.append(FrameThree.change(paramInt5))
        return byteArrayOutput
    
    @staticmethod
    def send3(paramInt: int, paramArrayOfint: bytearray) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput.append(paramInt.to_bytes(1, byteorder='big'))
        for i in range(len(paramArrayOfint)):
            byteArrayOutput.append(FrameThree.change(paramArrayOfint[i]))
        return byteArrayOutput
    
    @staticmethod
    def send4(paramInt1: int, paramInt2: int) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput.append(paramInt1.to_bytes(1, byteorder='big'))
        byteArrayOutput.append(FrameThree.change(paramInt2))
        return byteArrayOutput
    
    @staticmethod
    def send5(paramInt1: int, paramInt2: int, paramInt3: int) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput.append(FrameThree.change(paramInt1))
        byteArrayOutput.append(FrameThree.change(paramInt2))
        byteArrayOutput.append(FrameThree.change(paramInt3))
        return byteArrayOutput
    
    @staticmethod
    def send6(paramInt1: int, paramInt2: int, paramInt3: int, paramInt4: int, paramInt5: int, paramInt6: int, paramInt7: int, paramInt8: int, paramInt9: int, paramInt10: int, paramInt11: int, paramInt12: int, paramInt13: int, paramInt14: int, paramInt15: int, paramInt16: int, paramInt17: int, paramInt18: int, paramInt19: int, paramInt20: int, paramInt21: int, paramInt22: int, paramInt23: int, paramInt24: int, paramInt25: int) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput.append(paramInt1.to_bytes(1, byteorder='big'))
        byteArrayOutput.append(paramInt2.to_bytes(1, byteorder='big'))
        byteArrayOutput.append(paramInt3.to_bytes(1, byteorder='big'))
        byteArrayOutput.append(paramInt4.to_bytes(1, byteorder='big'))
        byteArrayOutput.append(paramInt5.to_bytes(1, byteorder='big'))
        byteArrayOutput.append(paramInt6.to_bytes(1, byteorder='big'))
        byteArrayOutput.append(paramInt7.to_bytes(1, byteorder='big'))
        byteArrayOutput.append(paramInt8.to_bytes(1, byteorder='big'))
        byteArrayOutput.append(paramInt9.to_bytes(1, byteorder='big'))
        byteArrayOutput.append(paramInt10.to_bytes(1, byteorder='big'))
        byteArrayOutput.append(paramInt11.to_bytes(1, byteorder='big'))
        byteArrayOutput.append(paramInt12.to_bytes(1, byteorder='big'))
        byteArrayOutput.append(paramInt13.to_bytes(1, byteorder='big'))
        byteArrayOutput.append(paramInt14.to_bytes(1, byteorder='big'))
        byteArrayOutput.append(paramInt15.to_bytes(1, byteorder='big'))
        byteArrayOutput.append(paramInt16.to_bytes(1, byteorder='big'))
        byteArrayOutput.append(paramInt17.to_bytes(1, byteorder='big'))
        byteArrayOutput.append(paramInt18.to_bytes(1, byteorder='big'))
        byteArrayOutput.append(paramInt19.to_bytes(1, byteorder='big'))
        byteArrayOutput.append(paramInt20.to_bytes(1, byteorder='big'))
        byteArrayOutput.append(paramInt21.to_bytes(1, byteorder='big'))
        byteArrayOutput.append(paramInt22.to_bytes(1, byteorder='big'))
        byteArrayOutput.append(paramInt23.to_bytes(1, byteorder='big'))
        byteArrayOutput.append(paramInt24.to_bytes(1, byteorder='big'))
        byteArrayOutput.append(paramInt25.to_bytes(1, byteorder='big'))
        return byteArrayOutput
    
    @staticmethod
    def send7(paramInt1: int, paramInt2: int, paramInt3: int, paramInt4: int) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput.append(paramInt1.to_bytes(1, byteorder='big'))
        byteArrayOutput.append(paramInt2.to_bytes(1, byteorder='big'))
        byteArrayOutput.append(paramInt3.to_bytes(1, byteorder='big'))
        byteArrayOutput.append(paramInt4.to_bytes(1, byteorder='big'))
        return byteArrayOutput
    
    @staticmethod
    def send8(paramInt1: int, paramInt2: int, paramInt3: int, paramInt4: int) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput.append(paramInt1.to_bytes(1, byteorder='big'))
        byteArrayOutput.append(paramInt2.to_bytes(1, byteorder='big'))
        byteArrayOutput.append(paramInt3.to_bytes(1, byteorder='big'))
        byteArrayOutput.append(paramInt4.to_bytes(1, byteorder='big'))
        return byteArrayOutput
    
    @staticmethod
    def send9(paramInt: int) -> bytearray:
        byteArrayOutput = bytearray()
        byteArrayOutput.append(paramInt.to_bytes(1, byteorder='big'))
        return byteArrayOutput
    
    @staticmethod
    def sendLong(paramDouble: float) -> bytearray:
        dataOutputStream = bytearray()
        l = int(1.0E10 * paramDouble)
        arrayOfByte = bytearray(8)
        arrayOfByte[0] = (l & 0xFF).to_bytes(1, byteorder='big')
        arrayOfByte[1] = (l >> 8 & 0xFF).to_bytes(1, byteorder='big')
        arrayOfByte[2] = (l >> 16 & 0xFF).to_bytes(1, byteorder='big')
        arrayOfByte[3] = (l >> 24 & 0xFF).to_bytes(1, byteorder='big')
        arrayOfByte[4] = (l >> 32 & 0xFF).to_bytes(1, byteorder='big')
        arrayOfByte[5] = (l >> 40 & 0xFF).to_bytes(1, byteorder='big')
        arrayOfByte[6] = (l >> 48 & 0xFF).to_bytes(1, byteorder='big')
        arrayOfByte[7] = (l >> 56 & 0xFF).to_bytes(1, byteorder='big')
        dataOutputStream.append(arrayOfByte[0])
        dataOutputStream.append(arrayOfByte[1])
        dataOutputStream.append(arrayOfByte[2])
        dataOutputStream.append(arrayOfByte[3])
        dataOutputStream.append(arrayOfByte[4])
        dataOutputStream.append(arrayOfByte[5])
        dataOutputStream.append(arrayOfByte[6])
        dataOutputStream.append(arrayOfByte[7])
        return dataOutputStream