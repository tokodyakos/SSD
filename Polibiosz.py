def polibios_encode(text):
    text = text.upper()
    encoded_text = ""
    polibios_grid = [
        ['A', 'B', 'C', 'D', 'E'],
        ['F', 'G', 'H', 'I', 'K'],
        ['L', 'M', 'N', 'O', 'P'],
        ['Q', 'R', 'S', 'T', 'U'],
        ['V', 'W', 'X', 'Y', 'Z']
    ]

    for karakter in text:
        if karakter == "J":
            karakter = "I"
        if karakter.isalpha():
            for i in range(5):
                for j in range(5):
                    if polibios_grid[i][j] == karakter:
                        encoded_text += str(i + 1) + str(j + 1) + " "
                        break
        else:
            encoded_text += karakter + " "

    return encoded_text.rstrip()

"""
def polibios_decode(encoded_text):
    decoded_text = ""
    parok = encoded_text.split()
    polibios_grid = [
        ['A', 'B', 'C', 'D', 'E'],
        ['F', 'G', 'H', 'I', 'K'],
        ['L', 'M', 'N', 'O', 'P'],
        ['Q', 'R', 'S', 'T', 'U'],
        ['V', 'W', 'X', 'Y', 'Z']
    ]

    for par in parok:
        row = int(par[0]) - 1
        col = int(par[1]) - 1
        decoded_text += polibios_grid[row][col]

    return decoded_text

input_text = input("Kérem, adjon meg egy mondatot: ")

encoded_text = polibios_encode(input_text)
with open("kodolt.txt", "w") as file:
    file.write(encoded_text)

with open("kodolt.txt", "r") as file:
    encoded_text_from_file = file.read()

decoded_text = polibios_decode(encoded_text_from_file)

print("Kódolt szöveg:", encoded_text)
print("Dekódolt szöveg:", decoded_text)
"""