from source.formats.base.basic import fmt_member
from generated.context import ContextReference


class BufferPresence:

	"""
	in DLA and JWE2, this can be a dependency to a model2stream
	"""

	context = ContextReference()

	def __init__(self, context, arg=0, template=None, set_default=True):
		self.name = ''
		self._context = context
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0

		# -1 for a static buffer, 0 for streamed buffer; may be stream index
		self.pool_index = 0
		self.data_offset = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		self.pool_index = 0
		self.data_offset = 0

	def read(self, stream):
		self.io_start = stream.tell()
		self.read_fields(stream, self)
		self.io_size = stream.tell() - self.io_start

	def write(self, stream):
		self.io_start = stream.tell()
		self.write_fields(stream, self)
		self.io_size = stream.tell() - self.io_start

	@classmethod
	def read_fields(cls, stream, instance):
		instance.pool_index = stream.read_int()
		instance.data_offset = stream.read_int()

	@classmethod
	def write_fields(cls, stream, instance):
		stream.write_int(instance.pool_index)
		stream.write_int(instance.data_offset)

	@classmethod
	def from_stream(cls, stream, context, arg=0, template=None):
		instance = cls(context, arg, template, set_default=False)
		instance.io_start = stream.tell()
		cls.read_fields(stream, instance)
		instance.io_size = stream.tell() - instance.io_start
		return instance

	@classmethod
	def to_stream(cls, stream, instance):
		instance.io_start = stream.tell()
		cls.write_fields(stream, instance)
		instance.io_size = stream.tell() - instance.io_start
		return instance

	def get_info_str(self, indent=0):
		return f'BufferPresence [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += f'\n	* pool_index = {fmt_member(self.pool_index, indent+1)}'
		s += f'\n	* data_offset = {fmt_member(self.data_offset, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
