produtos = ('Kit Copo', 30, 'Kit Taça', 35, 'Ventilador', 200, 'Pacote de Balões', 7.5)
print('-' * 40)
print(f'{"MERCADINHO IDEAL":^40}')
print('-' * 40)
print(f'{produtos[0]:.<31}R${produtos[1]:7.2f}')
print(f'{produtos[2]:.<31}R${produtos[3]:7.2F}')
print(f'{produtos[4]:.<31}R${produtos[5]:7.2F}')
print(f'{produtos[6]:.<31}R${produtos[7]:7.2F}')
print('-' * 40)
