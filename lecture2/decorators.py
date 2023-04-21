def announce(f):
    def wrapper():
        print("About to run")
        f()
        print("Done")
    return wrapper

@announce
def hello():
    print("Hello, world!")