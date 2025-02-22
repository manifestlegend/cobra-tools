from source.formats.base.basic import fmt_member
from generated.context import ContextReference


class AkMediaInformation:

	context = ContextReference()

	def __init__(self, context, arg=0, template=None, set_default=True):
		self.name = ''
		self._context = context
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0
		self.source_i_d = 0
		self.u_in_memory_media_size = 0
		self.u_source_bits = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		self.source_i_d = 0
		self.u_in_memory_media_size = 0
		self.u_source_bits = 0

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
		instance.source_i_d = stream.read_uint()
		instance.u_in_memory_media_size = stream.read_uint()
		instance.u_source_bits = stream.read_ubyte()

	@classmethod
	def write_fields(cls, stream, instance):
		stream.write_uint(instance.source_i_d)
		stream.write_uint(instance.u_in_memory_media_size)
		stream.write_ubyte(instance.u_source_bits)

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
		return f'AkMediaInformation [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += f'\n	* source_i_d = {fmt_member(self.source_i_d, indent+1)}'
		s += f'\n	* u_in_memory_media_size = {fmt_member(self.u_in_memory_media_size, indent+1)}'
		s += f'\n	* u_source_bits = {fmt_member(self.u_source_bits, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
