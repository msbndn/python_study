if __name__ == '__main__':
    name = input("Enter your name:")
    second_name = input("Enter your second name:")
    age = int(input("Enter your age:"))
    is_man = 0

    check_gender = input("Are you a man? (Yes/No): ")
    if check_gender == 'Yes' or check_gender == 'yes' or check_gender == 'YES':
        is_man = True
    elif check_gender == 'No' or check_gender == 'no' or check_gender == 'NO':
        is_man = False

    if is_man:
        print(name + ' ' + second_name + ' ' + 'is a man. ' + str(age) + ' years old.')
    else:
        print(name + ' ' + second_name + ' ' + 'is a woman. ' + str(age) + ' years old.')