from django.core.management.base import BaseCommand, CommandError
from thuvienbk.models import Question , PhongThuVien, NguoiQuanLyThuVien,ChuyenNganhSinhVien,SinhVien,TheLoaiSach,Sach,SinhVienMuaSach,SinhVienMuonSach,DanhGiaSach
import datetime
import random
from django.contrib.auth.models import User

class Command(BaseCommand):



    def handle(self, *args, **options):
        
        PhongThuVien.objects.all().delete()
        NguoiQuanLyThuVien.objects.all().delete()
        ChuyenNganhSinhVien.objects.all().delete()
        SinhVien.objects.all().delete()
        TheLoaiSach.objects.all().delete()
        Sach.objects.all().delete()
        SinhVienMuaSach.objects.all().delete()
        SinhVienMuonSach.objects.all().delete()
        DanhGiaSach.objects.all().delete()

        p1=PhongThuVien(ma_so_phong='P101',so_luong_sach_toi_da_co_the_chua=100); p1.save();
        p2=PhongThuVien(ma_so_phong='P102',so_luong_sach_toi_da_co_the_chua=100); p2.save();


        quanly1=User.objects.create_user('quanly1', password='quanly1',is_superuser=True,is_staff=True)
        quanly1=NguoiQuanLyThuVien(user=quanly1, ma_so_quan_ly='quanly1',cmnd='CMND-0000001',ho_va_ten='NGUYEN VAN A',dia_chi_nha='diachi1',dob='1929-05-07',gioi_tinh='Nam',phong_thu_vien_quan_ly=p1); quanly1.save()
        quanly2=User.objects.create_user('quanly2', password='quanly2',is_superuser=True,is_staff=True)
        quanly2=NguoiQuanLyThuVien(user=quanly2, ma_so_quan_ly='quanly2',cmnd='CMND-0000002',ho_va_ten='NGUYEN VAN B',dia_chi_nha='diachi2',dob='1929-05-08',gioi_tinh='Nam',phong_thu_vien_quan_ly=p2); quanly2.save()


        cn1=ChuyenNganhSinhVien(ten_chuyen_nganh='KHMT'); cn1.save();
        cn2=ChuyenNganhSinhVien(ten_chuyen_nganh='Business'); cn2.save();

        sv1=User.objects.create_user('sv1', password='sv1')
        sv1=SinhVien(user=sv1, ma_so_sinh_vien='sv1',cmnd='CMND-0000003',ho_va_ten='TRAN VAN C',dia_chi_nha='diachi3',dob='1929-05-07',gioi_tinh='Nam',chuyen_nganh=cn1); sv1.save()
        sv2=User.objects.create_user('sv2', password='sv2')
        sv2=SinhVien(user=sv2, ma_so_sinh_vien='sv2',cmnd='CMND-0000004',ho_va_ten='TRAN VAN D',dia_chi_nha='diachi4',dob='1929-05-01',gioi_tinh='Nam',chuyen_nganh=cn2); sv2.save()

        tl1=TheLoaiSach(the_loai_sach='Khoa hoc');   tl1.save()
        tl2=TheLoaiSach(the_loai_sach='Nghe thuat'); tl2.save()

        sach1=Sach(1,ten_sach='Toan cao cap',tac_gia='tac gia 1',nam_xuat_ban='1999',the_loai=tl1,gia_ban='10000',so_luong_ton_kho=10,so_luong_da_cho_muon=2,so_luong_da_ban=2); sach1.save()
        sach2=Sach(2,ten_sach='Ve tranh',    tac_gia='tac gia 2',nam_xuat_ban='1999',the_loai=tl2,gia_ban='15000',so_luong_ton_kho=5, so_luong_da_cho_muon=2,so_luong_da_ban=2); sach2.save()

        sv_mua_sach_1=SinhVienMuaSach(sinh_vien=sv1,sach=sach1,ngay_mua='2010-01-01'); sv_mua_sach_1.save();
        sv_mua_sach_2=SinhVienMuaSach(sinh_vien=sv2,sach=sach2,ngay_mua='2010-01-02'); sv_mua_sach_2.save();

        sv_muon_sach_1=SinhVienMuonSach(sinh_vien=sv1,sach=sach1,ngay_muon='2010-01-01'); sv_muon_sach_1.save();
        sv_muon_sach_2=SinhVienMuonSach(sinh_vien=sv2,sach=sach2,ngay_muon='2010-01-02'); sv_muon_sach_2.save();

        danh_gia_sach1=DanhGiaSach(sinh_vien=sv1,sach=sach1,rating=4,comment='comment1'); danh_gia_sach1.save();
        danh_gia_sach2=DanhGiaSach(sinh_vien=sv2,sach=sach2,rating=5,comment='comment2'); danh_gia_sach2.save();

        print('data inserted')