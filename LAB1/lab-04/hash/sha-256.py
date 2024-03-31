import hashlib

def calculate_sha256_hash(data):
  sha256_hash = hashlib.sha256()
  sha256_hash.update(data.encode('utf-8')) # Chuyển đổi dữ liệu thành bytes và cập nhật vào đối tượng hash
 
  return sha256_hash.hexdigest() # Trả về biểu diễn hex chuỗi hash

# Nhập dữ liệu để hash bằng SHA-256
data_to_hash = input("Nhập dữ liệu để hash bằng SHA-256: ")
# Tính toán giá trị hash
hash_value = calculate_sha256_hash(data_to_hash)
# In ra giá trị hash
print("Giá trị hash SHA-256:", hash_value)