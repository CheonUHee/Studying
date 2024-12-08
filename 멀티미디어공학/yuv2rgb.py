from PIL import Image

img = Image.new(mode='RGB', size=(352, 288))
height, width = img.height, img.width
# YUV420 파일의 데이터 구조가
# 한 프레임당 Y(352*288), U(176*144), V(176*144) 순으로 구성되므로
# 한 프레임당 1.5*너비*높이만큼 데이터가 존재한다.
frame_size = height * width * 3 // 2
frame_num = int(input('원하는 프레임 번호(0~14)를 입력하세요.: '))

file = open('bus.yuv', 'rb')
# seek 함수를 이용해 파일에서 읽고자 하는 시작점을 정한다.
file.seek(frame_num * frame_size)
# 프레임 크기만큼만 data에 저장
data = file.read(frame_size)
file.close()

pix = img.load()


# YUV420을 RGB로 변환하기
for y in range(height):
    for x in range(width):
        # YUV420 인덱싱

        Y = data[y * width + x]
        # U값은 Y 데이터 이후에 나오므로 height*width만큼 더하기
        # Y에 비해 해상도가 높이/2, 너비/2 작으므로 Y와 맞추기 위해 2씩 나누기
        U = data[(height*width) + (y//2) * (width//2) + (x//2)]
        # V값은 U 데이터 이후에 나오므로 height*width*5//4만큼 더하기
        # Y에 비해 해상도가 높이/2, 너비/2 작으므로 Y와 맞추기 위해 2씩 나누기
        V = data[(height*width*5//4) + (y//2) * (width//2) + (x//2)]
        
        R = int(1.164 * (Y-16) + 1.596 * (V-128))
        G = int(1.164 * (Y-16) - 0.391 * (U-128) - 0.813 * (V-128))
        B = int(1.164 * (Y-16) + 2.018 * (U-128))
        
        pix[x, y] = (R, G, B)

img.show()