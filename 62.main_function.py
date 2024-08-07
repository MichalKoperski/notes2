# Python interpreter sets "special variables", one of which __name__
# Python will assign the __name__ variable a value of '__main__' if it's the initial module being run

def main():
    print("Hello")

if __name__ == '__main__':
    main()