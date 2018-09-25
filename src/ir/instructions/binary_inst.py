from opcodes import INST_OP_CODE
from instruction import Instruction


class BinaryInst(Instruction):
	"""docstring for BinaryInst"""
	def __init__(self, name=None, op_code=None, left_value=None, right_value=None):
		super(BinaryInst, self).__init__(name, op_code)
		self.operands.append(left_value)
		self.operands.append(right_value)

	@property
	def op_code(self):
		return self._op_code
	
	@property
	def left_value(self):
		return self._left_value
	
	@property
	def right_value(self):
		return self._right_value
	
	@op_code.setter
	def op_code(self, op):
		self._op_code = op

	@left_value.setter
	def left_value(self, lv):
		self._left_value = lv

	@right_value.setter
	def right_value(self, rv):
		self._right_value = rv

	def __eval__(self):
		if self.opcode is None or len(self.operands) < 2:
			return None

		left_value = self.operands[0]
		right_value = self.operands[1]

		if self.opcode == INST_OP_CODE.ADD:
			return left_value + right_value
		
		if self.opcode == INST_OP_CODE.SUB:
			return left_value - right_value
		
		if self.opcode == INST_OP_CODE.MULT:
			return left_value * right_value
		
		if self.opcode == INST_OP_CODE.DIV:
			return left_value / right_value
		
		if self.opcode == INST_OP_CODE.FLOOR_DIV:
			return left_value // right_value
		
		if self.opcode == INST_OP_CODE.MOD:
			return left_value % right_value
		
		if self.opcode == INST_OP_CODE.LEFT_SHIFT:
			return left_value << right_value
		
		if self.opcode == INST_OP_CODE.RIGHT_SHIFT:
			return left_value >> right_value
		
		if self.opcode == INST_OP_CODE.BIT_OR:
			return left_value | right_value
		
		if self.opcode == INST_OP_CODE.BIT_XOR:
			return left_value ^ right_value
		
		if self.opcode == INST_OP_CODE.BIT_AND:
			return left_value & right_value
		
		if self.opcode == INST_OP_CODE.OR:
			return left_value or right_value
		
		if self.opcode == INST_OP_CODE.IS:
			return left_value is right_value
		
		if self.opcode == INST_OP_CODE.IS_NOT:
			return left_value is not right_value
		
		if self.opcode == INST_OP_CODE.EQ:
			return left_value == right_value
		
		if self.opcode == INST_OP_CODE.NOT_EQ:
			return left_value != right_value
		
		if self.opcode == INST_OP_CODE.LT:
			return left_value < right_value
		
		if self.opcode == INST_OP_CODE.LTE:
			return left_value <= right_value
		
		if self.opcode == INST_OP_CODE.GT:
			return left_value > right_value
		
		if self.opcode == INST_OP_CODE.GTE:
			return left_value >= right_value
		
		if self.opcode == INST_OP_CODE.IN:
			return left_value in right_value
		
		if self.opcode == INST_OP_CODE.NOT_IN:
			return left_value not in right_value

	def __repr__(self):
		_str = self.super(BinaryInst, self).__repr__()
		_str += "[" + str(self.name) + " = " + str(self.left_value) + \
			" " str(self.opcode) + " " + str(self.right_value) + "]"

		return _str
