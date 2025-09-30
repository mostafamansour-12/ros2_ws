import rclpy
from rclpy.node import Node
from custom_message.msg import SensorProperties

class LoggerNode(Node):
    def __init__(self):
        super().__init__('logger_node')
        self.subscription = self.create_subscription(
            SensorProperties, 'sensor_properties', self.listener_callback, 10)

    def listener_callback(self, msg):
        self.get_logger().info(f"Received sensor properties: {msg.sensor_values}")
        if msg.quality >= 50:
            readings = ", ".join([f"{s.range:.2f} cm" for s in msg.sensor_values])
            self.get_logger().info(f"Quality = {msg.quality} → {readings}")
        else:
            self.get_logger().info("Quality rejected.")

def main(args=None):
    rclpy.init(args=args)
    node = LoggerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()