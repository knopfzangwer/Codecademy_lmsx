import pandas as pd
from pandas._libs.hashtable import ismember

punctuation = ".,?'! "
alphabet = "abcdefghijklmnopqrstuvwxyz"

def decifrar_codigo(mensagem, offset):
    decifrada = []

    alfabeto_normal = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    # criando alfabeto com offset desejado
    alfabeto_k = [chr(i) for i in range(ord('a') + offset, ord('z') + 1)]
    alfbeto_k_complementar = [chr(i) for i in range(ord('a'), ord('a') + offset)]

    for item in alfbeto_k_complementar:
        alfabeto_k.append(item)

    for letra in mensagem:
        if letra in alfabeto_normal:
            indice_posicao = alfabeto_normal.index(letra)
            nova_letra = alfabeto_k[indice_posicao]
            decifrada.append(nova_letra)
        else:
            decifrada.append(letra)

    decifrada_nova = ''.join(decifrada)
    print(decifrada_nova)
    return decifrada_nova

mensagem_codificada = 'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'
decifrar_codigo(mensagem_codificada, 10)

def codificar_messagem(mensagem, offset):
    codificada = []

    alfabeto_normal = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    # criando alfabeto com offset desejado
    alfabeto_k = [chr(i) for i in range(ord('a') + offset, ord('z') + 1)]
    alfbeto_k_complementar = [chr(i) for i in range(ord('a'), ord('a') + offset)]

    for item in alfbeto_k_complementar:
        alfabeto_k.append(item)

    for letra in mensagem:
        if letra in alfabeto_k:
            indice_posicao = alfabeto_k.index(letra)
            nova_letra = alfabeto_normal[indice_posicao]
            codificada.append(nova_letra)
        else:
            codificada.append(letra)

    codificada_nova = ''.join(codificada)
    print(codificada_nova)
    return codificada_nova

mensagem_aberta = 'ola vishal, consegui decifrar seu codigo! estou mandando uma mensagem encriptada com o mesmo offset'
testando_messagem = codificar_messagem(mensagem_aberta, 10)
decifrar_codigo(testando_messagem, 10)

first_message = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
second_message = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"

decifrar_codigo(first_message, 10)
decifrar_codigo(second_message, 14)

third_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

for num in range(1, 10):
    breaker = decifrar_codigo(third_message, num)

def vigenere_coder(message, keyword):
    letter_pointer = 0
    keyword_final = ''
    for i in range(0, len(message)):
        if message[i] in punctuation:
            keyword_final += message[i]
        else:
            keyword_final += keyword[letter_pointer]
            letter_pointer = (letter_pointer+1) % len(keyword)
    print(keyword_final)

    translated_message = ''
    for i in range(0, len(message)):
        if message[i] not in punctuation:
            ln = alphabet.find(message[i]) + alphabet.find(keyword_final[i])
            translated_message += alphabet[ln % 26]
        else:
            translated_message += message[i]
    return translated_message

message_for_v = "thanks for teaching me all these cool ciphers! you really are the best!"
keyword = "besties"

print(vigenere_coder(message_for_v, keyword))

def vigenere_decoder(coded_message, keyword):
    letter_pointer = 0
    keyword_final = ''
    for i in range(0, len(coded_message)):
        if coded_message[i] in punctuation:
            keyword_final += coded_message[i]
        else:
            keyword_final += keyword[letter_pointer]
            letter_pointer = (letter_pointer+1) % len(keyword)
    translated_message = ''
    for i in range(0, len(coded_message)):
        if not coded_message[i] in punctuation:
            ln = alphabet.find(coded_message[i]) - alphabet.find(keyword_final[i])
            translated_message += alphabet[ln % 26]
        else:
            translated_message += coded_message[i]
    return translated_message

message = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
keyword = "friends"

print(vigenere_decoder(message, keyword))


