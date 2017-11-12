from base.BaseGet import BaseGet as Parent

class GetAccountCurrenciesByIssuer(Parent):

    ## Multiaccount parameters (3)
    def __init__(self):

        super(GetAccountCurrenciesByIssuer, self).__init__(rt = "getAccountCurrenciesByIssuer")

    def run(self):
        super(GetAccountCurrenciesByIssuer, self).run()               # calls 'BaseGet.run()'

    def getData(self, key=None):
        return super(GetAccountCurrenciesByIssuer, self).getData(key)    # calls 'BaseGet.getData()'