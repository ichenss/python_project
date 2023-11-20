import xlsxwriter
from PIL import Image

img = Image.open("../Face_ai/data/p1.jpg")
img_height = img.height
img_width = img.width

if img_width > 500:
    img_height = int(500 / img_width * img_height)
    img_width = 500

workbook = xlsxwriter.Workbook('draw.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_default_row(9)
worksheet.set_column(0, img_width, 1)

for i in range(img_width):
    for j in range(img_height):
        color = img.getpixel((i, j))
        color = tuple(item - item % 5 for item in color)
        color = "#%02x%02x%02x" % color  # 十进制转16进制
        cell_format = workbook.add_format({'bg_color': color})
        worksheet.write(j, i, '', cell_format)

workbook.close()
print("over")
