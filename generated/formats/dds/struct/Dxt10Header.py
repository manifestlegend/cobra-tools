from source.formats.base.basic import fmt_member
from generated.context import ContextReference
from generated.formats.dds.enum.D3D10ResourceDimension import D3D10ResourceDimension
from generated.formats.dds.enum.DxgiFormat import DxgiFormat


class Dxt10Header:

	context = ContextReference()

	def __init__(self, context, arg=0, template=None, set_default=True):
		self.name = ''
		self._context = context
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0
		self.dxgi_format = DxgiFormat(self.context, 0, None)
		self.resource_dimension = D3D10ResourceDimension(self.context, 0, None)
		self.misc_flag = 0
		self.array_size = 0
		self.misc_flag_2 = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		self.dxgi_format = DxgiFormat(self.context, 0, None)
		self.resource_dimension = D3D10ResourceDimension(self.context, 0, None)
		self.misc_flag = 0
		self.array_size = 0
		self.misc_flag_2 = 0

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
		instance.dxgi_format = DxgiFormat.from_value(stream.read_uint())
		instance.resource_dimension = D3D10ResourceDimension.from_value(stream.read_uint())
		instance.misc_flag = stream.read_uint()
		instance.array_size = stream.read_uint()
		instance.misc_flag_2 = stream.read_uint()

	@classmethod
	def write_fields(cls, stream, instance):
		stream.write_uint(instance.dxgi_format.value)
		stream.write_uint(instance.resource_dimension.value)
		stream.write_uint(instance.misc_flag)
		stream.write_uint(instance.array_size)
		stream.write_uint(instance.misc_flag_2)

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
		return f'Dxt10Header [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += f'\n	* dxgi_format = {fmt_member(self.dxgi_format, indent+1)}'
		s += f'\n	* resource_dimension = {fmt_member(self.resource_dimension, indent+1)}'
		s += f'\n	* misc_flag = {fmt_member(self.misc_flag, indent+1)}'
		s += f'\n	* array_size = {fmt_member(self.array_size, indent+1)}'
		s += f'\n	* misc_flag_2 = {fmt_member(self.misc_flag_2, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
