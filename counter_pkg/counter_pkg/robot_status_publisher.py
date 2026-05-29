import rclpy
from rclpy.node import Node

from robot_interfaces.msg import RobotStatus

from rclpy.qos import QoSProfile
from rclpy.qos import ReliabilityPolicy
from rclpy.qos import HistoryPolicy
from rclpy.qos import DurabilityPolicy


class RobotStatusPublisher(Node):

    def __init__(self):

        super().__init__('robot_status_publisher')

        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.RELIABLE,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            history=HistoryPolicy.KEEP_LAST,
            depth=10
        )

        self.publisher_ = self.create_publisher(
            RobotStatus,
            'robot_status',
            qos_profile
        )

        self.timer = self.create_timer(
            1.0,
            self.publish_status
        )

        self.battery = 100.0

    def publish_status(self):

        msg = RobotStatus()

        msg.battery_pct = self.battery
        msg.mode = "AUTO"
        msg.error_code = 0

        self.publisher_.publish(msg)

        self.get_logger().info(
            f'Published -> '
            f'Battery={msg.battery_pct}, '
            f'Mode={msg.mode}, '
            f'Error={msg.error_code}'
        )

        self.battery -= 1.0

        if self.battery < 0:
            self.battery = 100.0


def main(args=None):

    rclpy.init(args=args)

    node = RobotStatusPublisher()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()