
# reading every line with generator
def read_file():
    for line in open("passwords.txt", "r"):

        yield line


# actually algorithm
def checker():
    # result variable
    valid_passwords = 0

    for line in read_file():
        # cleaning line and taking data we need
        line = line.strip().split(" ")
        char, rule, password = line[0], line[1][:-1], line[2]
        rule_min, rule_max = rule.split("-")

        # processing over checkup
        if password.count(char) != 0 and int(rule_max) >= password.count(char) >= int(rule_min):
            valid_passwords+=1 # increasing over result count

    return valid_passwords


if __name__ == '__main__':
    print("Hello!")
    print("Let's check how many valid passwords you have")
    input("Press on any button:")
    print(f"You have {checker()} valid passwords)")
