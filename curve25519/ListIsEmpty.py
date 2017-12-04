

class ListIsEmpty(object):

    def __init__(self,l):

        self.value = True

        for i in l:
            if l[i] !=0:
                self.value = False
                break

    def __getattribute__(self, name):
        if(name=="value"):
            return object.__getattribute__(self, name)
