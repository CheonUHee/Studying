from PIL import Image

img = Image.new(mode='RGB', size=(512, 512))

file = open('lena512.raw', 'rb')
# data는 bytes형//file을 byte단위로 raster scan하여 한 줄로 씀
# 숫자를 넣으면 해당 byte만큼을 출력
data = file.read()
file.close() # close로 종료해서 리소스 반환

# load == pixel accessor
pix = img.load()


for y in range(img.height):
    for x in range(img.width):
        # data 위치 인덱싱
        # size의 너비가 512이므로 0 ~ 511이 한 줄이다.
        # 다음 칸으로 이동하기 위해 size.width만큼을 더해야 함
        # mode가 RGB이므로 (R,G,B)
        pix[x, y] = (data[y*img.width + x], data[y*img.width + x], data[y*img.width + x])

img.show()