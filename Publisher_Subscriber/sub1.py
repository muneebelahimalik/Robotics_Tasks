#Triples the received values and displays the result

class MinimalSubscriber(Node):
	
	def __init__(self):
		super().__init__('task4')
		self.subscription=self.create_subscription(Int32,'random',self.listener_callback,10)
		self.subscription
	def listener_callback(self,msg):
		val=msg.data	
		self.get_logger().info("I'm getting "+str(val*3))
