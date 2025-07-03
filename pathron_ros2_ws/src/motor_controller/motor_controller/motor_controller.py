import rclpy
from rclpy.node import Node
from custom_interfaces.msg import MotorControl

class MotorControllerNode(Node):

    def __init__(self):
        super().__init__("motor_controller_node")
        self.create_subscription(MotorControl, "motor_control_topic", self.control_signal_callback, 10)
        self.get_logger().info("Motor Controller node initialized!")

    def control_signal_callback(self, signal: MotorControl):
        self.get_logger().info(
            f"Motor Status - FL: {signal.front_left}, FR: {signal.front_right}, "
            f"RL: {signal.rear_left}, RR: {signal.rear_right}"
        )

def main(args=None):
    rclpy.init()
    node = MotorControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()