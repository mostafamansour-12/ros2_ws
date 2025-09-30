import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
from std_msgs.msg import String
from custom_message.msg import SensorProperties 
import random

class ValidatorNode(Node):
    def __init__(self):
        super().__init__('validatornode')
        self.msg = SensorProperties()
        self.ultradata = 0
        self.infradata = 0
        self.logger = self.get_logger()
        self.sub = self.create_subscription(Int64, '/ultrasonic_range', self.ultra_data, qos_profile=10)
        self.sub = self.create_subscription(Int64, '/infrared_range', self.infra_data, qos_profile=10)
        self.pub = self.create_publisher(SensorProperties, '/sensor_properties', qos_profile=10)
        self.timer = self.create_timer(0.1, self.run)

    def ultra_data(self, info):
        self.ultradata = info.data
        #self.logger.info(f'Subscribing: "{self.ultradata}"')

    def infra_data(self, info):
        self.infradata = info.data
        #self.logger.info(f'Subscribing: "{self.infradata}"')
        
    def run(self):
        self.msg.quality = random.randint(1,100)
        self.msg.sensor_values = f'Ultrasonic: {float(self.ultradata)}, Infrared: {float(self.infradata)}'
        self.logger.info(f'Quality: {self.msg.quality}, {self.msg.sensor_values}')


def main(args=None):
    rclpy.init(args=args)
    node = ValidatorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()