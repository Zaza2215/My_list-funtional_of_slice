from collections import UserList


class MyList(UserList):

    def __getitem__(self, key):
        if isinstance(key, slice):
            start, stop, step = key.start, key.stop, key.step
            if start <= len(self) and stop <= len(self):
                return super().__getitem__(key)
            else:
                pass  # TODO: implement the necessary logic
        else:
            return super().__getitem__(key)
