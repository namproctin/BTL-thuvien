from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Question , PhongThuVien, NguoiQuanLyThuVien,ChuyenNganhSinhVien,SinhVien,TheLoaiSach,Sach,SinhVienMuaSach,SinhVienMuonSach,DanhGiaSach



class PhongThuVienAdmin(admin.ModelAdmin):
    list_display = ('id','ma_so_phong', 'so_luong_sach_toi_da_co_the_chua')

class NguoiQuanLyThuVienAdmin(admin.ModelAdmin):
    list_display = ('id','ma_so_quan_ly','cmnd','ho_va_ten','dob','gioi_tinh','dia_chi_nha','phong_thu_vien_quan_ly')

class ChuyenNganhSinhVienAdmin(admin.ModelAdmin):
    list_display = ('id','ten_chuyen_nganh')
    
class SinhVienAdmin(admin.ModelAdmin):
    list_display = ('id','ma_so_sinh_vien','chuyen_nganh','cmnd','ho_va_ten','dob','gioi_tinh','dia_chi_nha')

class TheLoaiSachAdmin(admin.ModelAdmin):
    list_display = ('id','the_loai_sach')

class SachAdmin(admin.ModelAdmin):
    list_display = ('id','ten_sach','tac_gia','nam_xuat_ban','the_loai','gia_ban','so_luong_ton_kho','so_luong_da_cho_muon','so_luong_da_ban')


class SinhVienMuaSachAdmin(admin.ModelAdmin):
    list_display = ('id','sinh_vien','sach','ngay_mua')


class SinhVienMuonSachAdmin(admin.ModelAdmin):
    list_display = ('id','sinh_vien','sach','ngay_muon')

class DanhGiaSachAdmin(admin.ModelAdmin):
    list_display = ('id','sinh_vien','sach','rating','comment')

admin.site.register(PhongThuVien, PhongThuVienAdmin)
admin.site.register(NguoiQuanLyThuVien, NguoiQuanLyThuVienAdmin)
admin.site.register(ChuyenNganhSinhVien, ChuyenNganhSinhVienAdmin)
admin.site.register(SinhVien, SinhVienAdmin)
admin.site.register(TheLoaiSach, TheLoaiSachAdmin)
admin.site.register(Sach, SachAdmin)
admin.site.register(SinhVienMuaSach, SinhVienMuaSachAdmin)
admin.site.register(SinhVienMuonSach, SinhVienMuonSachAdmin)
admin.site.register(DanhGiaSach, DanhGiaSachAdmin)





