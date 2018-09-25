class Value(object):
	def __init__(self, name=None):
		super(Value, self).__init__()
		self.name = name
		self.users = []
		self.uses = []
	
	@property
	def name(self):
		return self._name
	
	@name.setter
	def name(self, name):
		self._name = name

	def __repr__(self):
		return "[{}][{}]".format(self.__class__.__name__, str(self.name))
