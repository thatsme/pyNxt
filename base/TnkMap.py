# -*- coding: utf-8 -*-

class tokenMap:
    def __init__(self, **response):

        """

        :param response:
        """

        self.index = 0

        for k,v in response.items():
            if isinstance(v,dict):
                self.__dict__[k] = tokenMap(**v)
            elif isinstance(v,list):
                for val, a in enumerate(v):
                    sval = str(val).zfill(4)
                    pointer = k + "_" + sval
                    if isinstance(a, str) or isinstance(a, int):
                        self.__dict__[pointer] = v
                    else:
                        self.__dict__[pointer] = tokenMap(**a)
            else:
                self.__dict__[k] = v

