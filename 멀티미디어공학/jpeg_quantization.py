# 학과: 화학공학과, 학번: 2018114044, 성명: 황수본
# 멀티미디어공학 13-2주차 과제

import math
from PIL import Image

###
# 1) lena512.raw 영상을 읽어서 화면에 디스플레이
###

original_img = Image.new(mode='RGB', size=(512, 512))
height, width = original_img.height, original_img.width

file = open('lena512.raw', 'rb')
data = file.read()
file.close()

pix = original_img.load()

for y in range(height):
    for x in range(width):
        # data 위치 인덱싱
        # size의 너비가 512이므로 0 ~ 511이 한 줄이다.
        # 다음 칸으로 이동하기 위해 size.width만큼을 더해야 함
        # mode가 RGB이므로 (R,G,B)
        pix[x, y] = (data[y*width + x], data[y*width + x], data[y*width + x])

original_img.show()


###
# 2) 표준문서 Annex A.3.3 FDCT and IDCT (informative) 수식을 이용하여 8 x 8 block based Forward DCT 를 수행
###

# RGB를 YUV420으로 변환하기
y_data = [0] * (height * width)
u_data = [0] * ((height // 2) * (width // 2))
v_data = [0] * ((height // 2) * (width // 2))


for i in range(len(data)):
    R, G, B = data[i], data[i], data[i]
    
    Y = int(0.257 * R + 0.504 * G + 0.098 * B + 16)
    U = int(-0.148 * R - 0.291 * G + 0.439 * B + 128)
    V = int(0.439 * R - 0.368 * G - 0.071 * B + 128)

    y_data[i] = Y
    u_data[i // 4] = U
    v_data[i // 4] = V



# 8x8 블록으로 나누는 함수
def divide_blocks(data, height, width, block_size=8):
    blocks = []
    # by, bx는 각각 현재 블록의 세로, 가로 방향 시작 위치
    for by in range(0, height, block_size):
        for bx in range(0, width, block_size):
            block = [data[(by + y) * width + (bx + x)] for y in range(block_size) for x in range(block_size)]
            # 1D 데이터를 2D로 변환
            blocks.append([block[i:i + block_size] for i in range(0, len(block), block_size)])
    return blocks

# Forward DCT 수행 (8x8 블록 단위)
def Foward_DCT(block):
    # block_size = 8
    coeff = [[0] * 8 for _ in range(8)]
    
    for u in range(8):
            for v in range(8):
                # 시그마 계산
                sum_value = 0
                for x in range(8):
                    for y in range(8):
                        sum_value += block[x][y] * math.cos(((2 * x + 1) * u * math.pi) / 16) * math.cos(((2*y + 1) * v * math.pi) / 16)

                # C_u, C_v 계산
                C_u = math.sqrt(1 / 2) if u == 0 else 1
                C_v = math.sqrt(1 / 2) if v == 0 else 1
                coeff[u][v] = 0.25 * C_u * C_v * sum_value
    
    return coeff
    
# Y 데이터를 블록으로 나누기
y_blocks = divide_blocks(y_data, height, width)

# Y 데이터에 FDCT 적용
y_fdct = [Foward_DCT(block) for block in y_blocks]


###
# 3) 표준문서 Annex K.1 Table K.1 Luminance quantization table을 사용하여 위의 DCT Coefficients를 Quantization 수행 (Annex A.3.4 Rounding Operation 준수)
###

Luminance_quantization_table = [
    [16, 11, 10, 16, 24, 40, 51, 61],
    [12, 12, 14, 19, 26, 58, 60, 55],
    [14, 13, 16, 24, 40, 57, 69, 56],
    [14, 17, 22, 29, 51, 87, 80, 62],
    [18, 22, 37, 56, 68, 109, 103, 77],
    [24, 35, 55, 64, 81, 104, 113, 92],
    [49, 64, 78, 87, 103, 121, 120, 101],
    [72, 92, 95, 98, 112, 100, 103, 99]
]

# 8x8 DCT block에 양자화 수행
def quantization(blocks):
    quantized_blocks = []
    for block in blocks:
        quantized_block = [[0] * 8 for _ in range(8)]
        for u in range(8):
            for v in range(8):
                quantized_block[u][v] = round(block[u][v] / Luminance_quantization_table[u][v])
        quantized_blocks.append(quantized_block)  

    return quantized_blocks

quantized_y = quantization(y_fdct)


###
# 4) Quantization 을 수행한 DCT Coefficients 를 위의 Q-table를 이용하여 De-Quantization을 수행
###

def dequantization(blocks):
    dequantized_blocks = []
    for block in blocks:
        dequantized_block = [[0] * 8 for _ in range(8)]
        for u in range(8):
            for v in range(8):
                dequantized_block[u][v] = block[u][v] * Luminance_quantization_table[u][v]
        dequantized_blocks.append(dequantized_block)  

    return dequantized_blocks

dequantized_y = dequantization(quantized_y)


###
# 5) De-Q 데이터를 8 x 8 block based Inverse DCT 를 수행
###

def Inverse_DCT(block):
    coeff_idct = [[0] * 8 for _ in range(8)]
    
    for x in range(8):
            for y in range(8):
                # 시그마 계산
                sum_value = 0
                for u in range(8):
                    for v in range(8):
                        # C_u, C_v 계산
                        C_u = math.sqrt(1 / 2) if u == 0 else 1
                        C_v = math.sqrt(1 / 2) if v == 0 else 1
                
                        sum_value += C_u * C_v * block[u][v] * math.cos(((2 * x + 1) * u * math.pi) / 16) * math.cos(((2*y + 1) * v * math.pi) / 16)

                coeff_idct[x][y] = 0.25 * sum_value
    
    return coeff_idct


# Y 데이터에 IDCT 적용
y_idct = [Inverse_DCT(block) for block in dequantized_y]


###
# 6) 최종 결과를 화면에 디스플레이
###

new_img = Image.new(mode='RGB', size=(512, 512))
new_pix = new_img.load()

# 8x8 블록 데이터를 1D 배열로 변환
def blocks_to_1D(blocks, height, width, block_size=8):
    data = [0] * (height * width)
    block_index = 0

    for by in range(0, height, block_size):
        for bx in range(0, width, block_size):
            block = blocks[block_index]
            block_index += 1
            for y in range(block_size):
                for x in range(block_size):
                    data[(by + y) * width + (bx + x)] = block[y][x]

    return data

y_data_new = blocks_to_1D(y_idct, height, width)

# YUV420을 RGB로 변환하기
for i in range(height):
    for j in range(width):
        Y = y_data_new[i * width + j]
        U = u_data[(i//2) * (width//2) + (j//2)]
        V = v_data[(i//2) * (width//2) + (j//2)]

        R = int(1.164 * (Y-16) + 1.596 * (V-128))
        G = int(1.164 * (Y-16) - 0.391 * (U-128) - 0.813 * (V-128))
        B = int(1.164 * (Y-16) + 2.018 * (U-128))

        new_pix[j, i] = (R, G, B)

new_img.show()