from PIL import Image

# Имя файла, который вы положили в папку
file_name = "icon-1.png" 

img = Image.open(file_name).convert("RGBA")

# Создаем квадратный холст
size = max(img.size)
new_im = Image.new('RGB', (size, size), (10, 10, 10)) # Цвет фона #0a0a0a

# Кладем картинку по центру
paste_x = int((size - img.size[0]) / 2)
paste_y = int((size - img.size[1]) / 2)
new_im.paste(img, (paste_x, paste_y), img)

# Сохраняем нужные размеры
new_im.resize((512, 512), Image.Resampling.LANCZOS).save("icon-512.png")
new_im.resize((192, 192), Image.Resampling.LANCZOS).save("icon-192.png")

print("Ура! Файлы icon-512.png и icon-192.png созданы.")