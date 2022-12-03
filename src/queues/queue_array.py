class QueueArray:
	def __init__(self):
		self.queue = list()
		
	def __isNone__(self, data):
		return data == None
	def getSize(self):
		return len(self.queue)
	def isEmpty(self):
		return self.getSize() == 0
	def enqueue(self, data):
		if not self.__isNone__(data):
			self.queue.append(data)
		raise ValueError("Data is empty")
	
	def dequeue(self):
		if not self.isEmpty():
			 return self.queue.pop(0)
		raise ValueError("Can not deqeue from empty queue")