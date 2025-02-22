

import logging

from source.formats.base.basic import fmt_member
from generated.context import ContextReference


class DataEntry:

	"""
	32 bytes
	"""

	context = ContextReference()

	def __init__(self, context, arg=0, template=None, set_default=True):
		self.name = ''
		self._context = context
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0

		# djb2 hash
		self.file_hash = 0

		# djb2 hash for extension
		self.ext_hash = 0

		# 1-based indexing into set_header.sets; 0 if data is not part of a set
		self.set_index = 0

		# number of buffers that should be read from list for this entry
		self.buffer_count = 0
		self.zero = 0

		# size of first buffer, in the case of the ms2 the size 1 is the size of the first two buffers together
		self.size_1 = 0

		# size of last buffer; tex and texstream have all size here
		self.size_2 = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		self.file_hash = 0
		if self.context.version >= 19:
			self.ext_hash = 0
		self.set_index = 0
		self.buffer_count = 0
		if self.context.version >= 19:
			self.zero = 0
		self.size_1 = 0
		self.size_2 = 0

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
		instance.file_hash = stream.read_uint()
		if instance.context.version >= 19:
			instance.ext_hash = stream.read_uint()
		instance.set_index = stream.read_ushort()
		instance.buffer_count = stream.read_ushort()
		if instance.context.version >= 19:
			instance.zero = stream.read_uint()
		instance.size_1 = stream.read_uint64()
		instance.size_2 = stream.read_uint64()

	@classmethod
	def write_fields(cls, stream, instance):
		stream.write_uint(instance.file_hash)
		if instance.context.version >= 19:
			stream.write_uint(instance.ext_hash)
		stream.write_ushort(instance.set_index)
		stream.write_ushort(instance.buffer_count)
		if instance.context.version >= 19:
			stream.write_uint(instance.zero)
		stream.write_uint64(instance.size_1)
		stream.write_uint64(instance.size_2)

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
		return f'DataEntry [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += f'\n	* file_hash = {fmt_member(self.file_hash, indent+1)}'
		s += f'\n	* ext_hash = {fmt_member(self.ext_hash, indent+1)}'
		s += f'\n	* set_index = {fmt_member(self.set_index, indent+1)}'
		s += f'\n	* buffer_count = {fmt_member(self.buffer_count, indent+1)}'
		s += f'\n	* zero = {fmt_member(self.zero, indent+1)}'
		s += f'\n	* size_1 = {fmt_member(self.size_1, indent+1)}'
		s += f'\n	* size_2 = {fmt_member(self.size_2, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s

	def update_data(self, datas):
		"""Load datas into this DataEntry's buffers, and update its size values according to an assumed pattern
		data : list of bytes object, each representing the data of one buffer for this data entry"""
		for buffer, data in zip(self.sorted_buffers, datas):
			buffer.update_data(data)
		# update data 0, 1 size
		# total = sum(len(d) for d in datas)
		if len(datas) == 1:
			self.size_1 = len(datas[0])
			self.size_2 = 0
		elif len(datas) == 2:
			self.size_1 = 0
			self.size_2 = sum(len(d) for d in datas)
		elif len(datas) > 2:
			self.size_1 = sum(len(d) for d in datas[:-1])
			self.size_2 = len(datas[-1])

	@property
	def sorted_buffers(self):
		"""Get buffers sorted by index"""
		return sorted(self.buffers, key=lambda buffer: buffer.index)

	@property
	def buffer_datas(self):
		"""Get data for each buffer"""
		return list(buffer.data for buffer in self.sorted_buffers)

	def __eq__(self, other):
		attr_check = ("buffer_count", "size_1", "size_2")
		same = True
		for attr in attr_check:
			a = getattr(self, attr)
			b = getattr(other, attr)
			if a != b:
				logging.warning(f"Data differs for '{attr}' - {a} vs {b}")
				same = False
		for i, (a, b) in enumerate(zip(self.sorted_buffers, other.sorted_buffers)):
			if a != b:
				logging.warning(f"Buffer {i} differs for {a} vs {b}")
				same = False
		return same

