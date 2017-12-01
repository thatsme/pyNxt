
class MyContainer:
    def __init__(self, *params):
           self.data = params
    def __iter__(self):
        if hasattr(self.data[0], "__iter__"):
            return self.data[0].__iter__()
        return self.data.__iter__()
    def __getitem__(self, item):
        if len(self.data)>=item and item is not 0:
            return self.data[item-1]
        else:
            return None
    def __setitem__(self, key, value):
        if len(self.data)>=key and key is not 0:
            self.data[key] = value
        else:
            return None