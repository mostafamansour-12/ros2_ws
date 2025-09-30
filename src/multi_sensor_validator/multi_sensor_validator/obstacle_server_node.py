import rclpy
from rclpy.node import Node
from custom_message.srv import CheckObstacle

class ObstacleServer(Node):
    def __init__(self):
        super().__init__('obstacle_server')
        self.srv = self.create_service(CheckObstacle, 'check_obstacle', self.check_obstacle_callback)

    def check_obstacle_callback(self, request, response):
        for val in request.sensor_values:
            if val < 50:
                response.obstacle_detected = True
                response.message = f"Obstacle detected at {val} cm"
                self.get_logger().info(response.message)
                return response

        response.obstacle_detected = False
        response.message = "Path is clear"
        self.get_logger().info(response.message)
        return response

def main(args=None):
    rclpy.init(args=args)
    node = ObstacleServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()