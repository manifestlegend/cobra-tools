from generated.formats.fgm.compound.FgmHeader import FgmHeader
from generated.formats.ovl_base.basic import ConvStream
from modules.formats.BaseFormat import MemStructLoader


class FgmLoader(MemStructLoader):
	target_class = FgmHeader
	extension = ".fgm"

	def create(self):
		super().create()
		# print(self.header)
		self.create_data_entry((self.update_names_buffer(),))

	@staticmethod
	def read_z_str(stream, pos):
		stream.seek(pos)
		return stream.read_zstring()

	def collect(self):
		super().collect()
		# self.header.debug_ptrs()
		self.get_names()
		# print(self.header)

	def get_names(self):
		"""Assigns names from the data buffer"""
		buffer_data = self.data_entry.buffer_datas[0]
		stream = ConvStream(buffer_data)
		self.header.shader_name = self.read_z_str(stream, 0)
		for arr in (self.header.attributes.data, self.header.textures.data):
			if arr:
				for member in arr:
					member.name = self.read_z_str(stream, member.offset)

	def update_names_buffer(self):
		"""Rewrites the name buffer and updates the offsets"""
		names_writer = ConvStream()
		# shader name is at 0
		names_writer.write_zstring(self.header.shader_name)
		names_writer.write(b"\x00")
		# attribs are written first
		for arr in (self.header.attributes.data, self.header.textures.data):
			if arr:
				for member in arr:
					member.offset = names_writer.tell()
					names_writer.write_zstring(member.name)
		return names_writer.getvalue()
