#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys
import select
import tty
import termios
import time
from pynput import keyboard
import p1pygame


timestep = 1
wheel_radius = 3.3 # r

track_width = 28.7 # L

# action_list = [[3.874630939427411, 0], [0, 3.874630939427411], [3.874630939427411, 0], [3.874630939427411, 3.874630939427411], [3.874630939427411, 3.874630939427411], [3.874630939427411, 7.853981633974483], [3.874630939427411, 0], [0, 3.874630939427411], [3.874630939427411, 0], [3.874630939427411, 3.874630939427411], [0, 3.874630939427411], [3.874630939427411, 3.874630939427411], [3.874630939427411, 3.874630939427411], [0, 3.874630939427411], [0, 3.874630939427411], [3.874630939427411, 0], [3.874630939427411, 3.874630939427411], [0, 3.874630939427411], [3.874630939427411, 3.874630939427411], [3.874630939427411, 3.874630939427411], [7.853981633974483, 3.874630939427411], [7.853981633974483, 3.874630939427411], [3.874630939427411, 3.874630939427411], [3.874630939427411, 3.874630939427411], [3.874630939427411, 0], [3.874630939427411, 0], [0, 3.874630939427411], [7.853981633974483, 3.874630939427411], [0, 3.874630939427411], [3.874630939427411, 0], [3.874630939427411, 3.874630939427411], [0, 3.874630939427411], [7.853981633974483, 0], [3.874630939427411, 3.874630939427411], [3.874630939427411, 3.874630939427411], [0, 3.874630939427411], [7.853981633974483, 7.853981633974483], [3.874630939427411, 7.853981633974483], [3.874630939427411, 3.874630939427411], [3.874630939427411, 3.874630939427411], [3.874630939427411, 7.853981633974483], [7.853981633974483, 7.853981633974483], [3.874630939427411, 3.874630939427411], [0, 3.874630939427411], [7.853981633974483, 3.874630939427411], [0, 3.874630939427411], [3.874630939427411, 0], [0, 3.874630939427411], [3.874630939427411, 0], [3.874630939427411, 3.874630939427411], [0, 3.874630939427411], [3.874630939427411, 0]]
# print(len(action_list))
# action_list.append([0,0])


# Define key codes
# LIN_VEL_STEP_SIZE = 0.1
# ANG_VEL_STEP_SIZE = 0.1

class KeyboardControlNode(Node):

    def __init__(self):
        super().__init__('keyboard_control_node')

        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)

        self.settings = termios.tcgetattr(sys.stdin)

    # def getKey(self):
    #     """Get the key that is pressed"""
    #     tty.setraw(sys.stdin.fileno())
    #     rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    #     if rlist:
    #         key = sys.stdin.read(1)
    #     else:
    #         key = ''

    #     termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)
    #     return key

    def run_keyboard_control(self):

        # self.get_logger().info(self.msg)
        velocity_message = Twist()
        linear_vel=0.0
        angular_vel=0.0


        for i,action in enumerate(action_list):
            # key = self.getKey()
            # if key is not None:
            #     if key == '\x1b':  # Escape key
            #         break
            #     elif key == 'q':  # Quit
            #         linear_vel=0.0
            #         angular_vel=0.0
            #     elif key == 'w':  # Forward
            #         linear_vel += LIN_VEL_STEP_SIZE
            #     elif key == 's':  # Reverse
            #         linear_vel -= LIN_VEL_STEP_SIZE
            #     elif key == 'd':  # Right
            #         angular_vel -= ANG_VEL_STEP_SIZE
            #     elif key == 'a':  # Left
            #         angular_vel += ANG_VEL_STEP_SIZE

                linear_vel_cm = (wheel_radius/2)*(action[0]+action[1])
                angular_vel_cm = (wheel_radius/track_width)*(action[1]-action[0])
                
                p_linear = 1
                p_angular = 1.05

                linear_vel = (linear_vel_cm/100)*p_linear
                angular_vel = (angular_vel_cm/1)*p_angular

                if angular_vel>0:
                        angular_vel= angular_vel*1
                if angular_vel<0:
                    angular_vel=angular_vel*1

                print("\nAction ",i)
                print("Steer Angle",angular_vel)
                print("Linear Velocity",linear_vel)
                
                # Publish the twist message
                velocity_message.linear.x = linear_vel
                velocity_message.angular.z = angular_vel
                
                self.cmd_vel_pub.publish(velocity_message)
                time.sleep(timestep)


def main(args=None):
    rclpy.init(args=args)
    node = KeyboardControlNode()
    node.run_keyboard_control()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()