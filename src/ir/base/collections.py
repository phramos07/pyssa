from user import User


# This class shouldn't be instantiated during SSA construction
class Collection(User):
	"""docstring for Collection"""
	def __init__(self, name=None, ctx=None, elements=[]):
		super(List, self).__init__(name)
		self.ctx = ctx
		self.elements = elements
		self.operands.extend(elements)

	@property
	def ctx(self):
		return self._ctx
	
	@ctx.setter
	def ctx(self, ctx):
		self._ctx = ctx
	
	def __repr__(self):
		_str = super(List, self).__repr__()
		_str += "[" + str(self.ctx) + "]"

		return "[" + _str + "]"
		

class List(Collection):
	"""docstring for List"""
	def __init__(self, name=None, ctx=None, elements=[]):
		super(List, self).__init__(name, ctx, elements)


class Tuple(Collection):
	"""docstring for Tuple"""
	def __init__(self, name=None, ctx=None, elements=[]):
		super(Tuple, self).__init__(name, ctx, elements)


class Set(User):
	"""docstring for Set"""
	def __init__(self, name=None, elements=[]):
		super(Set, self).__init__(name)
		self.elements = elements
		

class Dict(User):
	"""docstring for Dict"""
	def __init__(self, name=None, keys=[], values=[]):
		super(Dict, self).__init__(name)
		# These lists must be in matching order
		self.keys = keys
		self.values = values

	def __getitem__(self, i):
		return self.values[i]

	# TODO: Compact String representation of a DICT
	# def __repr__():
	# 	pass
