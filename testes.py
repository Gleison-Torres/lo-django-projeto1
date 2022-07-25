senha = 'avAlanche1@'

contador_maiusculas = 0
contador_caractere_especial = 0
contador_numeros = 0

for s in senha:
    if s.isupper():
        contador_maiusculas += 1
    if s in '@$%&*!':
        print(s)
        contador_caractere_especial += 1
    if s.isnumeric():
        print(s)
        contador_numeros += 1

print(f'Esta senha contem {contador_maiusculas} letras maiusculas.')
print(f'Esta senha contem {contador_caractere_especial} caractere especial')
print(f'Esta senha contem {contador_numeros} caracteres numericos')

if contador_maiusculas == 0 or contador_caractere_especial == 0:
    if contador_maiusculas == 0:
        print('Esta senha precisa de pelo menos uma letra maiuscula')
    if contador_caractere_especial == 0:
        print('Esta senha precisa de pelo menos um caractere especial Ex. [@-#-$-%-&-*')