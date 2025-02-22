from source.formats.base.basic import fmt_member
from generated.context import ContextReference


class MaterialName:

	context = ContextReference()

	def __init__(self, context, arg=0, template=None, set_default=True):
		self.name = ''
		self._context = context
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0

		# index into ms2 names array
		self.name_index = 0

		# index into ms2 names array
		self.name_index = 0

		# unknown, nonzero in PZ flamingo juvenile, might be junk (padding)
		self.some_index = 0

		# unknown, nonzero in PZ flamingo juvenile, might be junk (padding)
		self.some_index = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		if self.context.version >= 47:
			self.name_index = 0
		if self.context.version <= 32:
			self.name_index = 0
		if self.context.version >= 47:
			self.some_index = 0
		if self.context.version <= 32:
			self.some_index = 0

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
		if instance.context.version >= 47:
			instance.name_index = stream.read_uint()
		if instance.context.version <= 32:
			instance.name_index = stream.read_ushort()
		if instance.context.version >= 47:
			instance.some_index = stream.read_uint()
		if instance.context.version <= 32:
			instance.some_index = stream.read_ushort()

	@classmethod
	def write_fields(cls, stream, instance):
		if instance.context.version >= 47:
			stream.write_uint(instance.name_index)
		if instance.context.version <= 32:
			stream.write_ushort(instance.name_index)
		if instance.context.version >= 47:
			stream.write_uint(instance.some_index)
		if instance.context.version <= 32:
			stream.write_ushort(instance.some_index)

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
		return f'MaterialName [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += f'\n	* name_index = {fmt_member(self.name_index, indent+1)}'
		s += f'\n	* some_index = {fmt_member(self.some_index, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
