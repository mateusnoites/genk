from asyncio.windows_events import NULL


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

cypher = [
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
    new_cypher = list(cypher)

    text = str(input("Insira seu texto: "))
    keynum = str(input("Insira a chave numérica (deixar em branco para a chave padrão): "))

    if keynum.replace(" ", "") == "":
        keynum == "000000000000000000000000000000000000000000000000000" # enchendo de zero pra piorar a performance :D
    
    final_key = keynum

    keys = list(keynum)

    for i in keys: # dessa parte até a linha 102, nem eu entendo o que eu fiz
        i = int(i)

        if i != 0:
            if (i%2) == 0:
                for i in range(0, i + 1):
                    new_cypher.reverse()
                    pass
            else:
                new_cypher.sort(reverse=((i + 13)%2 == 0))
        else:
            pass

    divided = list(text)

    new_text_list = divided

    for i in divided:
        if i in letters:
            new_text_list[divided.index(i)] = new_cypher[letters.index(i)]
        else:
            new_text_list[divided.index(i)] = "?!"

    new_text = prefix

    for i in new_text_list:
        new_text += i 

    print("Seu texto em Genk: " + new_text)
    print("Sua chave: " + final_key)
    print("")
    res = input("Deseja encriptar mais algum texto? [s/n]: ")

    if res.startswith("s"):
        pass
    elif res.startswith("n"):
        loop = False
