import sys, re

numbers = {
    0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',
    10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',
    20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety'
}

def has_numbers(s):
    return any(c.isdigit() for c in s)

def convert_to_word(number):
    if number <= 20 or number % 10 == 0:
        return numbers[number]
    return numbers[number/10*10] + '-' + numbers[number%10]

def convert_if_number(word):
    if has_numbers(word):
        if word.isdigit():
            return convert_to_word(int(word))
        else:
            match = re.match(r"([0-9]*)([^0-9]*)", word, re.I)
            if match:
                items = match.groups()
                return convert_to_word(int(items[0])) + items[1]
    else:
        return word

for line in sys.stdin:
    line = line.strip().split()

    print ' '.join([convert_if_number(word) for word in line]).capitalize()
