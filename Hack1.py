import random
def good_password_generator(lenght=10):

  letters = 'abcdefghijklmnopqrstuvwxyz'
  upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  digits = '0123456789'
  symbols = '!@#$%^&*()_+=\'\\"'
  alphabet = letters + upper_letters + digits + symbols
  password = ''
  for i in range (lenght):
    char = random.choice(alphabet)
    password += char
  return password

print(good_password_generator(15))