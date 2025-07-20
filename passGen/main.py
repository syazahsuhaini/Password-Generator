from utils import lengthInput, typ2

# ask user auto password generation or customized
optTyp = int(input("1-Auto password generation | 2-Customized password generation : "))

while optTyp not in [1, 2]:
  print("Invalid input.")
  optTyp = int(input("1-Auto password generation | 2-Customized password generation : "))
else:
  if optTyp == 1:
    length = 20
    count = 4
    lengthInput(optTyp, length, count, '', '', '', '')
  else:
    # ask user for password length
    length = int(input("Enter desired password length: "))

    while length < 12:
      print("Password length must be greater than or equal to 12 characters.")
      length = int(input("Enter desired password length: "))
    else:
      count, optU, optL, optD, optS = typ2()

      while count < 2:
        print("Options must at least 2.")
        count, optU, optL, optD, optS = typ2()
      else:
        lengthInput(optTyp, length, count, optU, optL, optD, optS)


