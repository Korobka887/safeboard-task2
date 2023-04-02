def main():
    line = input()
    flag = True
    closing_brackets = "}])"
    opening_brackets = "{[("
    brackets = ""
    for i in line:
        brackets += i if i in opening_brackets or i in closing_brackets else ""

    index = 1
    while index < len(brackets):
        if brackets[index] in closing_brackets:
            flag = False if line[index] != line[index - 1] else flag
            brackets = brackets[:index - 1] + brackets[index + 1:]
            index -= 1
        else:
            index += 1
    print("Nice" if len(brackets) == 0 and not flag else "Bruh")


if __name__ == '__main__':
    main()
