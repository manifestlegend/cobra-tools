from source.formats.base.basic import fmt_member
import generated.formats.base.basic
import generated.formats.dinosaurmaterialvariants.compound.PatternArray
import generated.formats.ovl_base.basic
from generated.formats.ovl_base.compound.MemStruct import MemStruct
from generated.formats.ovl_base.compound.Pointer import Pointer


class DinoPatternsHeader(MemStruct):

	def __init__(self, context, arg=0, template=None, set_default=True):
		self.name = ''
		super().__init__(context, arg, template, set_default)
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0
		self.set_count = 0
		self.pattern_count = 0
		self.zero = 0
		self.fgm_name = Pointer(self.context, 0, generated.formats.ovl_base.basic.ZStringObfuscated)
		self.set_name = Pointer(self.context, 0, generated.formats.base.basic.ZString)
		self.patterns = Pointer(self.context, self.pattern_count, generated.formats.dinosaurmaterialvariants.compound.PatternArray.PatternArray)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		self.set_count = 0
		self.pattern_count = 0
		self.zero = 0
		self.fgm_name = Pointer(self.context, 0, generated.formats.ovl_base.basic.ZStringObfuscated)
		self.set_name = Pointer(self.context, 0, generated.formats.base.basic.ZString)
		self.patterns = Pointer(self.context, self.pattern_count, generated.formats.dinosaurmaterialvariants.compound.PatternArray.PatternArray)

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
		instance.set_count = stream.read_uint64()
		instance.set_name = Pointer.from_stream(stream, instance.context, 0, generated.formats.base.basic.ZString)
		instance.patterns = Pointer.from_stream(stream, instance.context, instance.pattern_count, generated.formats.dinosaurmaterialvariants.compound.PatternArray.PatternArray)
		instance.pattern_count = stream.read_uint64()
		instance.zero = stream.read_uint64()
		instance.fgm_name.arg = 0
		instance.set_name.arg = 0
		instance.patterns.arg = instance.pattern_count

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Pointer.to_stream(stream, instance.fgm_name)
		stream.write_uint64(instance.set_count)
		Pointer.to_stream(stream, instance.set_name)
		Pointer.to_stream(stream, instance.patterns)
		stream.write_uint64(instance.pattern_count)
		stream.write_uint64(instance.zero)

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
		return f'DinoPatternsHeader [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* fgm_name = {fmt_member(self.fgm_name, indent+1)}'
		s += f'\n	* set_count = {fmt_member(self.set_count, indent+1)}'
		s += f'\n	* set_name = {fmt_member(self.set_name, indent+1)}'
		s += f'\n	* patterns = {fmt_member(self.patterns, indent+1)}'
		s += f'\n	* pattern_count = {fmt_member(self.pattern_count, indent+1)}'
		s += f'\n	* zero = {fmt_member(self.zero, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
