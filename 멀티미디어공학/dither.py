from PIL import Image

img = Image.new(mode='RGB', size=(512, 512))

file = open('lena512.raw', 'rb')
data = file.read()
file.close()

pix = img.load()

# 4x4 dither matrix
d = (
    (0, 8, 2, 10),
    (12, 4, 14, 6),
    (3, 11, 1, 9),
    (15, 7, 13, 5)
)

for y in range(img.height):
    for x in range(img.width):
        # dither matrix 사이즈가 4x4이기 때문에 4의 나머지를 구함 (모듈로 연산)
        i = x % 4
        j = y % 4
        # dither matrix 값은 0~15 사이이므로
        # 8비트(256)에 맞춰 dither matrix 값을 스케일링 해야 함 -> 256/16 = 16을 곱하기
        value = 255 if data[y*img.width + x] > d[j][i]*16 else 0
        pix[x, y] = (value, value, value)

img.show()

# from PIL import Image

# img = Image.new(mode='RGB', size=(512, 512))

# file = open('lena512.raw', 'rb')
# data = file.read()
# file.close()

# pix = img.load()

# # 2x2 dither matrix
# d = (
#     (0, 2),
#     (3, 1),
# )

# for y in range(img.height):
#     for x in range(img.width):
#         # dither matrix 사이즈가 2x2이기 때문에 2의 나머지를 구함 (모듈로 연산)
#         i = x % 2
#         j = y % 2
#         # dither matrix 값은 0~3 사이이므로
#         # 8비트(256)에 맞춰 dither matrix 값을 스케일링 해야 함 -> 256/4 = 64를 곱하기
#         value = 255 if data[y*img.width + x] > d[j][i]*64 else 0
#         pix[x, y] = (value, value, value)

# img.show()