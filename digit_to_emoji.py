emojies = {
    '0': ':zero:',
    '1': ':one:',
    '2': ':two:',
    '3': ':three:',
    '4': ':four:',
    '5': ':five:',
    '6': ':six:',
    '7': ':seven:',
    '8': ':eight:',
    '9': ':nine:',
}

def toEmoji(num):
    str_num = str(num)
    emoji = ' '.join([emojies[char] for char in str_num])
    return emoji
