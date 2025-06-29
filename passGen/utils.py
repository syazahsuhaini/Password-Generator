import random
import string

def lengthInput(optTyp, length, count, optU, optL, optD, optS):
  o = optTyp
  l = length
  c = count
  ou = optU
  ol = optL
  od = optD
  os = optS

  # define character sets
  uppletters = string.ascii_uppercase
  lowletters = string.ascii_lowercase
  digits = string.digits
  symbols = string.punctuation

  # the password must have combination of uppercase, lowercase, digit and symbol
  result = []

  if l % c == 0:
    comb1 = l // c
    comb2 = comb1
  else:
    comb2 = l // c
    comb1 = comb2 + (l - (comb2 * c))

  if o == 1 or (o == 2 and c == 4):
    for _ in range(comb1):
      result.append(random.choice(lowletters))
    for _ in range(comb2):
      result.append(random.choice(uppletters))
      result.append(random.choice(digits))
      result.append(random.choice(symbols))

  elif c == 3 and ol == 'Y':
    for _ in range(comb1):
      result.append(random.choice(lowletters))
    if ou == 'Y' and od == 'Y' and os == 'N':
      for _ in range(comb2):
        result.append(random.choice(uppletters))
        result.append(random.choice(digits))
    elif ou == 'Y' and od == 'N' and os == 'Y':
      for _ in range(comb2):
        result.append(random.choice(uppletters))
        result.append(random.choice(symbols))
    elif ou == 'N' and od == 'Y' and os == 'Y':
      for _ in range(comb2):
        result.append(random.choice(digits))
        result.append(random.choice(symbols))
  elif c == 3 and ol == 'N':
    for _ in range(comb1):
      result.append(random.choice(uppletters))
    for _ in range(comb2):
      result.append(random.choice(digits))
      result.append(random.choice(symbols))

  elif c == 2 and ol == 'Y':
    for _ in range(comb1):
      result.append(random.choice(lowletters))
    if ou == 'Y' and od == 'N' and os == 'N':
      for _ in range(comb2):
        result.append(random.choice(uppletters))
    if ou == 'N' and od == 'Y' and os == 'N':
      for _ in range(comb2):
        result.append(random.choice(digits))
    if ou == 'N' and od == 'N' and os == 'Y':
      for _ in range(comb2):
        result.append(random.choice(symbols))
  elif c == 2 and ol == 'N':
    for _ in range(comb1):
      result.append(random.choice(uppletters))
    if od == 'Y':
      for _ in range(comb2):
        result.append(random.choice(digits))
    elif os == 'Y':
      for _ in range(comb2):
        result.append(random.choice(symbols))

  random.shuffle(result)

  password = ''.join(result)

  print("Your password: ", password)
  print("Password length: ", len(password))

def typ2():
  optU, optL, optD, optS = optTyp2()

  while optU == 'N' and optL == 'N':
    print("Must include at least upper or lower character.")
    optU, optL, optD, optS = optTyp2()
  else:
    count = countOptTyp2(optU, optL, optD, optS)

  return count, optU, optL, optD, optS

def optTyp2():
  optU = ''
  optL = ''
  optD = ''
  optS = ''

  while True:
    optU = input("Do you want your password to include uppercase letters? Y-Yes | N-No ").upper()
    if optU in ['Y','N']:
      break
    print("Invalid input. Please enter Y or N.")

  while True:
    optL = input("Do you want your password to include lowercase letters? Y-Yes | N-No ").upper()
    if optL in ['Y','N']:
      break
    print("Invalid input. Please enter Y or N.")

  while True:
    optD = input("Do you want your password to include digits? Y-Yes | N-No ").upper()
    if optD in ['Y','N']:
      break
    print("Invalid input. Please enter Y or N.")

  while True:
    optS = input("Do you want your password to include symbols? Y-Yes | N-No ").upper()
    if optS in ['Y','N']:
      break
    print("Invalid input. Please enter Y or N.")

  return optU, optL, optD, optS

def countOptTyp2(optU, optL, optD, optS):
  count = 0

  if optU == 'Y':
    count += 1
  if optL == 'Y':
    count += 1
  if optD == 'Y':
    count += 1
  if optS == 'Y':
    count += 1
  print("Count options: ", count)

  return count