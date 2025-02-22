from source.formats.base.basic import fmt_member
from generated.context import ContextReference


class Size:

	context = ContextReference()

	def __init__(self, context, arg=0, template=None, set_default=True):
		self.name = ''
		self._context = context
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0

		# index into name list
		self.id = 0
		self.width_1 = 0
		self.height_1 = 0
		self.width_2 = 0
		self.height_2 = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		self.id = 0
		self.width_1 = 0
		self.height_1 = 0
		self.width_2 = 0
		self.height_2 = 0

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
		instance.id = stream.read_uint64()
		instance.width_1 = stream.read_uint64()
		instance.height_1 = stream.read_uint64()
		instance.width_2 = stream.read_uint64()
		instance.height_2 = stream.read_uint64()

	@classmethod
	def write_fields(cls, stream, instance):
		stream.write_uint64(instance.id)
		stream.write_uint64(instance.width_1)
		stream.write_uint64(instance.height_1)
		stream.write_uint64(instance.width_2)
		stream.write_uint64(instance.height_2)

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
		return f'Size [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += f'\n	* id = {fmt_member(self.id, indent+1)}'
		s += f'\n	* width_1 = {fmt_member(self.width_1, indent+1)}'
		s += f'\n	* height_1 = {fmt_member(self.height_1, indent+1)}'
		s += f'\n	* width_2 = {fmt_member(self.width_2, indent+1)}'
		s += f'\n	* height_2 = {fmt_member(self.height_2, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
