import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class VelocityPublisher(Node):
    def __init__(self):
        super().__init__('velocity_publisher')
        self.publisher_ = self.create_publisher(Twist, '/model/simple_rover/cmd_vel', 10)
        self.timer = self.create_timer(1, self.publish_velocity)
        self.linear_velocity = 0.5 # m/s
        self.angular_velocity = 0.5  # rad/s

    def publish_velocity(self):
        msg = Twist()
        msg.linear.x = self.linear_velocity
        msg.angular.z = self.angular_velocity
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publishing: Linear={self.linear_velocity} Angular={self.angular_velocity}")

def main(args=None):
    rclpy.init(args=args)
    velocity_publisher = VelocityPublisher()
    rclpy.spin(velocity_publisher)
    velocity_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
