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
    number = ''
    words = string.split()
    for word in words:
        number += digit_map[word]
    integer = int(number)
    return integer

print(convert("one zero three six"))