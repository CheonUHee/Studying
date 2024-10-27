from PIL import Image

img = Image.new(mode='RGB', size=(512, 512))
file = open('lena512_1bit.raw', 'rb')

pix = img.load()
# read용 buffer
unpack = bytearray()

for i in range(img.height * img.width // 8):
    # 비트 연산을 위해 byte형을 int형으로 변환
    data = int.from_bytes(file.read(1), byteorder='little')

    for j in range(8):
        # 하위 비트를 하나씩 추출하기 위해, 1과 AND 연산을 하여 하위 비트를 추출하기
        # 추출한 비트가 1이면 255를 unpack에 추가, 추출한 비트가 0이면 0을 unpack에 추가
        unpack.append(255 if data & 0b00000001 == 1 else 0)
        # 다음 칸의 비트를 추출하기 위해 data 비트를 오른쪽으로 1칸 이동
        data >>= 1

file.close()

for y in range(img.height):
   for x in range(img.width):
        # unpack 위치 인덱싱
        # size의 너비가 512이므로 0 ~ 511이 한 줄이다.
        # 따라서 다음 줄로 이동하기 위해 size.width만큼을 더해야 함
        # Image의 mode가 RGB이므로 (R,G,B)
        pix[x, y] = (unpack[y * img.width + x], unpack[y * img.width + x], unpack[y * img.width + x])

img.show()