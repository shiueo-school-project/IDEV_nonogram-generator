import random
from PIL import Image, ImageDraw, ImageFont


def exczero(array):
    for i in range(0, len(array)):
        while 0 in array[i]:
            array[i].remove(0)

        if int(len(array[i])) < 1:
            array[i].append(0)

    return array


def ToImage(a, b, c, name):
    sztf = []
    sztt = []
    for i in range(0, len(a)):
        sztf.append(len(a[i]))
    sztf = max(sztf)

    for i in range(0, len(b)):
        sztt.append(len(b[i]))
    sztt = max(sztt)

    width = len(c) + sztt
    height = len(c[0]) + sztf
    print(width, height)

    Size = 120
    SizeW = Size * width
    SizeH = Size * height
    print(f"{a}\n{b}\n{c}")
    canvas = Image.new("RGB", (SizeW, SizeH), color="#ffffff")
    rect = ImageDraw.Draw(canvas)
    rect.rectangle(((SizeW * 1 / 35, SizeH * 1 / 35), (SizeW * 34 / 35, SizeH * 34 / 35)), outline=(0, 0, 0), width=4)
    rect.rectangle(((SizeW * 1 / 35 + sztt * (Size * 33 / 35), SizeH * 1 / 35 + sztf * (Size * 33 / 35)),
                    (SizeW * 34 / 35, SizeH * 34 / 35)), outline=(0, 0, 0), width=8)

    fnt = ImageFont.truetype("./src/fonts/GSTR.ttf", int(SizeW / 40))
    text = ImageDraw.Draw(canvas)
    text.text((SizeW * 30.3 / 35, SizeH * 34 / 35), "SHI3DO.", font=fnt, fill=(0, 0, 0, 30))

    for i in range(0, width):
        drawx = (SizeW * 33 / 35) / width
        linex = ImageDraw.Draw(canvas)
        line = ((SizeW * 1 / 35 + drawx * i, SizeH * 1 / 35), (SizeW * 1 / 35 + drawx * i, SizeH * 34 / 35))
        linex.line(line, fill="black")

    for i in range(0, height):
        drawy = (SizeH * 33 / 35) / height
        liney = ImageDraw.Draw(canvas)
        line = ((SizeW * 1 / 35, SizeH * 1 / 35 + drawy * i), (SizeW * 34 / 35, SizeH * 1 / 35 + drawy * i))
        liney.line(line, fill="black")

    fnx = ImageFont.truetype("./src/fonts/GSTR.ttf", 70)
    text = ImageDraw.Draw(canvas)
    for i in range(0, width - sztt):
        j = len(a[i])
        drawx = (SizeW * 33 / 35) / width
        drawy = (SizeH * 33 / 35) / height
        for g in range(0, j):
            text.text((SizeW * 1 / 35 + drawx * i + drawx * sztt + 30,
                       SizeH * 1 / 35 + drawy * g + 30), str(a[i][g]), font=fnx,
                      fill=(0, 0, 0, 30))

    for i in range(0, height - sztf):
        j = len(b[i])
        drawx = (SizeW * 33 / 35) / width
        drawy = (SizeH * 33 / 35) / height
        for g in range(0, j):
            text.text((SizeW * 1 / 35 + drawx * g + 30,
                       SizeH * 1 / 35 + drawy * i + drawy * sztf + 30), str(b[i][g]), font=fnx,
                      fill=(0, 0, 0, 30))

    canvas.save(f"./output/{name}.png", "png")

    for i in range(0, len(c)):
        j = len(c[i])
        drawx = (SizeW * 33 / 35) / width
        drawy = (SizeH * 33 / 35) / height
        for g in range(0, j):
            if c[i][g] == 1:
                rect.rectangle(((SizeW * 1 / 35 + drawx * i + drawx * sztt, drawy * sztf + SizeH * 1 / 35 + drawy * g),
                                (SizeW * 1 / 35 + drawx * i + drawx * sztt + 110,
                                 drawy * sztf + SizeH * 1 / 35 + drawy * g + 110)),
                               fill=(0, 0, 0))

    canvas.save(f"./output/answer_{name}.png", "png")
    print(name)


def run(rows, columns, name):
    if rows == 0 or columns == 0:
        print(">0.")
        return 0

    nonoarray = []
    nonoarray_c_rows = []
    nonoarray_c_columns = []

    for i in range(0, rows):
        nonoarray_2 = []

        for j in range(0, columns):
            k = random.randrange(0, 2)
            nonoarray_2.append(k)

        nonoarray.append(nonoarray_2)

    for i in range(0, rows):
        nonoc = 0
        nonoca = []
        for j in range(0, columns):
            k = nonoarray[i][j]
            if k == 1:
                nonoc += 1
            else:
                nonoca.append(nonoc)
                nonoc = 0

            if j == columns - 1:
                nonoca.append(nonoc)

        nonoarray_c_rows.append(nonoca)

    for i in range(0, columns):
        nonoc = 0
        nonoca = []
        for j in range(0, rows):
            k = nonoarray[j][i]

            if k == 1:
                nonoc += 1
            else:
                nonoca.append(nonoc)
                nonoc = 0

            if j == rows - 1:
                nonoca.append(nonoc)

        nonoarray_c_columns.append(nonoca)

    nonoarray_c_rows = exczero(nonoarray_c_rows)
    nonoarray_c_columns = exczero(nonoarray_c_columns)

    ToImage(nonoarray_c_rows, nonoarray_c_columns, nonoarray, name)
