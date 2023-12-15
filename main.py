import os

def compactador(nomeArquivo):
  arquivo = open('entrada.txt', 'r')
  arquivoCompactado = open('entrada_compactada.txt', 'w')
  arquivoLegenda = open('legenda.txt', 'w')
  cont = 0
  dic = {}
  stringCompactada = ""
  stringLegenda = ""

  for linha in arquivo:
    linha = linha.split(" ")
    for palavra in linha:
      if palavra not in dic:
        dic[palavra] = cont
        cont += 1
      
      palavra = str(dic[palavra])
      stringCompactada += palavra + " "

  for key in dic:
    stringLegenda += f'{key}:{dic[key]}\n'

  arquivoCompactado.write(stringCompactada)
  arquivoLegenda.write(stringLegenda)

def descompactador(nomeArquivo):
    with open('legenda.txt', 'r') as arquivoLegenda:
        dicionario = {}
        for item in arquivoLegenda:
            item = item.replace('\n', '')
            item = item.split(":")
            dicionario[item[1]] = item[0]

    with open(f'{nomeArquivo}.txt', 'r') as arquivoEntrada:
        txt = ''
        for linha in arquivoEntrada:
            itens = linha.split()
            for palavra in itens:
                if palavra in dicionario:
                    palavra = dicionario[palavra]
                    txt += palavra + ' '

    with open('saida_descompactada.txt', 'w') as arquivoSaidaDescompactado:
        arquivoSaidaDescompactado.write(txt)

compactador("entrada")
descompactador("entrada_compactada")