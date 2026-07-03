#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import TwistStamped
from nav_msgs.msg import Odometry

import math
import time


class DrawSquare(Node):

    def __init__(self):
        super().__init__('square_draw_node')

        # Publisher
        self.cmd_vel_pub = self.create_publisher(
            TwistStamped,
            '/cmd_vel',
            10
        )

        # Subscriber
        self.odom_sub = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10
        )

        # Current robot pose
        self.x = 0.0
        self.y = 0.0
        self.yaw = 0.0

        # Wait for odometry
        self.get_logger().info("Waiting for odometry...")
        rclpy.spin_once(self, timeout_sec=1.0)

        # Start drawing
        self.draw_square()

    # -----------------------------
    # Odometry Callback
    # -----------------------------
    def odom_callback(self, msg):

        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y

        q = msg.pose.pose.orientation

        # Quaternion -> Yaw
        siny_cosp = 2 * (q.w * q.z + q.x * q.y)
        cosy_cosp = 1 - 2 * (q.y * q.y + q.z * q.z)

        self.yaw = math.atan2(siny_cosp, cosy_cosp)

        print(
            f"Current Position -> "
            f"X = {self.x:.3f}, "
            f"Y = {self.y:.3f}, "
            f"Yaw = {math.degrees(self.yaw):.2f}°"
        )

    # -----------------------------
    # Move Robot
    # -----------------------------
    def move(self, linear, angular, duration):

        msg = TwistStamped()
        msg.twist.linear.x = linear
        msg.twist.angular.z = angular

        end_time = time.time() + duration

        while time.time() < end_time:

            self.cmd_vel_pub.publish(msg)

            # Process subscriber callback
            rclpy.spin_once(self, timeout_sec=0.01)

            time.sleep(0.1)

        self.stop()

    # -----------------------------
    # Stop Robot
    # -----------------------------
    def stop(self):

        stop_msg = TwistStamped()

        self.cmd_vel_pub.publish(stop_msg)

        time.sleep(0.5)

    # -----------------------------
    # Draw Square
    # -----------------------------
    def draw_square(self):

        for i in range(4):

            self.get_logger().info(f"Moving Side {i+1}")

            # Move Straight
            self.move(
                linear=0.1,
                angular=0.0,
                duration=2.0
            )

            self.get_logger().info(
                f"Reached Corner {i+1} -> "
                f"X={self.x:.3f}, "
                f"Y={self.y:.3f}"
            )

            # Rotate 90 degrees
            self.move(
                linear=0.0,
                angular=1.57,
                duration=1.0
            )

        self.get_logger().info("Square Completed")


def main(args=None):

    rclpy.init(args=args)

    node = DrawSquare()

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()