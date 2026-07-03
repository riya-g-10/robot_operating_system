#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class DrawSquare(Node):
    def __init__(self):
        super().__init__('square_draw_node')
        self.cmd_vel=self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.draw_square()

    def move(self, linear, angular, duration):
        msg = Twist()
        msg.linear.x = linear
        msg.angular.z = angular
        end_time = time.time() + duration
        while time.time() < end_time:
            self.cmd_vel.publish(msg)
            time.sleep(0.1)
        self.stop()

    def stop(self):
        self.cmd_vel.publish(Twist())
        time.sleep(0.1)

    def draw_square(self):
        for _ in range(4):
            self.move(linear=2.0, angular=0.0, duration=2.0)
            self.move(linear=0.0, angular=1.578, duration=1.0)

def main ():
    rclpy.init()
    node = DrawSquare()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
