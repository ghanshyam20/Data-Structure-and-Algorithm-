total = 0.0

while True:
    s = input("enter the numbers:")

    try:
        num = float(s)

        if num == 0:
            break

        total += num
        print(f"The total is now {total}")

    except ValueError:
        print("That wasn’t a number.")

print(f"The grand total is {total}")
