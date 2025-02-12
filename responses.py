from random import choice, randint

def get_response(user_input: str) -> str:
    lowered :str = user_input.lower()

    if lowered == '':
        print('why is everyone ignoring me bhai..')
    elif 'hello' in lowered:
        return 'hello bhai im so bored'
    elif 'how are you' in lowered:
        return'im good bhai how are you??'
    elif 'roll a dice for me async':
        return f'you rolled :{randint(1,6)}'