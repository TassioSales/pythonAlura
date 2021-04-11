from ExtratorArgumentosUrl import ExtratorArgumentosUrl

# Vídeo 01 - Métodos especiais

url = "https://bytebank.com/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=1500"

argumentosUrl = ExtratorArgumentosUrl(url)
moedaOrigem, moedaDestino = argumentosUrl.extraiArgumentos()
valor = argumentosUrl.extraiValor()
print(moedaDestino, moedaOrigem, valor)
print(len(argumentosUrl))

# Vídeo 02 - Dando um nome a nossa classe

url = "https://bytebank.com/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=1500"

argumentosUrl = ExtratorArgumentosUrl(url)
moedaOrigem, moedaDestino = argumentosUrl.extraiArgumentos()
valor = argumentosUrl.extraiValor()
print(moedaDestino, moedaOrigem, valor)
print(len(argumentosUrl))
print(argumentosUrl)

# Vídeo 03 - Comparando instâncias

url = "https://bytebank.com/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=1500"

argumentosUrl1 = ExtratorArgumentosUrl(url)
argumentosUrl2 = ExtratorArgumentosUrl(url)

print(id(argumentosUrl1))
print(id(argumentosUrl2))
print(argumentosUrl1 == argumentosUrl2)

url1 = "https://bytebank.com/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=1500"
url2 = "https://bytebank.com/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=500"

argumentosUrl1 = ExtratorArgumentosUrl(url1)
argumentosUrl2 = ExtratorArgumentosUrl(url2)

print(id(argumentosUrl1))
print(id(argumentosUrl2))
print(argumentosUrl1 == argumentosUrl2)