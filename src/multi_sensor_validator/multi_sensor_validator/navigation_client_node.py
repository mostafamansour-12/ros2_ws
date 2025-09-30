import rclpy
from rclpy.node import Node
from custom_message.srv import CheckObstacle
import random

class NavigationClient(Node):
    def __init__(self):
        super().__init__('navigation_client')
        self.client = self.create_client(CheckObstacle, 'check_obstacle')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Service not available, waiting...")
        self.send_request()

    def send_request(self):
        request = CheckObstacle.Request()
        request.sensor_values = [random.randint(10, 200), random.randint(10, 200)]
        self.future = self.client.call_async(request)
        self.future.add_done_callback(self.response_callback)

    def response_callback(self, future):
        try:
            response = future.result()
            self.get_logger().info(f"Response: {response.message}")
        except Exception as e:
            self.get_logger().error(f"Service call failed {e}")

def main(args=None):
    rclpy.init(args=args)
    node = NavigationClient()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()