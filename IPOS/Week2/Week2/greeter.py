
def greet():
    print(f"hello from greeter.py{__name__}")
    print("Hello,World!")

def main():

    greet()
    print(__name__)

if __name__ == '__main__':
    main()
    #a = 42
    #greet()