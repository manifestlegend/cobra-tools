from source.formats.base.basic import fmt_member
from generated.context import ContextReference


class SizedStrData:

	"""
	24 bytes for DLA, ZTUAC, PC, JWE1, old PZ
	32 bytes for PZ1.6+, JWFloatCount
	"""

	context = ContextReference()

	def __init__(self, context, arg=0, template=None, set_default=True):
		self.name = ''
		self._context = context
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0

		# seemingly related to the names of mani files stripped from their prefix, but usually slightly smaller than what is actually needed
		self.names_size = 0
		self.hash_block_size = 0
		self.zero_0 = 0

		# haven't seen this one actually used, may be wrong
		self.count = 0
		self.zero_1 = 0
		self.zero_2 = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		self.names_size = 0
		self.hash_block_size = 0
		self.zero_0 = 0
		self.count = 0
		self.zero_1 = 0
		if self.context.version >= 20:
			self.zero_2 = 0

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
		instance.names_size = stream.read_ushort()
		instance.hash_block_size = stream.read_ushort()
		instance.zero_0 = stream.read_uint64()
		instance.count = stream.read_uint()
		instance.zero_1 = stream.read_uint64()
		if instance.context.version >= 20:
			instance.zero_2 = stream.read_uint64()

	@classmethod
	def write_fields(cls, stream, instance):
		stream.write_ushort(instance.names_size)
		stream.write_ushort(instance.hash_block_size)
		stream.write_uint64(instance.zero_0)
		stream.write_uint(instance.count)
		stream.write_uint64(instance.zero_1)
		if instance.context.version >= 20:
			stream.write_uint64(instance.zero_2)

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
		return f'SizedStrData [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += f'\n	* names_size = {fmt_member(self.names_size, indent+1)}'
		s += f'\n	* hash_block_size = {fmt_member(self.hash_block_size, indent+1)}'
		s += f'\n	* zero_0 = {fmt_member(self.zero_0, indent+1)}'
		s += f'\n	* count = {fmt_member(self.count, indent+1)}'
		s += f'\n	* zero_1 = {fmt_member(self.zero_1, indent+1)}'
		s += f'\n	* zero_2 = {fmt_member(self.zero_2, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
