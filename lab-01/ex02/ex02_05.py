so_gio_lam = float(input("Nhập số giờ làm mỗi tuần:"))
luong_gio = float(input("Nhập thù lap trên mỗi giờ làm tiêu chuẩn:"))
gio_tieu_chuan = 44 # số giờ làm chuẩn mỗi tuần
gio_Vuot_chuan = max(0,so_gio_lam - gio_tieu_chuan) #số giờ làm vượt chuẩn mỗi tuần
thuc_linh = gio_tieu_chuan * luong_gio + gio_Vuot_chuan * luong_gio * 1.5 # Tính tổng thu nhập
print(f"số tiền thực lĩnh của nhân viên:{thuc_linh}")