

class Numsize(object):

    def __init__(self, x, n):

        """

        :param x: bite[]
        :param n: int
        """
        self.x = x
        self.n = n

        self.run()

    def run(self):

        while True:
            if self.n is not 0 and self.x[self.n] is 0:
                --self.n
            else:
                return self.n+1

        """
        while (n - - != 0 & & x[n] == 0)
            ;
            return n + 1;
           
        """
