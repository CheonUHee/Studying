from PIL import Image

img = Image.new('RGB', (512, 512))
pix = img.load()

# open 함수: 모드
# r == 읽기용, w == 쓰기용, b = binary 모드 
input_file = open('lena512.raw', 'rb')
output_file = open('lena512_1bit.raw', 'wb')

# 읽어오는 file의 크기가 큰 경우 메모리 부하가 크므로,
# 끊어서 불러오는 게 좋다 

# write용 buffer
b = bytearray(1)


for i in range(img.height * img.width // 8):
    # data는 bytes형..byte단위로 raster scan하여 한 줄로 씀
    # read()에 숫자를 넣으면 해당 byte만큼을 읽어옴
    data = input_file.read(8)
    # 1byte 크기의 int형 2진수
    b[0] = 0b00000000
    
    # little endian 방식: 작은 단위의 byte를 먼저 기록한다.
    # 1byte 단위의 저장은 상관 없지만, 2byte 이상은 byte order가 중요하다.

    # 비트연산
    # 비트 shift 연산자 << 가 먼저 실행된 후, 비트 or(|) 연산자가 실행되어 비트가 b[0]에 누적되면서 저장됨
    for j in range(8):
        b[0] |= 0b00000001 << j if data[j] > 127 else 0b00000000
    output_file.write(b)

input_file.close()
output_file.close()