
"""
       try {
            if ((hex.length()&0x01) == 1)
                throw new NumberFormatException("Hex string length is not a multiple of 2");
            byte[] bytes = new byte[hex.length() / 2];
            for (int i = 0; i < bytes.length; i++) {
                int char1 = hex.charAt(i * 2);
                char1 = char1 > 0x60 ? char1 - 0x57 : char1 - 0x30;
                int char2 = hex.charAt(i * 2 + 1);
                char2 = char2 > 0x60 ? char2 - 0x57 : char2 - 0x30;
                if (char1 < 0 || char2 < 0 || char1 > 15 || char2 > 15)
                    throw new NumberFormatException("Invalid hex number: " + hex);
                bytes[i] = (byte)((char1 << 4) + char2);
            }
            return bytes;
        } catch (Exception exc) {
            Nxt.log.debug("Invalid hex string: '" + hex + "'");
            throw exc;
        }


"""

class ParseHexString(object):

    def __init__(self, hex):
        """

        """
        if not isinstance(hex, str):
            return None
        else:

            self.hex = hex
            self.listOfByte = None

        self.run()

    def run(self):

        if len(self.hex)&0x01 == 1:
            return None

        lbytes = []
        for i in range(0, len(self.hex), 2):
            op1, op2 = self.hex[i:i + 2]
            oop1 = ord(op1)
            oop2 = ord(op2)

            char1 = oop1 - 0x57 if oop1 > 0x60 else oop1 - 0x30
            char2 = oop2 - 0x57 if oop2 > 0x60 else oop2 - 0x30

            if (char1 < 0 or char2 < 0 or char1 > 15 or char2 > 15):
                print("Invalid hex number ",op1,op2)

            lbytes.append(((char1 << 4) + char2))

        #self.listOfByte = lbytes
        self.listOfByte = [(xi + 128) % 256 - 128 for xi in lbytes]

    def getData(self):
        return self.listOfByte
