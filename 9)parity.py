def main():
    x=int(input("Input a number:"))
    if is_even(x):
        print("Even Number")
    else:
        print("Odd Number")
    
def is_even(x):
    return x%2==0
    
main()