#!/usr/bin/env python3
import rclpy
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TwistStamped
from nav_msgs.msg import Odometry
import time

class DrawSquare(Node):
    def __init__(self):
        super().__init__('square_draw_node')
        self.cmd_vel = self.create_publisher(TwistStamped, '/cmd_vel', 10)
        self.odometry = self.create_subscription(Odometry, '/odom', self.callback, 10)

    def callback(self, data):
        curr_position_x = round(data.pose.pose.position.x, 2)
        curr_position_y = round(data.pose.pose.position.y, 2)
        print(curr_position_x, curr_position_y)
        self.move(linear=0.1, angular=0.0, duration=5.0)

    def move(self, linear, angular, duration):
        msg = TwistStamped()
        msg.twist.linear.x = linear
        msg.twist.angular.z = angular
        self.cmd_vel.publish(msg)

def main():
    rclpy.init()
    node = DrawSquare()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()