from source.formats.base.basic import fmt_member
import generated.formats.base.basic
import generated.formats.matcol.compound.Attrib
import generated.formats.matcol.compound.Info
from generated.formats.ovl_base.compound.ArrayPointer import ArrayPointer
from generated.formats.ovl_base.compound.MemStruct import MemStruct
from generated.formats.ovl_base.compound.Pointer import Pointer


class LayerFrag(MemStruct):

	def __init__(self, context, arg=0, template=None, set_default=True):
		self.name = ''
		super().__init__(context, arg, template, set_default)
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0
		self.u_0 = 0
		self.u_1 = 0
		self.info_count = 0
		self.u_2 = 0
		self.u_3 = 0
		self.attrib_count = 0
		self.layer_name = Pointer(self.context, 0, generated.formats.base.basic.ZString)
		self.infos = ArrayPointer(self.context, self.info_count, generated.formats.matcol.compound.Info.Info)
		self.attribs = ArrayPointer(self.context, self.attrib_count, generated.formats.matcol.compound.Attrib.Attrib)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		self.u_0 = 0
		self.u_1 = 0
		self.info_count = 0
		self.u_2 = 0
		self.u_3 = 0
		self.attrib_count = 0
		self.layer_name = Pointer(self.context, 0, generated.formats.base.basic.ZString)
		self.infos = ArrayPointer(self.context, self.info_count, generated.formats.matcol.compound.Info.Info)
		self.attribs = ArrayPointer(self.context, self.attrib_count, generated.formats.matcol.compound.Attrib.Attrib)

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
		instance.layer_name = Pointer.from_stream(stream, instance.context, 0, generated.formats.base.basic.ZString)
		instance.u_0 = stream.read_uint64()
		instance.u_1 = stream.read_uint64()
		instance.infos = ArrayPointer.from_stream(stream, instance.context, instance.info_count, generated.formats.matcol.compound.Info.Info)
		instance.info_count = stream.read_uint64()
		instance.u_2 = stream.read_uint64()
		instance.u_3 = stream.read_uint64()
		instance.attribs = ArrayPointer.from_stream(stream, instance.context, instance.attrib_count, generated.formats.matcol.compound.Attrib.Attrib)
		instance.attrib_count = stream.read_uint64()
		instance.layer_name.arg = 0
		instance.infos.arg = instance.info_count
		instance.attribs.arg = instance.attrib_count

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Pointer.to_stream(stream, instance.layer_name)
		stream.write_uint64(instance.u_0)
		stream.write_uint64(instance.u_1)
		ArrayPointer.to_stream(stream, instance.infos)
		stream.write_uint64(instance.info_count)
		stream.write_uint64(instance.u_2)
		stream.write_uint64(instance.u_3)
		ArrayPointer.to_stream(stream, instance.attribs)
		stream.write_uint64(instance.attrib_count)

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
		return f'LayerFrag [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* layer_name = {fmt_member(self.layer_name, indent+1)}'
		s += f'\n	* u_0 = {fmt_member(self.u_0, indent+1)}'
		s += f'\n	* u_1 = {fmt_member(self.u_1, indent+1)}'
		s += f'\n	* infos = {fmt_member(self.infos, indent+1)}'
		s += f'\n	* info_count = {fmt_member(self.info_count, indent+1)}'
		s += f'\n	* u_2 = {fmt_member(self.u_2, indent+1)}'
		s += f'\n	* u_3 = {fmt_member(self.u_3, indent+1)}'
		s += f'\n	* attribs = {fmt_member(self.attribs, indent+1)}'
		s += f'\n	* attrib_count = {fmt_member(self.attrib_count, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
