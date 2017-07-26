class Output:
    """A device which   prints whatever gets passed to it"""
    def write(self, index, value):
        print(value)

    def read(self, index):
        pass

class Input:
    """A device triggering on a read to return user data"""
    def read(self, index):
        f = input('I need input...')
        try: # Hacky; Will be taken out once we get an actual parser running
            return int(f)
        except ValueError:
            return f

    def write(self, index, value):
        pass