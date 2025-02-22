from source.formats.base.basic import fmt_member
import generated.formats.wsm.compound.Vector3
import generated.formats.wsm.compound.Vector4
import numpy
from generated.formats.ovl_base.compound.ArrayPointer import ArrayPointer
from generated.formats.ovl_base.compound.MemStruct import MemStruct


class WsmHeader(MemStruct):

	"""
	56 bytes for JWE2
	"""

	def __init__(self, context, arg=0, template=None, set_default=True):
		self.name = ''
		super().__init__(context, arg, template, set_default)
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0
		self.duration = 0.0

		# likely
		self.frame_count = 0

		# unk
		self.unknowns = numpy.zeros((8,), dtype=numpy.dtype('float32'))
		self.locs = ArrayPointer(self.context, self.frame_count, generated.formats.wsm.compound.Vector3.Vector3)
		self.quats = ArrayPointer(self.context, self.frame_count, generated.formats.wsm.compound.Vector4.Vector4)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		self.duration = 0.0
		self.frame_count = 0
		self.unknowns = numpy.zeros((8,), dtype=numpy.dtype('float32'))
		self.locs = ArrayPointer(self.context, self.frame_count, generated.formats.wsm.compound.Vector3.Vector3)
		self.quats = ArrayPointer(self.context, self.frame_count, generated.formats.wsm.compound.Vector4.Vector4)

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
		instance.duration = stream.read_float()
		instance.frame_count = stream.read_uint()
		instance.unknowns = stream.read_floats((8,))
		instance.locs = ArrayPointer.from_stream(stream, instance.context, instance.frame_count, generated.formats.wsm.compound.Vector3.Vector3)
		instance.quats = ArrayPointer.from_stream(stream, instance.context, instance.frame_count, generated.formats.wsm.compound.Vector4.Vector4)
		instance.locs.arg = instance.frame_count
		instance.quats.arg = instance.frame_count

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		stream.write_float(instance.duration)
		stream.write_uint(instance.frame_count)
		stream.write_floats(instance.unknowns)
		ArrayPointer.to_stream(stream, instance.locs)
		ArrayPointer.to_stream(stream, instance.quats)

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
		return f'WsmHeader [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* duration = {fmt_member(self.duration, indent+1)}'
		s += f'\n	* frame_count = {fmt_member(self.frame_count, indent+1)}'
		s += f'\n	* unknowns = {fmt_member(self.unknowns, indent+1)}'
		s += f'\n	* locs = {fmt_member(self.locs, indent+1)}'
		s += f'\n	* quats = {fmt_member(self.quats, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
