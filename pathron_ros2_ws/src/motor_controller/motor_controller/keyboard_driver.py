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
        self.motor_control_topic_ = self.create_publisher(MotorControl, "motor_control_topic", 10)
        
        # Motor hızları (0-255 arası)
        self.motor_speeds = {
            'front_left': 0,
            'front_right': 0,
            'rear_left': 0,
            'rear_right': 0
        }
        
        # Klavye ayarları
        self.settings = termios.tcgetattr(sys.stdin)
        
        # Timer ile sürekli mesaj yayınlama
        self.timer = self.create_timer(0.1, self.publish_motor_control)
        
        # Klavye dinleme thread'i
        self.keyboard_thread = threading.Thread(target=self.keyboard_listener)
        self.keyboard_thread.daemon = True
        self.keyboard_thread.start()
        
        self.get_logger().info("Keyboard Driver Node started!")
        self.print_instructions()
    
    def print_instructions(self):
        """Kullanım talimatlarını yazdır"""
        print("\n" + "="*50)
        print("KEYBOARD MOTOR CONTROL")
        print("="*50)
        print("W: İleri hareket (hız: 50)")
        print("S: Geri hareket (hız: 50)")
        print("A: Sola dönüş (hız: 50)")
        print("D: Sağa dönüş (hız: 50)")
        print("SPACE: Tüm motorları durdur")
        print("X: Çıkış")
        print("="*50)
        print("Mevcut motor hızları:")
        self.print_motor_status()
    
    def print_motor_status(self):
        """Motor durumunu yazdır"""
        print(f"FL: {self.motor_speeds['front_left']:3d} | FR: {self.motor_speeds['front_right']:3d}")
        print(f"RL: {self.motor_speeds['rear_left']:3d} | RR: {self.motor_speeds['rear_right']:3d}")
        print("-" * 20)
    
    def get_key(self):
        """Klavyeden tek tuş al"""
        tty.setraw(sys.stdin.fileno())
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)
        return key
    
    def keyboard_listener(self):
        """Klavye girişlerini dinle"""
        while True:
            try:
                key = self.get_key().lower()
                
                if key == 'x':
                    self.get_logger().info("Çıkış yapılıyor...")
                    rclpy.shutdown()
                    break
                elif key == ' ':  # SPACE
                    self.stop_all_motors()
                elif key == 'w':
                    self.move_forward()
                elif key == 's':
                    self.move_backward()
                elif key == 'a':
                    self.turn_left()
                elif key == 'd':
                    self.turn_right()
                
                # Motor durumunu göster
                self.print_motor_status()
                
            except Exception as e:
                self.get_logger().error(f"Klavye hatası: {e}")
                break
    
    def clamp_speed(self, speed):
        """Hız değerini 0-255 arasında sınırla"""
        return max(0, min(255, speed))
    
    def stop_all_motors(self):
        """Tüm motorları durdur"""
        for key in self.motor_speeds:
            self.motor_speeds[key] = 0
        self.get_logger().info("Tüm motorlar durduruldu")
    
    def move_forward(self):
        """İleri hareket - sabit hız 50"""
        for key in self.motor_speeds:
            self.motor_speeds[key] = 50
        self.get_logger().info("İleri hareket - hız: 50")
    
    def move_backward(self):
        """Geri hareket - sabit hız 50 (negatif yön)"""
        for key in self.motor_speeds:
            self.motor_speeds[key] = 50  # Geri için de pozitif değer, yön kontrolü donanımda yapılır
        self.get_logger().info("Geri hareket - hız: 50")
    
    def turn_left(self):
        """Sola dönüş - sabit hız 50"""
        self.motor_speeds['front_left'] = 0
        self.motor_speeds['rear_left'] = 0
        self.motor_speeds['front_right'] = 50
        self.motor_speeds['rear_right'] = 50
        self.get_logger().info("Sola dönüş - hız: 50")
    
    def turn_right(self):
        """Sağa dönüş - sabit hız 50"""
        self.motor_speeds['front_left'] = 50
        self.motor_speeds['rear_left'] = 50
        self.motor_speeds['front_right'] = 0
        self.motor_speeds['rear_right'] = 0
        self.get_logger().info("Sağa dönüş - hız: 50")
    
    def publish_motor_control(self):
        """Motor kontrol mesajını yayınla"""
        msg = MotorControl()
        msg.front_left = self.motor_speeds['front_left']
        msg.front_right = self.motor_speeds['front_right']
        msg.rear_left = self.motor_speeds['rear_left']
        msg.rear_right = self.motor_speeds['rear_right']
        
        self.motor_control_topic_.publish(msg)
    
    def __del__(self):
        """Destructor - terminal ayarlarını geri yükle"""
        try:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)
        except:
            pass


def main(args=None):
    rclpy.init(args=args)
    
    keyboard_driver = KeyboardDriverNode()
    
    try:
        rclpy.spin(keyboard_driver)
    except KeyboardInterrupt:
        pass
    finally:
        keyboard_driver.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
