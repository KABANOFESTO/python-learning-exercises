def Fibonacci(num):
    if num <= 1:
        return num
    else:
        return Fibonacci(num - 1) + Fibonacci(num - 2)


def main():
    num = int(input("Enter a number: "))
    print(f"Fibonacci of {num} is {Fibonacci(num)}")


if __name__ == "__main__":
    main()