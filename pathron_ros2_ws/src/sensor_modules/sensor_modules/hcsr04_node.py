import rclpy
from rclpy.node import Node
from sensor_modules.hcsr04 import HCSR04
from sensor_msgs.msg import Range
import yaml
import os
from ament_index_python.packages import get_package_share_directory

def load_pin_config():
    config_path = os.path.join(
        get_package_share_directory('pathron_config'),
        'config',
        'pin_config.yaml'
    )
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


class HCSR04Node(Node):
    def __init__(self):
        super().__init__('hcsr04_node')

        # Sensör sınıfını oluştur

        pins = load_pin_config()
        trig = pins['ultrasonic']['trig_pin']
        echo = pins['ultrasonic']['echo_pin']

        self.sensor = HCSR04(trig_pin=trig, echo_pin=echo)

        # ROS publisher
        self.publisher_ = self.create_publisher(Range, 'ultrasonic', 10)

        self.range_msg = Range()
        self.range_msg.radiation_type = Range.ULTRASOUND
        self.range_msg.field_of_view = 0.26
        self.range_msg.min_range = 0.02
        self.range_msg.max_range = 4.0
        self.range_msg.header.frame_id = 'ultrasonic_sensor'

        self.timer = self.create_timer(0.05, self.publish_distance)
        self.get_logger().info("HCSR04 ROS node started.")

    def publish_distance(self):
        try:
            distance = self.sensor.get_distance()
            self.range_msg.range = distance
            self.range_msg.header.stamp = self.get_clock().now().to_msg()
            self.publisher_.publish(self.range_msg)
        except Exception as e:
            self.get_logger().warn(f"Measurement failed: {e}")

    def destroy_node(self):
        self.sensor.cleanup()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = HCSR04Node()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Shutting down...")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
