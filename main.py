with open('entrada.txt','r') as arq:
    texto = arq.read()

print(texto)

lista = texto.split(' ')

cont = 0
dicionario = {}
zipada = []
txt_zipado = ''

for item in lista:
    if item not in dicionario:
        dicionario[item] = str(cont)
        txt_zipado += f' {item} : {dicionario[item]};\n'
        cont += 1
    zipada.append(dicionario[item])

txt_zipado += '\n'
txt_zipado += ' '.join(zipada)
print(txt_zipado)

with open('saida_compactada.txt','w') as arq:
    arq.write(txt_zipado)

