class Post(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __iter__(self):
        return iter(self.__dict__)
