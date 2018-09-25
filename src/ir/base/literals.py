from user import User


class FormattedValue(User):
	"""docstring for FormattedValue"""
	def __init__(self, name=None, value=None, conversion=None, format_spec=None):
		super(FormattedValue, self).__init__(name)
		self.value = value
		self.conversion = conversion
		self.format_spec = format_spec
		if value is not None:
			self.operands.append(value)

	@property
	def value(self):
		return self._value
	
	@property
	def conversion(self):
		return self._conversion
	
	@property
	def format_spec(self):
		return self._format_spec

	@value.setter
	def value(self, v):
		self._value = v

	@conversion.setter
	def conversion(self, conv):
		self._conversion = conv

	@format_spec.setter
	def format_spec(self, f_spec):
		self._format_spec = f_spec

	def __repr__(self):
		_str = super(FormattedValue, self).__repr__()
		_str += "[CONV:" str(self.conversion) + ", FORMAT:" str(format_spec) + "]"

		return "[" + _str + "]"


class JoinedString(User):
	"""docstring for JoinedString"""
	def __init__(self, name=None, values=[]):
		super(JoinedString, self).__init__(name)
		self.values = values
		self.operands.extend(values)


class EllipsisLiteral(User):
	"""docstring for Ellipsis"""
	def __init__(self, name=None):
		super(EllipsisLiteral, self).__init__(name)
		
	def __repr__(self):
		return "..."


