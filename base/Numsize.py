

class Numsize(object):

    def __init__(self, x, n):

        """

        :param x: bite[]
        :param n: int
        """
        self.x = x
        self.n = n-1
        self.value = 0

        while True:
            if self.n != 0 and self.x[self.n] == 0:
                --self.n
            else:
                self.value = self.n+1
                break

    def __getattribute__(self, name):
        if(name=="value"):
            return object.__getattribute__(self, name)

        """
        while (n - - != 0 & & x[n] == 0)
            ;
            return n + 1;
           
        """
