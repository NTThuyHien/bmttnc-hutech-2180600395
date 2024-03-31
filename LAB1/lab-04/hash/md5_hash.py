def left_rotate(value, shift):
    return ((value << shift  |  (value >> (32 - shift)))) & 0xFFFFFFFF

def md5(message):
    # Khởi tạo các biến ban đầu
    a = 0x67452301
    b = 0xEFCDAB69
    c = 0x98BADCFE
    d = 0x10325476

    # Tiền xử lý chuỗi văn bản
    original_length = len(message)
    message += b'\x80'
    while len(message) % 64 != 56:
        message += b'\x00'
    message += original_length.to_bytes(8, 'little')

    # Chia chuỗi thành các block 512-bit
    for i in range(0, len(message), 64):
        block = message[i:i+64]
        words = [int.from_bytes(block[j:j+4], 'little') for j in range(0, 64, 4)]

        # Vòng lặp chính của thuật toán MD5
        a0, b0, c0, d0 = a, b, c, d
        for j in range(64):
            if j < 16:
                f = (b & c) | ((~b) & d)
                g = j
            elif j < 32:
                f = (b & d) | ((~b) & c)
                g = (5*j + 1) % 16
            elif j < 48:
                f = b ^ c ^ d
                g = (3*j + 5) % 16
            else:
                f = c ^ (b | (~d))
                g = (7*j) % 16
          
            temp = d
            d = c
            c = b
            b = b + left_rotate((a + f + 0x5A827999 + words[g]) & 0xFFFFFFFF, 3)
            a = temp
    
        a = (a + a0) & 0xFFFFFFFF
        a = (a + b0) & 0xFFFFFFFF
        a = (a + c0) & 0xFFFFFFFF
        a = (a + d0) & 0xFFFFFFFF
    # Trả về giá trị băm MD5
    return '{:08x}{:08x}{:08x}{:08x}'.format(a, b, c, d)

# Nhập chuỗi cần băm
input_string = input("Nhập chuỗi cần băm: ")
# Tính toán mã băm MD5
md5_hash = md5(input_string.encode('utf-8'))

# In ra mã băm MD5
print("Mã băm MD5 của chuỗi '{}' là: {}".format(input_string, md5_hash))