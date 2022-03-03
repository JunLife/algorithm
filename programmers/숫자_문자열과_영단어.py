def solution(s):
    _dict = {
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
    
    for number, string in enumerate(_dict):
        s = s.replace(string, str(number))
    return int(s)