def check_problema3(problema3, string):
    try:
        with open(problema3, 'r') as file:
            for line in file:
                line_without_spaces = line.replace(" ", "")
                if string in line_without_spaces:
                    return True
        return False
    except IOError:
        print(f"Error: Could not open file '{problema3}'")


problema3 = 'problema3.ino'
string1 = 'led_pin=5'
string2 =  'digitalWrite(led_pin,HIGH)'

if check_problema3(problema3, string1):
    if check_problema3(problema3, string2):
      print("Punctaj total: 10/10")
    else:
      print("Punctaj total: 5/10")
else:
    print("Punctaj total: 0")
