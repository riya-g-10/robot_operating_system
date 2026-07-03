import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
import math


class DrawStar(Node):
    def __init__(self):
        super().__init__('star_draw_node')
        self.cmd_vel = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        time.sleep(1)
        self.draw_star()

    def move(self, linear, angular, duration):
        msg = Twist()
        msg.linear.x = linear
        msg.angular.z = angular

        start = time.time()
        while time.time() - start < duration:
            self.cmd_vel.publish(msg)
            time.sleep(0.02)

        self.stop()

    def stop(self):
        self.cmd_vel.publish(Twist())
        time.sleep(0.1)

    def draw_star(self):
        self.get_logger().info("Drawing CLOSED star...")

        speed = 2.0
        edge_length_time = 2.0

        turn_speed = 2.0
        turn_angle = math.radians(144)
        turn_time = turn_angle / turn_speed

        # IMPORTANT FIX: reduce drift accumulation
        for i in range(5):
            self.move(speed, 0.0, edge_length_time)
            self.move(0.0, turn_speed, turn_time)

        # force stop
        self.cmd_vel.publish(Twist())
        self.get_logger().info("Star done.")


def main():
    rclpy.init()
    node = DrawStar()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()