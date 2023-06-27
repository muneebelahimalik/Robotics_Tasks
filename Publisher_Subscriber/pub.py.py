class MinimalPublisher(Node):
	
	def __init__(self):
		super().__init__('task3')
		self.publisher_=self.create_publisher(Int32, 'values',10)
		self.i=random.randint(0,9)
		
		timer_period=0.5
		self.timer=self.create_timer(timer_period,self.timer_callback)
	def timer_callback(self):
		msg=Int32()
		msg.data=self.i
		self.publisher_.publish(msg)
		
		self.get_logger().info("I'm seding "+str(msg.data))
		self.i=random.randint(0,9)
