
class IterMixin(object):
    def __iter__(self):
        for attr, value in self.__dict__.iteritems():
            yield attr, value