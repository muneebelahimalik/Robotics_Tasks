#Displays whether the received value is a multiple of 3 or not

class MinimalSubscriber(Node):
	
	def __init__(self):
		super().__init__('task4')
		self.subscription=self.create_subscription(Int32,'random',self.listener_callback,10)
		self.subscription
	def listener_callback(self,msg):
		val=msg.data
		if val%3==0:
			self.get_logger().info("I'm getting "+str(val))
			self.get_logger().info("It is a multiple of 3 ")
		else:
			self.get_logger().info("I'm getting "+str(val))
			self.get_logger().info("It is not a multiple of 3 ")
