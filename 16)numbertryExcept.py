def main():
    print("x is ",get_int("What's x? "))


def get_int(prompt):
    while True:
        try:
            x=int(input(prompt))
        except ValueError:
            pass
        else:
            return x
        
main()