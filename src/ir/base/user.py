from value import Value


class User(Value):
	"""docstring for User"""
	def __init__(self, name=None):
		super(User, self).__init__(name)
		self.operands = []

	def __repr__(self):
		_str = "[" + super(User, self).__repr__()

		if len(self.operands) > 0:
			_str += ", Operands: ["
			for op in self.operands:
				_str += str(op)
				_str += ", "
			_str += "]"

		return _str + "]"
