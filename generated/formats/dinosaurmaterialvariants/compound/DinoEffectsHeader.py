from source.formats.base.basic import fmt_member
import generated.formats.ovl_base.basic
import numpy
from generated.formats.dinosaurmaterialvariants.compound.Vector3F import Vector3F
from generated.formats.ovl_base.compound.MemStruct import MemStruct
from generated.formats.ovl_base.compound.Pointer import Pointer


class DinoEffectsHeader(MemStruct):

	def __init__(self, context, arg=0, template=None, set_default=True):
		self.name = ''
		super().__init__(context, arg, template, set_default)
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0
		self.vec_0 = Vector3F(self.context, 0, None)
		self.vec_1 = Vector3F(self.context, 0, None)
		self.a = 0
		self.b = 0
		self.vec_2 = Vector3F(self.context, 0, None)
		self.vec_3 = Vector3F(self.context, 0, None)
		self.vec_4 = Vector3F(self.context, 0, None)
		self.c = 0
		self.d = 0
		self.e = 0.0
		self.f = 0.0
		self.g = 0
		self.floats = numpy.zeros((39,), dtype=numpy.dtype('float32'))
		self.d = 0
		self.e = 0.0
		self.fgm_name = Pointer(self.context, 0, generated.formats.ovl_base.basic.ZStringObfuscated)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		self.vec_0 = Vector3F(self.context, 0, None)
		self.vec_1 = Vector3F(self.context, 0, None)
		self.a = 0
		self.b = 0
		self.vec_2 = Vector3F(self.context, 0, None)
		self.vec_3 = Vector3F(self.context, 0, None)
		self.vec_4 = Vector3F(self.context, 0, None)
		self.c = 0
		self.d = 0
		self.e = 0.0
		self.f = 0.0
		self.g = 0
		self.floats = numpy.zeros((39,), dtype=numpy.dtype('float32'))
		self.d = 0
		self.e = 0.0
		self.fgm_name = Pointer(self.context, 0, generated.formats.ovl_base.basic.ZStringObfuscated)

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
		instance.fgm_name = Pointer.from_stream(stream, instance.context, 0, generated.formats.ovl_base.basic.ZStringObfuscated)
		instance.vec_0 = Vector3F.from_stream(stream, instance.context, 0, None)
		instance.vec_1 = Vector3F.from_stream(stream, instance.context, 0, None)
		instance.a = stream.read_uint()
		instance.b = stream.read_uint()
		instance.vec_2 = Vector3F.from_stream(stream, instance.context, 0, None)
		instance.vec_3 = Vector3F.from_stream(stream, instance.context, 0, None)
		instance.vec_4 = Vector3F.from_stream(stream, instance.context, 0, None)
		instance.c = stream.read_uint()
		instance.d = stream.read_uint()
		instance.e = stream.read_float()
		instance.f = stream.read_float()
		instance.g = stream.read_uint()
		instance.floats = stream.read_floats((39,))
		instance.d = stream.read_uint()
		instance.e = stream.read_float()
		instance.fgm_name.arg = 0

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Pointer.to_stream(stream, instance.fgm_name)
		Vector3F.to_stream(stream, instance.vec_0)
		Vector3F.to_stream(stream, instance.vec_1)
		stream.write_uint(instance.a)
		stream.write_uint(instance.b)
		Vector3F.to_stream(stream, instance.vec_2)
		Vector3F.to_stream(stream, instance.vec_3)
		Vector3F.to_stream(stream, instance.vec_4)
		stream.write_uint(instance.c)
		stream.write_uint(instance.d)
		stream.write_float(instance.e)
		stream.write_float(instance.f)
		stream.write_uint(instance.g)
		stream.write_floats(instance.floats)
		stream.write_uint(instance.d)
		stream.write_float(instance.e)

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
		return f'DinoEffectsHeader [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* fgm_name = {fmt_member(self.fgm_name, indent+1)}'
		s += f'\n	* vec_0 = {fmt_member(self.vec_0, indent+1)}'
		s += f'\n	* vec_1 = {fmt_member(self.vec_1, indent+1)}'
		s += f'\n	* a = {fmt_member(self.a, indent+1)}'
		s += f'\n	* b = {fmt_member(self.b, indent+1)}'
		s += f'\n	* vec_2 = {fmt_member(self.vec_2, indent+1)}'
		s += f'\n	* vec_3 = {fmt_member(self.vec_3, indent+1)}'
		s += f'\n	* vec_4 = {fmt_member(self.vec_4, indent+1)}'
		s += f'\n	* c = {fmt_member(self.c, indent+1)}'
		s += f'\n	* d = {fmt_member(self.d, indent+1)}'
		s += f'\n	* e = {fmt_member(self.e, indent+1)}'
		s += f'\n	* f = {fmt_member(self.f, indent+1)}'
		s += f'\n	* g = {fmt_member(self.g, indent+1)}'
		s += f'\n	* floats = {fmt_member(self.floats, indent+1)}'
		s += f'\n	* d = {fmt_member(self.d, indent+1)}'
		s += f'\n	* e = {fmt_member(self.e, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
