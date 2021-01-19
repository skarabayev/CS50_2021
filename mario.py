def main():
    size = int(input("Enter size of the pyramid: "))
    constructor(size)

def constructor(size):
    spaces = size - 1
    for i in range(0, size):
        for j in range(0,spaces):
            print(" ", end="")
        spaces -=1
        for j in range(0, i+1):
            print("#", end="")
        print()
main()
