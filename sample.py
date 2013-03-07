import code
import infection


def original(x, y, z):
    print "%s %s %s" % (x, y, z)


def wrap_dump_arguments(*args, **kwargs):
    print "I'm infected!"
    print "*args: %s" % repr(args)
    print "**kwargs: %s" % repr(kwargs)
    x, y, z = args

    return (x, 500, z), kwargs


def run():
    print "Sample application to demonstrate use of code.interact() in conjunction with the infection helpers."
    while True:
        var = raw_input("1) REPL, 2) Call original(), Q) quit\n:")
        if var == "1":
            print "Ctrl+Z Enter to exit."
            code.interact(local=globals())
        elif var == "q" or var == "Q":
            exit()
        else:
            original(1, 2, 3)


if __name__ == "__main__":
    x = infection.Infection(original, wrap_dump_arguments, local=globals())
    x.apply()
    # OR
    # infection.infect(do_nothing, dummy_dumpargs, local=globals())
    run()
