import random


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'meow':
        return '~nyaaaaa <3'

    if message == 'roll dat dice homie':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return '`go myaw yourself`'

    if p_message == 'catfood?':
        return 'GIVE ME TUNA ^..^'

    if p_message == 'do mission':
        return 'n m'

    return 'meow?'
