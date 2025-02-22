from source.formats.base.basic import fmt_member
from generated.bitfield import BasicBitfield
from generated.bitfield import BitfieldMember


class WeightsFlag(BasicBitfield):
	has_weights = BitfieldMember(pos=0, mask=0x1, return_type=bool)
	bone_index = BitfieldMember(pos=1, mask=0xfffe, return_type=int)

	def set_defaults(self):
		pass

	def read(self, stream):
		self._value = stream.read_ushort()

	def write(self, stream):
		stream.write_ushort(self._value)

	@classmethod
	def from_stream(cls, stream, context=None, arg=0, template=None):
		return cls.from_value(stream.read_ushort())

	@classmethod
	def to_stream(cls, stream, instance):
		stream.write_ushort(instance._value)
