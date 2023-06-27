#Wall Follower Robot Code in Ghazebo Simulation and ROS Framework

def __init__(self):
		super().__init__('keys_to_twist')
		
		self.subscription_=self.create_subscription(LaserScan,'scan',self.listener_callback,10)
		self.subscription_
		self.publisher_=self.create_publisher(Twist, 'cmd_vel',10)
		
		
		
		
	def listener_callback(self,msg):
		mg=Twist()
		value1 = min(msg.ranges[0:18])
		value2 = msg.ranges[18]
		value3 = min(msg.ranges[18:35])
		
		if value2<=1.0:
			mg.linear.x=0.0
			mg.angular.z=0.0
				
		else:
			if value1<=1:
				mg.linear.x=1.0
				mg.angular.z=0.15
			elif value3<=1:
				mg.linear.x=1.0
				mg.angular.z=-0.15
			else:
				mg.linear.x=1.0
				mg.angular.z=0.0
		
		self.publisher_.publish(mg)
			
