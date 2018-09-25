from value import Value


class Num(Value):
	"""docstring for Num"""
	def __init__(self, name=None, num=None):
		super(Num, self).__init__(name)
		self.num = num
		
	@property
	def num(self):
		return self._num
	
	@num.setter
	def num(self, num):
		self._num = num

	def __repr__(self):
		return "[" + super(Num, self).__repr__() + "[{}]".format(str(self.num)) + "]"


class String(Value):
	"""docstring for String"""
	def __init__(self, name=None, string=None):
		super(String, self).__init__(name)
		self.string = string
		
	@property
	def string(self):
		return self._string
	
	@string.setter
	def string(self, st):
		self._string = st

	def __repr__(self):
		return "[" + super(String, self).__repr__() + "[{}]".format(str(self.string)) + "]"

