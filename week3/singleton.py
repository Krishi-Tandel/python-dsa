#desgin pattern- singleton
#ensure only one instance of a class
class ControlTower:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print('Initializing control tower')
        return cls._instance
    
    def manageFlight(self,flight):
        print(f'Managing fight {flight}')

t1 = ControlTower()
t2 = ControlTower()

print(t1 is t2)

t1.manageFlight('a123')
t2.manageFlight('b456')

print(t1 is t2)


class Config:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print('Initializing instance')
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, "_initialize"):
            self.appname = 'My app'
            self.versiom = '1.0'
            self.debug = False
            self._initialize = True

c1 = Config()
c2 = Config()
print(c1 is c2)

c1._initialize = False

print(c2._initialize)
print(c1._initialize)
        
