from source.formats.base.basic import fmt_member
import generated.formats.posedriverdef.compound.Driver
from generated.formats.ovl_base.compound.ArrayPointer import ArrayPointer
from generated.formats.ovl_base.compound.MemStruct import MemStruct


class PoseDriverDefRoot(MemStruct):

	def __init__(self, context, arg=0, template=None, set_default=True):
		self.name = ''
		super().__init__(context, arg, template, set_default)
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0
		self.count = 0
		self.drivers = ArrayPointer(self.context, self.count, generated.formats.posedriverdef.compound.Driver.Driver)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		self.count = 0
		self.drivers = ArrayPointer(self.context, self.count, generated.formats.posedriverdef.compound.Driver.Driver)

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
		super().read_fields(stream, instance)
		instance.drivers = ArrayPointer.from_stream(stream, instance.context, instance.count, generated.formats.posedriverdef.compound.Driver.Driver)
		instance.count = stream.read_uint64()
		instance.drivers.arg = instance.count

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		ArrayPointer.to_stream(stream, instance.drivers)
		stream.write_uint64(instance.count)

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
		return f'PoseDriverDefRoot [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* drivers = {fmt_member(self.drivers, indent+1)}'
		s += f'\n	* count = {fmt_member(self.count, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
