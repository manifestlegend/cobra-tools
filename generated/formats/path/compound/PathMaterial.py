from source.formats.base.basic import fmt_member
import generated.formats.base.basic
import generated.formats.path.compound.PathMaterialData
from generated.formats.ovl_base.compound.ArrayPointer import ArrayPointer
from generated.formats.ovl_base.compound.MemStruct import MemStruct
from generated.formats.ovl_base.compound.Pointer import Pointer


class PathMaterial(MemStruct):

	def __init__(self, context, arg=0, template=None, set_default=True):
		self.name = ''
		super().__init__(context, arg, template, set_default)
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0
		self.path_sub_type = 0
		self.num_data = 0
		self.elevated_mat = Pointer(self.context, 0, generated.formats.base.basic.ZString)
		self.elevated_mat_valid = Pointer(self.context, 0, generated.formats.base.basic.ZString)
		self.elevated_mat_invalid = Pointer(self.context, 0, generated.formats.base.basic.ZString)
		self.terrain_mat = Pointer(self.context, 0, generated.formats.base.basic.ZString)
		self.terrain_mat_valid = Pointer(self.context, 0, generated.formats.base.basic.ZString)
		self.terrain_mat_invalid = Pointer(self.context, 0, generated.formats.base.basic.ZString)
		self.underside_mat_1 = Pointer(self.context, 0, generated.formats.base.basic.ZString)
		self.underside_mat_2 = Pointer(self.context, 0, generated.formats.base.basic.ZString)
		self.stairs_mat_1 = Pointer(self.context, 0, generated.formats.base.basic.ZString)
		self.stairs_mat_2 = Pointer(self.context, 0, generated.formats.base.basic.ZString)
		self.mat_data = ArrayPointer(self.context, self.num_data, generated.formats.path.compound.PathMaterialData.PathMaterialData)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		self.path_sub_type = 0
		self.num_data = 0
		self.elevated_mat = Pointer(self.context, 0, generated.formats.base.basic.ZString)
		self.elevated_mat_valid = Pointer(self.context, 0, generated.formats.base.basic.ZString)
		self.elevated_mat_invalid = Pointer(self.context, 0, generated.formats.base.basic.ZString)
		self.terrain_mat = Pointer(self.context, 0, generated.formats.base.basic.ZString)
		self.terrain_mat_valid = Pointer(self.context, 0, generated.formats.base.basic.ZString)
		self.terrain_mat_invalid = Pointer(self.context, 0, generated.formats.base.basic.ZString)
		self.underside_mat_1 = Pointer(self.context, 0, generated.formats.base.basic.ZString)
		self.underside_mat_2 = Pointer(self.context, 0, generated.formats.base.basic.ZString)
		self.stairs_mat_1 = Pointer(self.context, 0, generated.formats.base.basic.ZString)
		self.stairs_mat_2 = Pointer(self.context, 0, generated.formats.base.basic.ZString)
		self.mat_data = ArrayPointer(self.context, self.num_data, generated.formats.path.compound.PathMaterialData.PathMaterialData)

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
		instance.elevated_mat = Pointer.from_stream(stream, instance.context, 0, generated.formats.base.basic.ZString)
		instance.elevated_mat_valid = Pointer.from_stream(stream, instance.context, 0, generated.formats.base.basic.ZString)
		instance.elevated_mat_invalid = Pointer.from_stream(stream, instance.context, 0, generated.formats.base.basic.ZString)
		instance.terrain_mat = Pointer.from_stream(stream, instance.context, 0, generated.formats.base.basic.ZString)
		instance.terrain_mat_valid = Pointer.from_stream(stream, instance.context, 0, generated.formats.base.basic.ZString)
		instance.terrain_mat_invalid = Pointer.from_stream(stream, instance.context, 0, generated.formats.base.basic.ZString)
		instance.underside_mat_1 = Pointer.from_stream(stream, instance.context, 0, generated.formats.base.basic.ZString)
		instance.underside_mat_2 = Pointer.from_stream(stream, instance.context, 0, generated.formats.base.basic.ZString)
		instance.stairs_mat_1 = Pointer.from_stream(stream, instance.context, 0, generated.formats.base.basic.ZString)
		instance.stairs_mat_2 = Pointer.from_stream(stream, instance.context, 0, generated.formats.base.basic.ZString)
		instance.path_sub_type = stream.read_uint64()
		instance.mat_data = ArrayPointer.from_stream(stream, instance.context, instance.num_data, generated.formats.path.compound.PathMaterialData.PathMaterialData)
		instance.num_data = stream.read_uint64()
		instance.elevated_mat.arg = 0
		instance.elevated_mat_valid.arg = 0
		instance.elevated_mat_invalid.arg = 0
		instance.terrain_mat.arg = 0
		instance.terrain_mat_valid.arg = 0
		instance.terrain_mat_invalid.arg = 0
		instance.underside_mat_1.arg = 0
		instance.underside_mat_2.arg = 0
		instance.stairs_mat_1.arg = 0
		instance.stairs_mat_2.arg = 0
		instance.mat_data.arg = instance.num_data

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Pointer.to_stream(stream, instance.elevated_mat)
		Pointer.to_stream(stream, instance.elevated_mat_valid)
		Pointer.to_stream(stream, instance.elevated_mat_invalid)
		Pointer.to_stream(stream, instance.terrain_mat)
		Pointer.to_stream(stream, instance.terrain_mat_valid)
		Pointer.to_stream(stream, instance.terrain_mat_invalid)
		Pointer.to_stream(stream, instance.underside_mat_1)
		Pointer.to_stream(stream, instance.underside_mat_2)
		Pointer.to_stream(stream, instance.stairs_mat_1)
		Pointer.to_stream(stream, instance.stairs_mat_2)
		stream.write_uint64(instance.path_sub_type)
		ArrayPointer.to_stream(stream, instance.mat_data)
		stream.write_uint64(instance.num_data)

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
		return f'PathMaterial [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* elevated_mat = {fmt_member(self.elevated_mat, indent+1)}'
		s += f'\n	* elevated_mat_valid = {fmt_member(self.elevated_mat_valid, indent+1)}'
		s += f'\n	* elevated_mat_invalid = {fmt_member(self.elevated_mat_invalid, indent+1)}'
		s += f'\n	* terrain_mat = {fmt_member(self.terrain_mat, indent+1)}'
		s += f'\n	* terrain_mat_valid = {fmt_member(self.terrain_mat_valid, indent+1)}'
		s += f'\n	* terrain_mat_invalid = {fmt_member(self.terrain_mat_invalid, indent+1)}'
		s += f'\n	* underside_mat_1 = {fmt_member(self.underside_mat_1, indent+1)}'
		s += f'\n	* underside_mat_2 = {fmt_member(self.underside_mat_2, indent+1)}'
		s += f'\n	* stairs_mat_1 = {fmt_member(self.stairs_mat_1, indent+1)}'
		s += f'\n	* stairs_mat_2 = {fmt_member(self.stairs_mat_2, indent+1)}'
		s += f'\n	* path_sub_type = {fmt_member(self.path_sub_type, indent+1)}'
		s += f'\n	* mat_data = {fmt_member(self.mat_data, indent+1)}'
		s += f'\n	* num_data = {fmt_member(self.num_data, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
