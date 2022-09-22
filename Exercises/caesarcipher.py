alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").strip()
text = input("Type your message:\n").lower().strip()
shift = int(input("Type the shift number:\n"))

shift = shift % 26

def caesar():
    if direction == 'encode':
        nnw_txt = ''
        for letra in text:
            posicao = alphabet.index(letra)
            nova_posicao = posicao + shift
            if nova_posicao > 26:
                nova_posicao = nova_posicao % 26
            nnw_txt += alphabet[nova_posicao]
        return f'The encoded text is "{nnw_txt}"'
    elif direction == 'decode':
        new_txt = ''
        for letra in text:
            posicao = alphabet.index(letra)
            new_position = posicao - shift
            new_txt += alphabet[new_position]
        return f'The decoded text is {new_txt}'


print(caesar())
