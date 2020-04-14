import struct

class CreateBA(object):

    def __init__(self, n):

        self.run(n)

    def run(self, n):
        tmp = []
        for i in range(n):
            tmp.append(0x00)

        bytes = struct.pack("{}I".format(len(tmp)), *tmp)

        print(type(bytes))
        print(bytes[33])

        return bytes