def is_gender_a_man():
  is_man = input("Are you a man? (Yes/No): ")
  
  if is_man == 'No' or is_man == 'no' or is_man == 'NO':
    return False
  else:
    return True

if __name__ == '__main__':
    name = input("Enter your name:")
    second_name = input("Enter your second name:")
    age = int(input("Enter your age:"))
    is_man = is_gender_a_man()

    if is_man:
        print(name + ' ' + second_name + ' ' + 'is a man. ' + str(age) + ' years old.')
    else:
        print(name + ' ' + second_name + ' ' + 'is a woman. ' + str(age) + ' years old.')
