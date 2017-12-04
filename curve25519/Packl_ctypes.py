import struct
import ctypes

PyLong_AsByteArray = ctypes.pythonapi._PyLong_AsByteArray
PyLong_AsByteArray.argtypes = [ctypes.py_object,
                               ctypes.c_char_p,
                               ctypes.c_size_t,
                               ctypes.c_int,
                               ctypes.c_int]

class Packl_ctypes(object):

    def __init__(self,lnum):
        self.value = None

        a = ctypes.create_string_buffer(lnum.bit_length()//8 + 1)
        PyLong_AsByteArray(lnum, a, len(a), 0, 1)
        #for a1 in a:
        #    print(struct.unpack('b', a1))
        #print(struct.unpack('b', a[-1]))
        b = struct.unpack('b', a[-1])
        self.value = b[0]

    def __getattribute__(self, name):
        if(name=="value"):
            return object.__getattribute__(self, name)

