import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
from multi_sensor_validator.Ultrasonic_Sensor import Ultrasonic

class InfraredNode(Node):
    def __init__(self):
        super().__init__('infrared_node')
        self.pub = self.create_publisher(Int64, 'infrared_range', qos_profile=10)
        self.ultrasonic = Ultrasonic()
        self.msg = Int64()
        self.timer = self.create_timer(0.1, self.run)

    def run(self):
        self.msg.data = self.ultrasonic.getDistance()
        self.pub.publish(self.msg)

def main(args=None):
    rclpy.init(args=args)
    node = InfraredNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()