# 1. 문자를 입력받아, 대소문자를 변경하시오.
# 문자내의 대문자->소문자, 소문자->대문자
# 예) HellO => hELLo

def convert_case(text):
    convert_text = ""

    for char in text:
        if char.islower():
            convert_text += char.upper()
        elif char.isupper():
            convert_text += char.lower()
        else:
            convert_text += char

    return convert_text

print(convert_case('HellO'))
print(convert_case('WelCOME'))
print(convert_case('GoodBye'))
print(convert_case('Good Bye'))
print(convert_case('This is long message.. haha1234'))

def convert_case2(text):
    return ''.join([char.upper() if char.islower() else char.lower() for char in text])

print(convert_case2('HellO'))
