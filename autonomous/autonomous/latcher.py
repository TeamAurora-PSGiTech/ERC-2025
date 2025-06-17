import rclpy
from rclpy.node import Node
from nav_msgs.msg import OccupancyGrid
from geometry_msgs.msg import TwistStamped
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy

class MapRepublisher(Node):
    def __init__(self):
        super().__init__('latched_map_republisher')
        qos = QoSProfile(
            depth=1,
            reliability=ReliabilityPolicy.RELIABLE,
            durability=DurabilityPolicy.TRANSIENT_LOCAL)
        self.pub = self.create_publisher(OccupancyGrid, '/map', qos)
        self.sub = self.create_subscription(OccupancyGrid, '/rtabmap/map', self.callback, 10)
        self.pub_cmd = self.create_publisher(TwistStamped, '/cmd_vel', 10)
        self.sub_cmd = self.create_subscription(TwistStamped, '/cmd_vel_smoothed', self.repub_cmd, 10)

    def callback(self, msg):
        self.pub.publish(msg)
    def repub_cmd(self, msg):
        msg.twist.linear.x *= 30.0/2
        msg.twist.angular.z *= 10.526315789473685/2
        self.pub_cmd.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MapRepublisher()
    rclpy.spin(node)
    rclpy.shutdown()
