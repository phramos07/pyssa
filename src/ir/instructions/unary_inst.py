from opcodes import INST_OP_CODE
from instruction import Instruction


class UnaryInst(Instruction):
	def __init__(self, name=None, op_code=None, value=None):
		super(UnaryInst, self).__init__(name, op_code)
		self.operands.append(value)

	@property
	def op_code(self):
		return self._op_code
	
	@property
	def value(self):
		return self._value
	
	@op_code.setter
	def op_code(self, op):
		self._op_code = op

	@value.setter
	def value(self, lv):
		self._value = lv

	def __eval__(self):
		if self.opcode is None or len(self.operands) < 1:
			return None

		value = self.operands[0]

		if self.opcode == INST_OP_CODE.ADD:
			return value
		
		if self.opcode == INST_OP_CODE.SUB:
			return - value
		
		if self.opcode == INST_OP_CODE.NOT:
			return not value
		
		if self.opcode == INST_OP_CODE.INVERT:
			return ~ value

	def __repr__(self):
		_str = self.super(UnaryInst, self).__repr__()
		_str += "[" + str(self.name) + " = " str(self.opcode) + " " + str(self.value) + "]"

		return _str

