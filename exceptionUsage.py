digit_map = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def convert(string):
    try:
        integer = -1
        number = ''
        words = string.split()
        for word in words:
            number += digit_map[word]
        integer = int(number)
    except (KeyError, TypeError, AttributeError):
        print("Conversion failed")
    if integer != -1:
        return integer
    else:
        pass

print(convert("one zero threety six"))
print(convert(512))
print(convert("one zero two eight seven two"))