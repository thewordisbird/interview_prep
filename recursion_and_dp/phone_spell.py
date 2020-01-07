

def phone_spell(number, keypad):
    digit_list = num_to_digits(number)
    digit = digit_list.pop()
    result = []
    #chache = {}
    _phone_spell(digit_list, digit, keypad, result)
    return result

def _phone_spell(digit_list, digit, keypad, result):
    if digit_list:
        
        for letter in keypad[digit]:
            digit = digit_list.pop()
            word =  word + _phone_spell(digit_list, digit, keypad, result)
            print(word)
            result.append(word)


def num_to_digits(number):
    digit_list = []
    while number > 0:
        digit_list.append(number%10)
        number = number//10
    
    return digit_list




if __name__ == "__main__":
    keypad = {
            1:[],                   2:['a', 'b', 'c'],  3:['d', 'e', 'f'], 
            4:['g', 'h', 'i'],      5:['j', 'k', 'l'],  6:['m', 'n', 'o'], 
            7:['p', 'q', 'r', 's'], 8:['t', 'u', 'v'],  9:['w', 'x', 'y', 'z']
        }

print("Testing num_to_digits")
print(num_to_digits(397) == [7, 9, 3])

print("Phone Spell for 234")
print(phone_spell(234, keypad))



















