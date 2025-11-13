path = 'data/endpoints_data.json'

def caesar_encrypt(text: str, offset: str, mode: str):
    result = ""
    for i in text.upper():
        if i == ' ':
            result += i
            continue
        char = chr(ord(i) - offset) if mode == "decrypt" else chr(ord(i) + offset)
        if ord(char) < ord('A'):
            num_char = abs(ord(char) - ord('A'))
            char = chr(ord('Z') + 1 - num_char)
        elif ord(char) > ord('Z'):
            num_char = ord(char) - ord('Z')
            char = chr(ord('A') - 1 + num_char)
        result += char
    return result

def fence_encrypt(text: str):
    text = text.replace(' ', '')
    flag = True
    even, no_even ="",""
    for i in text:
        if flag:
            even += i
        else:
            no_even += i
        flag = not flag
    return even + no_even
      
def fence_decrypt(text:str):
    result = text
    len_text = len(text) // 2 + 1
    if len(text) % 2 != 0:
        len_text += 1
    for _ in range(len_text):
        result = fence_encrypt(result)
    return result


def write_endpoint(data):
    with open(path, 'a') as f:
        data