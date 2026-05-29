import rclpy
from rclpy.node import Node

from robot_interfaces.msg import RobotStatus

from rclpy.qos import QoSProfile
from rclpy.qos import ReliabilityPolicy
from rclpy.qos import HistoryPolicy


class BestEffortSubscriber(Node):

    def __init__(self):

        super().__init__('best_effort_subscriber')

        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )

        self.subscription = self.create_subscription(
            RobotStatus,
            'robot_status',
            self.listener_callback,
            qos_profile
        )

    def listener_callback(self, msg):

        self.get_logger().info(
            f'[BEST_EFFORT] Battery={msg.battery_pct}'
        )


def main(args=None):

    rclpy.init(args=args)

    node = BestEffortSubscriber()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()