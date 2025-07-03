import rclpy
from rclpy.node import Node
from custom_interfaces.msg import MotorControl
import threading
import sys
import termios
import tty

class KeyboardDriverNode(Node):

    def __init__(self):
        super().__init__("keyboard_driver_node")
        self.motor_pub_ = self.create_publisher(MotorControl, "motor_control_topic", 10)

        self.linear_velocity = 0
        self.angular_velocity = 0

        self.last_linear_velocity = None
        self.last_angular_velocity = None

        self.settings = termios.tcgetattr(sys.stdin)

        self.keyboard_thread = threading.Thread(target=self.keyboard_listener)
        self.keyboard_thread.daemon = True
        self.keyboard_thread.start()

        self.get_logger().info("Keyboard Driver Node started.")
        self.print_instructions()

    def print_instructions(self):
        print("\n" + "="*50)
        print("KEYBOARD MOTOR CONTROL")
        print("="*50)
        print("W: İleri (linear +10)")
        print("S: Geri (linear -10)")
        print("A: Sola dön (angular -10)")
        print("D: Sağa dön (angular +10)")
        print("SPACE: Tümünü durdur")
        print("X: Çıkış")
        print("="*50)
        self.print_motor_status()

    def print_motor_status(self):
        sys.stdout.write(f"\rLinear: {self.linear_velocity:>4} | Angular: {self.angular_velocity:>4}   ")
        sys.stdout.flush()



    def get_key(self):
        tty.setraw(sys.stdin.fileno())
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)
        return key

    def keyboard_listener(self):
        while True:
            try:
                key = self.get_key().lower()
                changed = False

                if key == 'x':
                    self.get_logger().info("Çıkış yapılıyor...")
                    rclpy.shutdown()
                    break
                elif key == ' ':
                    self.linear_velocity = 0
                    self.angular_velocity = 0
                    changed = True
                    self.get_logger().info("Tüm motorlar durduruldu")
                elif key == 'w':
                    self.linear_velocity = self.clamp(self.linear_velocity + 10)
                    changed = True
                elif key == 's':
                    self.linear_velocity = self.clamp(self.linear_velocity - 10)
                    changed = True
                elif key == 'a':
                    self.angular_velocity = self.clamp(self.angular_velocity - 10)
                    changed = True
                elif key == 'd':
                    self.angular_velocity = self.clamp(self.angular_velocity + 10)
                    changed = True

                if changed:
                    self.publish_motor_command()
                    self.print_motor_status()

            except Exception as e:
                self.get_logger().error(f"Klavye hatası: {e}")
                break

    def clamp(self, val, min_val=-100, max_val=100):
        return max(min_val, min(max_val, val))

    def publish_motor_command(self):
        if (self.linear_velocity != self.last_linear_velocity or
            self.angular_velocity != self.last_angular_velocity):
            
            msg = MotorControl()
            msg.linear_velocity = self.linear_velocity
            msg.angular_velocity = self.angular_velocity
            self.motor_pub_.publish(msg)

            self.last_linear_velocity = self.linear_velocity
            self.last_angular_velocity = self.angular_velocity

    def __del__(self):
        try:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)
        except:
            pass

def main(args=None):
    rclpy.init(args=args)
    node = KeyboardDriverNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
