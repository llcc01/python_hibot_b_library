import serial
import threading

class HibotDriver:
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.ser = serial.Serial(port, baudrate, timeout=1)
        self.ser.flush()
        self.mutex = threading.Lock()

    def serial_send(self, data: bytearray):
        print(data.hex())
        self.ser.write(data)

    def serial_read(self):
        return self.ser.readline().decode('utf-8').rstrip()

    def serial_close(self):
        self.ser.close()

    def serial_flush(self):
        self.ser.flush()

    def do_action(self, action):
        self.lock()
        action(self)
        self.unlock()

    def lock(self):
        self.mutex.acquire()

    def unlock(self):
        self.mutex.release()
