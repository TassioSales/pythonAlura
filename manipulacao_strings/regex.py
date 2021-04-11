import re

# Vídeo 01 - O que são expressões regulares

email1 = 'Meu número é 1234-1234'
email2 = 'Fale comigo em 1234-1234 esse é meu telefone'
email3 = '1234-1234 é o meu celular'
email4 = 'ewqhueyhaxdnbca 9543-1254 fhdsahf ifdskafpohds'

padrao = '[0123456789][0123456789][0123456789][0123456789][-][0123456789][0123456789][0123456789][0123456789]'

retorno = re.search(padrao, email1)
print(retorno.group())

retorno = re.search(padrao, email2)
print(retorno.group())

retorno = re.search(padrao, email3)
print(retorno.group())

retorno = re.search(padrao, email4)
print(retorno.group())

# Vídeo 02 - Regex com quantificadores

padrao = '[0-9][0-9][0-9][0-9][-][0-9][0-9][0-9][0-9]'

retorno = re.search(padrao, email1)
print(retorno.group())

padrao = '[0-9]{4}[-][0-9]{4}'

retorno = re.search(padrao, email1)
print(retorno.group())

# Vídeo 03 - Quantificadores com intervalos

email4 = 'ewqhueyhaxdnbca 99543-1254 fhdsahf ifdskafpohds'

padrao = '[0-9]{4,5}[-][0-9]{4}'

retorno = re.search(padrao, email4)
print(retorno.group())

email4 = 'ewqhueyhaxdnbca 99543-1254 fhdsahf 9876-1234 ifdskafpohds 9876-1234'

retorno = re.findall(padrao, email4)
print(retorno)

padrao = '[0-9]{4,5}[-]*[0-9]{4}'
email4 = 'ewqhueyhaxdnbca 995431254 fhdsahf 98761234 ifdskafpohds 9876-1234'

retorno = re.findall(padrao, email4)
print(retorno)