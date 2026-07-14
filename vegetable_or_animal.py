def animal():
  print("Does the animal live in the water? Y/N")
  answer = input().lower()
  if answer == "n":
    print("Does the animal have wings? Y/N")
    answer = input().lower()
    if answer == "y":
      print("It must be an Ostrich!")
    else:
        print("It must be a Lion!")
  else:
    print("It must be a Whale!")

def vegetable():
  print("Is the vegetable green? Y/N")
  answer = input().lower()
  if answer == "y":
    print("Does the vegetable resemble a tree? Y/N")
    answer = input().lower()
    if answer == "y":
      print("It must be Broccoli!")
    else:
      print("It must be Peas!")
  elif answer == "n":
    print("Is the vegetable orange? Y/N")
    answer = input().lower()
    if answer == "y":
      print("It must be a Carrot!")
    else:
      print("It must be Sweetcorn!")
  else:
    print("That is not one of the options!")

print("Choose something from this list:\nPeas, Broccoli, Carrot, Sweetcorn, Ostrich, Lion or Whale")
print("Is your choice animal? Y/N")
answer = input().lower()
if answer == "y":
  animal()
else:
  vegetable()
