import base.Add as add
import base.Sub as sub


class Mont_Prep(object):

    def __init__(self, t1, t2, ax, az):
        """
        y^2 = x^3 + 486662 x^2 + x  over GF(2^255-19)

        t1 = ax + az
        t2 = ax - az  */
        :param t1: Long10
        :param t2: Long10
        :param ax: Long10
        :param az: Long10
        """

        add(t1, ax, az);
        sub(t2, ax, az);


