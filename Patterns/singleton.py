"""
Singleton pattern is a software design pattern that restricts the instantiation of a class to a singular instance

More specifically, the singleton pattern allows objects to:
    - Ensure they only have one instance
    - Provide easy access to that instance
    - Control their instantiation (for example, hiding the constructors of a class)

Common uses:
Singletons are often preferred to global variables because they do not pollute the global namespace (or their containing namespace). 
Additionally, they permit lazy allocation and initialization, whereas global variables in many languages will always consume resources.

The singleton pattern can also be used as a basis for other design patterns, such as the abstract factory, factory method, builder and prototype patterns. 
Facade objects are also often singletons because only one facade object is required.

Logging is a common real-world use case for singletons, because all objects that wish to log messages require a uniform point of access and conceptually write to a single source.
"""

class AplicationState:
    instance = None
    
    def __init__(self):
        self.isLoggedIn = False

    @staticmethod
    def getAppState():
        if not AplicationState.instance:
            AplicationState.instance = AplicationState()
        return AplicationState.instance
    
appState1 = AplicationState.getAppState()
print(appState1.isLoggedIn) # False

appState2 = AplicationState.getAppState()
appState2.isLoggedIn = True

print(appState1.isLoggedIn) # True
print(appState2.isLoggedIn) # True