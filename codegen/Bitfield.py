from .BaseClass import BaseClass
import logging


class Bitfield(BaseClass):

    def map_pos(self):
        """Generate position if it does not exist"""
        pos = 0
        for field in self.struct:
            num_bits = field.attrib.get("numbits")
            if num_bits:
                field.attrib["pos"] = str(pos)
                pos += int(num_bits)

    def get_mask(self):
        """Generate position if it does not exist"""
        for field in self.struct:

            if not field.attrib.get('mask'):
                if "numbits" in field.attrib:
                    num_bits = int(field.attrib["numbits"])
                elif "width" in field.attrib:
                    num_bits = int(field.attrib["width"])
                elif "bit" in field.attrib:
                    num_bits = 1
                    field.attrib["pos"] = field.attrib["bit"]
                    field.attrib["type"] = "bool"
                else:
                    raise AttributeError(f"Neither width, mask, bit or numbits are defined for {field.attrib['name']}")
                pos = int(field.attrib["pos"])

                mask = ~((~0) << (pos + num_bits)) & ((~0) << pos)
                field.attrib['mask'] = str(hex(mask))
            # else:
            #   print("old:", field.attrib['mask'])

    def write_storage_io_methods(self, f, storage, attr='self._value'):
        for method_type in ("read", "write"):
            self.write_line(f)
            self.write_line(f, 1, f"def {method_type}(self, stream):")
            if method_type == "read":
                self.write_line(f, 2, f"self._value = {self.parser.read_for_type(storage, 'self.context')}")
            elif method_type == "write":
                self.write_line(f, 2, f"{self.parser.write_for_type(storage, attr, 'self.context')}")

        self.write_line(f)
        self.write_line(f, 1, "@classmethod")
        self.write_line(f, 1, "def from_stream(cls, stream, context=None, arg=0, template=None):")
        self.write_line(f, 2, f"return cls.from_value({self.parser.read_for_type(storage, 'context')})")

        self.write_line(f)
        self.write_line(f, 1, "@classmethod")
        self.write_line(f, 1, "def to_stream(cls, stream, instance):")
        self.write_line(f, 2, f"{self.parser.write_for_type(storage, 'instance._value', 'context')}")
        # f.write(f"\n")

    def read(self):
        """Create a self.struct class"""
        super().read()
        self.imports.add("BasicBitfield")
        self.imports.add("BitfieldMember")
        self.class_basename = "BasicBitfield"

        # write to python file
        with open(self.out_file, "w", encoding=self.parser.encoding) as f:
            # write the header stuff
            super().write(f)
            self.map_pos()
            self.get_mask()
            for field in self.struct:
                field_name = field.attrib["name"]
                _, field_type = self.parser.map_type(field.attrib.get("type", "int"))
                # print(field_name, field_type)
                if field_type not in self.parser.builtin_literals:
                    field_type = f'{field_type}.from_value'
                # else:
                #     field_type = field_type.lower()
                f.write(f"\n\t{field_name} = BitfieldMember(pos={field.attrib['pos']}, mask={field.attrib['mask']}, return_type={field_type})")

            f.write("\n\n\tdef set_defaults(self):")
            defaults = []
            for field in self.struct:
                field_name = field.attrib["name"]
                field_type = field.attrib.get("type", "int")
                field_default = field.attrib.get("default")
                # write the field's default, if it exists
                if field_default:
                    # we have to check if the default is an enum default value, in which case it has to be a member of that enum
                    if self.parser.tag_dict[field_type.lower()] == "enum":
                        field_default = field_type+"."+field_default
                    defaults.append((field_name, field_default))
            if defaults:
                for field_name, field_default in defaults:
                    f.write(f"\n\t\tself.{field_name} = {field_default}")
            else:
                f.write(f"\n\t\tpass")

            storage = self.struct.attrib["storage"]
            self.write_storage_io_methods(f, storage)
            f.write(f"\n")

