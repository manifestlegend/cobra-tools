from source.formats.base.basic import fmt_member
from generated.bitfield import BasicBitfield
from generated.bitfield import BitfieldMember
from generated.formats.ovl_base.enum.Compression import Compression


class VersionInfo(BasicBitfield):

	"""
	Determines the format of the OVL file.
	n.b. pos counts from the end!
	# compression                         __ _
	# pc/pz uncompressed	8212	00100000 00010100
	# pc/pz zlib			8340	00100000 10010100
	# pc/pz oodle			8724	00100010 00010100
	
	# JWE (uncomp)	        24596	01100000 00010100
	# JWE zlib				24724	01100000 10010100
	# JWE oodle (switch)	25108	01100010 00010100
	"""
	unk_1 = BitfieldMember(pos=2, mask=0x4, return_type=bool)
	unk_2 = BitfieldMember(pos=4, mask=0x10, return_type=bool)
	compression = BitfieldMember(pos=7, mask=0x380, return_type=Compression.from_value)
	unk_3 = BitfieldMember(pos=13, mask=0x2000, return_type=bool)
	is_jwe = BitfieldMember(pos=14, mask=0x4000, return_type=bool)

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
