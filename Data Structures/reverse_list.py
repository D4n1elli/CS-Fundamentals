# challenge: reverse a list by stacking it

def main():
    original = []

    print("\nPlease digit 10 numbers to stack them")

    # asks user for 10 numbers
    for i in range(0, 10):
        number = int(input(f"Number {i+1}: "))
        original.append(number)

    print(f"Original list: {original}")


    reversed_list = []

    # while original still have items, pop them into reversed list
    while original:
        reversed_list.append(original.pop())


    print(f"Stacked list: {reversed_list}")

main()