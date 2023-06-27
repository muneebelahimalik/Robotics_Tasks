#The robot normally drives in a straight line. 
#When the robot “sees” an obstacle in front within 0.8 meters, it will stop and turn to a new direction. 
#The turn is more than 90 degrees. The robot then resumes moving in the straight line. 
#This sequence is repeated.

from sensor_msgs.msg import LaserScan
import rclpy
import random
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys
import termios
import tty
import select


class MinimalPublisherSubscriber(Node):
	
	def __init__(self):
		super().__init__('keys_to_twist')
		
		self.subscription_=self.create_subscription(LaserScan,'scan',self.listener_callback,10)
		self.subscription_
		self.publisher_=self.create_publisher(Twist, 'cmd_vel',10)
		
		
		
		
	def listener_callback(self,msg):
		mg=Twist()
		value = msg.ranges[18]
		
		if value<=0.8:
			mg.linear.x=0.0
			mg.angular.z=3.0
		else:
			mg.linear.x=1.0
			mg.angular.z=0.0
		
		
		self.publisher_.publish(mg)
			
		
		
def main(args=None):
	rclpy.init (args=args)
	sub_pub = MinimalPublisherSubscriber()
	rclpy.spin(sub_pub)
	vel_pub.destroy_node ()
	rclpy.shutdown()
if __name__ =='__main__':
	main()
