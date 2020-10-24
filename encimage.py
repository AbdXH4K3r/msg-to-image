import time

def matrix_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)

try:
    import os,sys
    from PIL import Image, ImageDraw, ImageFont
    import webcolors

except:
    matrix_print("Modules not found!\nAuto Installing...")
    os.system('pip install pillow')
    os.system('pip install webcolors')

os.system('cls')
matrix_print ("Welcome to Encimage!\n")
choice = input("(c)reate ?\n> ")
if choice == "c":
    os.system('cls')
    matrix_print("Create Mode:\n")
    filename = input("File name (e.g. Test.jpg): ")
    width = int(input("Width : "))
    height = int(input("Height : "))
    color = input("Color (e.g. red,magenta...): ")
    img = Image.new('RGB', (width,height), color)
    q = input("Continue ? (y/n) : ")
    if q == "y":
        os.system('cls')
        tools = input("1) Add a Text.\n2) Add Image.\n> ")
        if tools == "1":
            os.system('cls')

            canvas = ImageDraw.Draw(img)
            text = input("In-image Text : ")
            hiddenmsg = input("Hidden msg : ")

            text_color = input("Color : ")
            colorrgb = webcolors.name_to_rgb(text_color)

            text_size = int(input("Text size : "))
            choose_font = input("Font :\n1) Arial.\n2) Helvetica.\n3) Times.\n4) Akzidenz Grotesk.\n5) 8-bit.\n> ")
            if choose_font=="1":
                font = ImageFont.truetype("fonts/arial.ttf", text_size)
            elif choose_font=="2":
                font = ImageFont.truetype("fonts/helvetica.ttf", text_size)
            elif choose_font=="3":
                font = ImageFont.truetype("fonts/times.ttf", text_size)
            elif choose_font=="4":
                font = ImageFont.truetype("fonts/akz.ttf", text_size)
            elif choose_font=="5":
                font = ImageFont.truetype("fonts/8-bit.ttf", text_size)

            w, h = canvas.textsize(text, font=font)
            tx = (("%s%s%s")%("Weight Position (",((width-w)/2)," will be the center) : "))
            ty = (("%s%s%s")%("Height Position (",((height-h)/2)," will be the center) : "))
            text_position_x = float(input(tx))
            text_position_y = float(input(ty))

            canvas.text((text_position_x,text_position_y), text, fill=colorrgb, font=font)

            saving = input("Save result? (y/n) : ")
            if saving == "y":
                img.save(filename)
                matrix_print ("File Saved. Adios!")
                file = open(filename,'a')
                file.write("\n\n\n[HIDDEN MSG]\n"+hiddenmsg)
                file.close()
                quit()

            if saving == "n":
                matrix_print ("OK. Adios!")
                quit()

    else:
        preview = Canvas(root,width,height)
        preview.pack()
        saving = input("Save result? (y/n) : ")
        if saving == "y":
            img.save(filename)
            matrix_print ("File Saved. Adios!")
            quit()

        if saving == "n":
            matrix_print ("OK. Adios!")
            quit()


else:
    quit()
