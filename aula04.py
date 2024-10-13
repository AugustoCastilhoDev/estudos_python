# if Lógica e Condições

vendas = 1500
meta = 1300

if vendas >= meta:
    print("Vendedor ganha bônus")
    print("Bateu a meta de vendas")
    bonus = 0.1 * vendas
    print("Bonus do vendedor: ", bonus)
else:
    print("Vendedor não ganha bônus")
    print("Não bateu a meta de vendas")

print("Acabou o programa")

#2º cenário

vendas = 1700
vendas_empresa = 10000
meta_empresa = 20000
meta1 = 1300 # ganhar 10%
meta2 = 2000 # ganhar 13%

if vendas >= 2000 and vendas_empresa >= meta_empresa:
    bonus = 0.13 * vendas
elif vendas >= 1300 and vendas_empresa >= meta_empresa:
    bonus = 0.1 * vendas
else:    
    bonus = 0    

print("Bonus: ",bonus)


lista_produtos = ["airpod", "ipad", "iphone", "macbook"]
produto_procurado = input("Procure um produto: ")
produto_procurado = produto_procurado.lower

if produto_procurado in lista_produtos:
    print("Produto no estoque")
else:
    print("Não temos esse produto")    
