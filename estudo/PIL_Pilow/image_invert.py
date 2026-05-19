from PIL import Image, ImageOps
from rich import print

# PIL (ou Pillow)   -> Python Imaging Library

# Image: cuida de carregar, salvar e manipular a estrutura básica da imagem.
# 
# ImageOps (Image Operations): foca em algoritmos prontos de nível mais alto, como inverter 
# cores, espelhar, mudar contraste automaticamente ou adicionar bordas.

# img = Image.open("../../assets/imgs/casa_modo_claro.png")
# img = Image.open("../../assets/imgs/coracao_modo_claro.png")
img = Image.open("../../assets/imgs/download_modo_claro.png")

if img.mode == "RGBA":
    # O método .split() divide a imagem em seus canais de cores individuais e 
    # retorna uma tupla contendo esses canais como objetos de imagem separados 
    # (em escala de cinza).

    # Cada um desses elementos isolados é uma imagem onde os tons de branco 
    # representam a maior intensidade daquela cor (ou total opacidade, no caso 
    # do Alpha) e os tons de preto representam a ausência dela.

    r, g, b, a = img.split()
    rgb_img = Image.merge("RGB", (r, g, b))

    invert_img = ImageOps.invert(rgb_img)
    
    r, g, b = invert_img.split()
    final_img = Image.merge("RGBA", (r, g, b, a))
else:
    final_img = ImageOps.invert(img)

final_img.save("download_modo_escuro.png")
final_img.show()