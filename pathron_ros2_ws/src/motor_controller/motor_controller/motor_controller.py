import rclpy
from rclpy.node import Node
from custom_interfaces.msg import MotorControl
import platform

if platform.machine().startswith("arm") or platform.machine().startswith("aarch64"):  # Sadece Raspberry Pi’de
    from motor_controller.motor_driver import MotorDriver
else:
    MotorDriver = None  # Dummy fallback


class MotorControllerNode(Node):

    def __init__(self):
        super().__init__("motor_controller_node")
        self.create_subscription(MotorControl, "motor_control_topic", self.control_signal_callback, 10)

        if MotorDriver:
            self.motor_driver = MotorDriver(
                in1=17, in2=18, ena=24,
                in3=22, in4=23, enb=25
            )
            self.get_logger().info("MotorDriver initialized for Raspberry Pi.")
        else:
            self.motor_driver = None
            self.get_logger().warn("MotorDriver unavailable. Running in simulation mode.")

        self.get_logger().info("Motor Controller node initialized!")

    def control_signal_callback(self, signal: MotorControl):
        # linear: -100 (geri) → 0 → +100 (ileri)
        # angular: -100 (sağa dön) → 0 → +100 (sola dön)

        linear = signal.linear_velocity
        angular = signal.angular_velocity

        # Diferansiyel sürüş
        left_motor_speed = max(-100, min(100, linear + angular))
        right_motor_speed = max(-100, min(100, linear - angular))

        if self.motor_driver:
            self.motor_driver.set_motors(left_motor_speed, right_motor_speed)
        else:
            self.get_logger().info(f"[Simulated] Left: {left_motor_speed}, Right: {right_motor_speed}")

    def destroy_node(self):
        if self.motor_driver:
            self.motor_driver.stop()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = MotorControllerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()
