import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/slok/autonoumous_pick-place_bot/install/robot_controller'