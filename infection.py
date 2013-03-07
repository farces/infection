__author__ = 'facest'

infected = {}


class Infection:
    """Represents a transform from an original method to an infected method. Basic implementation calls the target
       function followed by the original source function, with arguments possibly modified.

       Typical use case: provide debug info before entering a function.

       source: any method
       target: any method matching the prototype of source (*args, **kwargs OK)
       local: scope of the source and target methods (typically local=global())

       target: may modify input arguments, however it must return both args and kwargs if that is the case
       (tuple for *args, dict for **kwargs)
       """

    def __init__(self, source, target, local):
        self.source = source
        self.target = target
        self.local = local  # scope of the function to be infected
        self.__name__ = self.source.__name__

    def __call__(self, *args, **kwargs):
        args, kwargs = self._wrap(self.target, *args, **kwargs)
        return self.source(*args, **kwargs)

    def _wrap(self, call, *args, **kwargs):
        try:
            args, kwargs = call(*args, **kwargs)
        except TypeError:
            pass

        return args, kwargs

    def remove(self):
        """Reset infected function to it's original state"""
        self.local[self.source.__name__] = self.source
        del infected[self.source.__name__]
        print "Infection removed: %s" % self.source.__name__

    def apply(self):
        if self.source.__name__ in infected:
            print "Method already infected: %s -> %s" % (
                self.source.__name__, infected[self.source.__name__].target.__name__)
            return

        self.local[self.source.__name__] = self
        infected[self.source.__name__] = self
        print "Applied infection: %s -> %s" % (self.source.__name__, self.target.__name__)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.remove()


def infect(source, target, local):
    """Create Infection instance and immediately apply it to the source method"""
    inf = Infection(source, target, local)
    inf.apply()


def clear_infected():
    """Remove all current infections"""
    print "Clearing infections: "
    for source, instance in infected.items():
        print "Removing %s -> %s" % (source, instance.target.__name__)
        instance.remove()
    infected.clear()


def list_infected():
    """List current infected methods"""
    print "Infected methods: "
    for source, instance in infected.items():
        print "%s -> %s" % (source, instance.target.__name__)


