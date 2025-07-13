from mpu6050 import mpu6050

class MPU6050:
    def __init__(self, address=0x68):
        self.sensor = mpu6050(address)

    def read_accel(self):
        return self.sensor.get_accel_data()

    def read_gyro(self):
        return self.sensor.get_gyro_data()

    def read_all(self):
        return {
            'accel': self.read_accel(),
            'gyro': self.read_gyro()
        }
