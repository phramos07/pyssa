import sys
sys.path.append("../base/")
from user import User


class Instruction(User):
	"""docstring for Instruction"""
	def __init__(self, name=None, op_code=None):
		super(Instruction, self).__init__(name)
		self.op_code = op_code

	def __eval__(self):
		pass

	def __repr__(self):
		pass
