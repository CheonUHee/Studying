from PIL import Image

img = Image.new(mode='RGB', size=(512, 512))

file = open('lena512.raw', 'rb')
# data는 bytes형//file을 byte단위로 raster scan하여 한 줄로 씀
# read()에 숫자를 넣으면 해당 byte만큼을 출력
data = file.read()
file.close() # close로 종료해서 리소스 반환

# load == pixel accessor
pix = img.load()


for y in range(img.height):
    for x in range(img.width):
        # 1bit처럼 만들기
        ## 0 ~ 255 총 256단계가 있으므로 반절은 on(1), 다른 반절은 off(0)로 설정
        temp = 255 if data[y*img.width + x] > 127 else 0
        
        # data 위치 인덱싱
        ## size의 너비가 512이므로 0 ~ 511이 한 줄이다.
        ## 다음 칸으로 이동하기 위해 size.width만큼을 더해야 함
        ## mode가 RGB이므로 (R,G,B)
        pix[x, y] = (temp, temp, temp)

img.show()


# 단, 이 방법은 8bits 파일을 1bit처럼 보이게 만든 것일 뿐이다