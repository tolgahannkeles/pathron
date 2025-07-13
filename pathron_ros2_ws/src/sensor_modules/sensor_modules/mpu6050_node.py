import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from sensor_modules.mpu6050 import MPU6050  # <- Donanım sınıfı

class MPU6050Node(Node):
    def __init__(self):
        super().__init__('mpu6050_node')
        self.get_logger().info("MPU6050 ROS node başlatıldı.")

        self.sensor = MPU6050(address=0x68)
        self.publisher_ = self.create_publisher(Imu, 'imu/data_raw', 10)
        self.timer = self.create_timer(0.05, self.publish_imu_data)

    def publish_imu_data(self):
        try:
            data = self.sensor.read_all()
            accel = data['accel']
            gyro = data['gyro']

            imu_msg = Imu()
            imu_msg.header.stamp = self.get_clock().now().to_msg()
            imu_msg.header.frame_id = 'imu_link'

            imu_msg.linear_acceleration.x = accel['x']
            imu_msg.linear_acceleration.y = accel['y']
            imu_msg.linear_acceleration.z = accel['z']

            imu_msg.angular_velocity.x = gyro['x']
            imu_msg.angular_velocity.y = gyro['y']
            imu_msg.angular_velocity.z = gyro['z']

            self.publisher_.publish(imu_msg)
        except Exception as e:
            self.get_logger().error(f"MPU6050 okuma hatası: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = MPU6050Node()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Node kapatılıyor...")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
