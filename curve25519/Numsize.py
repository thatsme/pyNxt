

class Numsize(object):

    def __init__(self, x, n):

        """

        :param x: bite[]
        :param n: int
        """

        self.value = 0
        n -= 1
        while True:
            if n != 0 and x[n] == 0:
                n -= 1
            else:
                self.value = n+1
                break

    def __getattribute__(self, name):
        if(name=="value"):
            return object.__getattribute__(self, name)

        """
        while (n - - != 0 & & x[n] == 0)
            ;
            return n + 1;
           
        """
