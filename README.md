Projeto: Jogo da Forca em Python

Desenvolvi um clássico Jogo da Forca utilizando Python, focado em criar uma experiência completa de usuário via terminal e aplicar boas práticas de organização de código.

O que foi feito:
Modularização de Dados: Separei a lógica principal do jogo do banco de palavras. O arquivo resultado.py funciona como um "dicionário" independente, facilitando a manutenção e a expansão do vocabulário sem afetar o funcionamento do jogo.

Lógica de Controle: Implementei sistemas de verificação para letras repetidas, validação de entradas (apenas letras) e contagem de tentativas com feedback visual (boneco da forca em ASCII).

Interface e Experiência: Utilizei a biblioteca time para criar intervalos de resposta, tornando a interação mais dinâmica, e o random para garantir que cada partida apresente um desafio novo.

Portabilidade: O projeto foi compilado em um arquivo executável (.exe) com ícone personalizado, permitindo que qualquer pessoa jogue no Windows sem precisar instalar o Python.

Tecnologias Utilizadas:
Linguagem: Python 3.

Módulos: random, time e PyInstaller.