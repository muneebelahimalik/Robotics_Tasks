def __init__(self):
		super().__init__('keys_to_twist')
		
		self.subscription_=self.create_subscription(LaserScan,'scan',self.listener_callback,10)
		self.subscription_
		self.publisher_=self.create_publisher(Twist, 'cmd_vel',10)
		
		
		
		
	def listener_callback(self,msg):
		mg=Twist()
		x=len(msg.ranges)
		max_distance=10
		
		# Region 1
		value1 = min(min(msg.ranges[0:7]),max_distance)
		print("Range of region 1: " , value1)
		
		# Region 2
		value2= min(min(msg.ranges[7:14]),max_distance)
		print("Range of region 2: " , value2)
		
		# Region 3
		value3 = min(min(msg.ranges[14:21]),max_distance)
		print("Range of region 3: " , value3)
		
		# Region 4
		value4 = min(min(msg.ranges[21:28]),max_distance)
		print("Range of region 4: " , value4)
		
		# Region 5
		value5 = min(min(msg.ranges[28:35]),max_distance)
		print("Range of region 5: " , value5,"\n")
		
		
		self.publisher_.publish(mg)
