import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time


class DrawSquare(Node):

    def __init__(self):
        super().__init__('draw_square')

        self.publisher_ = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )

        time.sleep(1)

        self.draw_square()

    def move_forward(self, duration=2.0):

        msg = Twist()
        msg.linear.x = 2.0

        self.publisher_.publish(msg)

        self.get_logger().info("Moving Forward")

        time.sleep(duration)

    def turn_left(self, duration=1.0):

        msg = Twist()
        msg.angular.z = 1.57

        self.publisher_.publish(msg)

        self.get_logger().info("Turning Left")

        time.sleep(duration)

    def stop(self):

        msg = Twist()

        self.publisher_.publish(msg)

        time.sleep(0.2)

    def draw_square(self):

        for i in range(4):

            self.get_logger().info(f"Side {i+1}")

            self.move_forward()

            self.stop()

            self.turn_left()

            self.stop()

        self.get_logger().info("Square Completed")


def main(args=None):

    rclpy.init(args=args)

    node = DrawSquare()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()