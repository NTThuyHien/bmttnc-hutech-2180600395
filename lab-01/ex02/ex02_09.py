# Hàm tìm số nguyên tố

def tim_so_nguyen_to(n):
    # Kiểm tra nếu n <= 1
    if n <= 1:
        return False

    # Duyệt từ 2 đến căn bậc hai của n
    for i in range(2, int(n ** 0.5) + 1):
        # Kiểm tra nếu n chia hết cho i
        if n % i == 0:
            return False

    # Nếu không chia hết cho bất kỳ số nào từ 2 đến căn bậc hai của n
    return True


# Nhập số nguyên từ người dùng
number = int(input("Nhập vào số cần kiểm tra: "))

# Kiểm tra và in kết quả
if tim_so_nguyen_to(number):
    print(number, "là số nguyên tố.")
else:
    print(number, "không phải là số nguyên tố.")