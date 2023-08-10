#
# Example file for working with conditional statements
# LinkedIn Learning Python course by Joe Marini
#


def main():
    x, y = 100, 100

    if x < y:
        result = "x is less than y"
    elif x == y:
        result = "x same as y"
    else:
        result = "x > y"

    print(result)

    # conditional statements let you use "a if C else b"

    # match-case makes it easy to compare multiple values
    value = "one"


if __name__ == "__main__":
    main()
