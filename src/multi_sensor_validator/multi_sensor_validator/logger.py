import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class LoggerNode(Node):
    def __init__(self):
        super().__init__('logger_node')
        self.msg = String()
        self.logger = self.get_logger()
        self.sub = self.create_subscription(String, '/validation_result', self.callback, qos_profile=10)

    def callback(self, info):
        self.sub_msg = info.data
        # print(data)
        self.logger.info(f'Subscribing: "{self.sub_msg}"')


def main(args=None):
    rclpy.init(args=args)
    node = LoggerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()