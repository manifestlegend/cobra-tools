from source.formats.base.basic import fmt_member
from generated.bitfield import BasicBitfield
from generated.bitfield import BitfieldMember


class PixelFormatFlags(BasicBitfield):
	alpha_pixels = BitfieldMember(pos=0, mask=0x1, return_type=int)
	alpha = BitfieldMember(pos=1, mask=0x2, return_type=int)
	four_c_c = BitfieldMember(pos=2, mask=0x4, return_type=int)
	palette_indexed_4 = BitfieldMember(pos=3, mask=0x8, return_type=int)
	reserved_1 = BitfieldMember(pos=4, mask=0x10, return_type=int)
	palette_indexed_8 = BitfieldMember(pos=5, mask=0x20, return_type=int)
	rgb = BitfieldMember(pos=6, mask=0x40, return_type=int)
	reserved_2 = BitfieldMember(pos=7, mask=0x780, return_type=int)
	palette_indexed_1 = BitfieldMember(pos=11, mask=0x800, return_type=int)
	palette_indexed_2 = BitfieldMember(pos=12, mask=0x1000, return_type=int)
	reserved_3 = BitfieldMember(pos=13, mask=0x6000, return_type=int)
	alpha_premult = BitfieldMember(pos=15, mask=0x8000, return_type=int)
	reserved_4 = BitfieldMember(pos=16, mask=0x10000, return_type=int)
	luminance = BitfieldMember(pos=17, mask=0x20000, return_type=int)
	reserved_5 = BitfieldMember(pos=18, mask=0x7ffc0000, return_type=int)
	normal = BitfieldMember(pos=31, mask=0x80000000, return_type=int)

	def set_defaults(self):
		pass

	def read(self, stream):
		self._value = stream.read_uint()

	def write(self, stream):
		stream.write_uint(self._value)

	@classmethod
	def from_stream(cls, stream, context=None, arg=0, template=None):
		return cls.from_value(stream.read_uint())

	@classmethod
	def to_stream(cls, stream, instance):
		stream.write_uint(instance._value)
