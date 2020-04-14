import accounts.getAccount as ac
import accounts.sendMoney as sm
from inspect import getdoc

import base.BaseGet as bg

myAc = ac.GetAccount()

#print(ac.__doc__)
#print(myAc.__init__.__doc__)
#print(myAc.run.__doc__)
#print(myAc.getData.__doc__)

mySm = sm.SendMoney()

print(mySm.__init__.__doc__)
print(mySm.run.__doc__)
print(mySm.getData.__doc__)



