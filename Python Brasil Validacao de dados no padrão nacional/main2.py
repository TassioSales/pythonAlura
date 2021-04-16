from validate_docbr import CPF
from validate_docbr import CPF,CNPJ

arquivo = open('cpf-cnpj.txt', 'r')

cpf_cnpf = []

cpf = CPF()
cnpj = CNPJ()
for itens in arquivo:
        itens.strip()
        cpf_cnpf.append(itens)
print(cpf_cnpf)        

cpf_cnpf = cpf.mask(cpf_cnpf)

print(cpf_cnpf)