total_de_paginas = list(range(1, 18))

quantidade_DePaginas_exibidas = 4
pagina_atual = 1

inicio = 0
fim = quantidade_DePaginas_exibidas


print(total_de_paginas[inicio:fim])

while True:

    p = int(input('Escolha a página: '))
    if p == 0:
        break
    if p < 3:
        pagina_atual = p
        print(f'Você está na página: {pagina_atual}')
        print(total_de_paginas[0:4])
    if p >= 3:
        pagina_atual = p

        meio_r = round(quantidade_DePaginas_exibidas / 2)
        inicio = pagina_atual - meio_r
        fim = pagina_atual + meio_r
        print(total_de_paginas[inicio:fim])
