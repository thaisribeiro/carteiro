from PIL import Image
from unidecode import unidecode

input_text = open('text.txt').read()

# caminho da imagem onde vamos escrever nosso texto
background = Image.open('hand_fonts/page.png')
x, y = 0, 0

for text in unidecode(input_text):
    # verifica se tem quebra de linha e atualiza o eixo y, 
    # acrescentando 140px para a proxima linha
    if ord(text) == 10:
      x = 0
      y += 140
      continue
      
    # vamos usar a função ord que irá reproduzir
    # o respectivo código Ascii do nosso item e converter em string
    ascii_current = str(ord(text))
    try:
      font = Image.open(f'hand_fonts/{ascii_current}.png')
    except: 
      continue
    
    # atualiza a pagina em branco que escolhemos
    background.paste(font, (x, y))
    
    x += font.width

    # verificamos se a largura da linha está excedendo a largura da página, se sim, 
    # vamos para a próxima linha adicionando 140 px na variável y
    if background.width < x or len(text) * 115 > (background.width - x):
        x = 0
        y += 140

background.show()
