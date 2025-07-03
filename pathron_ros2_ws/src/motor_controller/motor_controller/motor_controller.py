import rclpy
from rclpy.node import Node
from custom_interfaces.msg import MotorControl

class MotorControllerNode(Node):

    def __init__(self):
        super().__init__("motor_controller_node")
        self.create_subscription(MotorControl, "motor_control_topic", self.control_signal_callback, 10)
        self.get_logger().info("Motor Controller node initialized!")

    def control_signal_callback(self, signal: MotorControl):
        # linear: -100 (geri) → 0 → +100 (ileri)
        # angular: -100 (sağa dön) → 0 → +100 (sola dön)

        linear = signal.linear_velocity
        angular = signal.angular_velocity

        # Basit diferansiyel sürüş modeli:
        left_motor_speed = linear + angular
        right_motor_speed = linear - angular

        # Hızları sınırla (-100 ile 100 arası kalmalı)
        left_motor_speed = max(-100, min(100, left_motor_speed))
        right_motor_speed = max(-100, min(100, right_motor_speed))

        # Log çıktısı
        self.get_logger().info(
            f"Motor Güçleri - Left: {left_motor_speed}, Right: {right_motor_speed}"
        )

def main(args=None):
    rclpy.init(args=args)
    node = MotorControllerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
