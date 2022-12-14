def announce (f):
    def wrapper():
        print ("about to run the function...")
        f()
        print ('Done...')
    return wrapper

@announce
def hello():
    print('Hello World')

hello()