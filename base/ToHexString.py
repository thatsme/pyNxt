
class ToHexString(object):

    def __init__(self, bytes):

        if not isinstance(bytes, list):
            return None
        else:
            self.bytes = bytes
            self.hexChars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
            self.string = None

        self.run()

    def run(self):
        blen = len(self.bytes)
        #chars =  [None] * blen *2
        chars =  []
        for i in range(blen):
            chars.append(self.hexChars[((self.bytes[i] >> 4) & 0xF)])
            chars.append(self.hexChars[(self.bytes[i] & 0xF)])
        self.string = "".join(chars)

    def getString(self):
        return self.string