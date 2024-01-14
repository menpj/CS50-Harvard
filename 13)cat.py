def main():
    meow(get_number())


def get_number():
    while True:
        x=int(input("What's n?"))
        if x>0:
            return x
        
def meow(x):
    for _ in range(x):
        print("meow")

main()