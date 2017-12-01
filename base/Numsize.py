

class Numsize(object):

    def __init__(self, x, n):

        """

        :param x: bite[]
        :param n: int
        """

        while True:
            if n is not 0 and x[n] is 0:
                --n
            else:
                return n+1

        """
        while (n - - != 0 & & x[n] == 0)
            ;
            return n + 1;
           
        """
