import matplotlib.pyplot as plt
from PIL import Image
from pdf2image import convert_from_path

# def latex_to_png(latex_str):
#     fig = plt.figure()
#
#     plt.axis("off")
#     plt.text(0.5, 0.5, f"${latex_str}$", size=50, ha="center", va="center")
#
#     # pdf_path = "result.pdf"
#     png_path = " result.png"
#     plt.savefig(png_path, format="png", bbox_inches="tight", pad_inches=0.4)
#     plt.close(fig)
#
#     # image = convert_from_path(pdf_path)
#     # image[0].save(png_path, "PNG")
#
#     return png_path
#
# latex_formula = ('При температуре \\(0^{\\circ}C\\) серебряная цепочка имеет длину \\(l_{\\circ}=0.6\\)м. При возрастании температуры происходит тепловое расширение серебряной цепочки, и её длина, выраженная в метрах, меняется по закону \\(l(t^{\\circ})=l_0(1+\\alpha{\\cdot}t^{\\circ})\\), где \\(\\alpha=1.95{\\cdot}10^{-5}(^{\\circ}C^{-1})\\) — коэффициент теплового расширения, \\(t^{\\circ}\\) — температура (в градусах Цельсия). При какой температуре серебряная цепочка удлинится на 0.3мм? Ответ выразите в градусах Цельсия.').replace('\\(', ' ').replace('\\)', ' ')
# png_path = latex_to_png(latex_formula)
#
# print(png_path)

# image = Image.open(png_path)
# image.show()

# t = 'При температуре \\(0^{\\circ}C\\)'
# t = t.replace('\\(', '').replace('\\)', '')
#
# print(t)


# import matplotlib.pyplot as plt
# from PIL import Image
#
# def latex_to_png(latex_str):
#     fig = plt.figure()
#
#     plt.axis("off")
#     plt.text(0.5, 0.5, f"{latex_str}", size=12, ha="center", va="center", wrap=True)
#
#     png_path = "result.png"
#
#     plt.savefig(png_path, format="png", bbox_inches="tight", pad_inches=0.1)
#     plt.close(fig)
#
#     return png_path
#
# latex_formula = "При температуре $0^{\circ}C$"
# png_path = latex_to_png(latex_formula)
#
# image = Image.open(png_path)
# image.show()


import matplotlib.pyplot as plt
import numpy as np
import io
import base64

def latex_to_console(latex_str):
    fig, ax = plt.subplots()
    ax.axis("off")
    ax.text(0.5, 0.5, f"${latex_str}$", size=50, ha="center", va="center")
    return ax.text(0.5, 0.5, f"{latex_str}", size=50, ha="center", va="center")

# Пример использования
latex_str = r"x^2 + y^2 = r^2"
latex_to_console(latex_str)
print(latex_to_console(latex_str))

