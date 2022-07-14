letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",

    ".",
    ",",
    " ",
    "!",
    "?"
]

prefix = "genk-"

JUMP = 2

cipher = [
    "7j",
    "ml",
    "pi",
    "ty",
    "1k",
    "bv",
    "il",
    "mn",
    "3a",
    "qw",
    "ou",
    "ur",
    "ma",
    "ey",
    "0y",
    "fc",
    "ui",
    "am",
    "yn",
    "ne",
    "5m",
    "ii",
    "bs",
    "kg",
    "hh",
    "cp",

    "99",
    "55",
    "22",
    "00",
    "11"
]

loop = True


while loop:
    text = str(input("Insira seu texto em Genk: "))

    if text.startswith(prefix):
        text = text.removeprefix(prefix)

        divided = [text[i:i+JUMP] for i in range(0, len(text), JUMP)]

        new_text_list = divided

        for i in divided:
            if i in cipher:
                new_text_list[divided.index(i)] = letters[cipher.index(i)]
            else:
                new_text_list[divided.index(i)] = "▯"

        new_text = ""

        for i in new_text_list:
            new_text += i

        print("Seu texto traduzido: " + new_text)
        print("")
    else:
        print("Isso não é um texto em Genk.")

    res = input("Deseja traduzir mais algum texto? [s/n]: ")

    if res.startswith("s"):
        pass
    elif res.startswith("n"):
        loop = False