import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/tolgahan/pathron/pathron_ros2_ws/install/motor_controller'
