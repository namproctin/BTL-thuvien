import datetime

from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text



class PhongThuVien(models.Model):
    ma_so_phong = models.CharField(max_length=100,unique=True) 
    so_luong_sach_toi_da_co_the_chua= models.IntegerField(default=100)
    

class NguoiQuanLyThuVien(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    cmnd= models.CharField(max_length=200,unique=True)
    ho_va_ten = models.CharField(max_length=200)
    dob = models.DateField(blank=True, null=True)   
    gioi_tinh = models.CharField(max_length=3, choices=[('Nam','Nam'),('Nu','Nu')], default='Nam')
    dia_chi_nha = models.CharField(max_length=300)
    ma_so_quan_ly = models.CharField(max_length=100, unique=True) 
    phong_thu_vien_quan_ly = models.OneToOneField(
        PhongThuVien,
        on_delete=models.CASCADE
    )

class ChuyenNganhSinhVien(models.Model):
    ten_chuyen_nganh = models.CharField(max_length=100,unique=True) 


class SinhVien(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    cmnd= models.CharField(max_length=200,unique=True)
    ho_va_ten = models.CharField(max_length=200)
    dob = models.DateField(blank=True, null=True)   
    gioi_tinh = models.CharField(max_length=3, choices=[('Nam','Nam'),('Nu','Nu')], default='Nam')
    dia_chi_nha = models.CharField(max_length=300)

    ma_so_sinh_vien = models.CharField(max_length=100, unique=True) 
    chuyen_nganh = models.ForeignKey(ChuyenNganhSinhVien, on_delete=models.CASCADE)

class TheLoaiSach(models.Model): 
    the_loai_sach = models.CharField(max_length=100) 


class Sach(models.Model):
    ten_sach = models.CharField(max_length=100) 
    tac_gia  = models.CharField(max_length=100) 
    nam_xuat_ban = models.IntegerField(default=0)
    the_loai = models.ForeignKey(TheLoaiSach, on_delete=models.CASCADE)
    gia_ban = models.IntegerField(default=0) 
    so_luong_ton_kho = models.IntegerField(default=0) 
    so_luong_da_cho_muon = models.IntegerField(default=0) 
    so_luong_da_ban = models.IntegerField(default=0) 



class SinhVienMuaSach(models.Model):
    sinh_vien = models.ForeignKey(SinhVien, on_delete=models.CASCADE)
    sach= models.ForeignKey(Sach, on_delete=models.CASCADE)
    ngay_mua = models.DateTimeField()

class SinhVienMuonSach(models.Model):
    sinh_vien = models.ForeignKey(SinhVien, on_delete=models.CASCADE)
    sach= models.ForeignKey(Sach, on_delete=models.CASCADE)
    ngay_muon = models.DateTimeField()

class DanhGiaSach(models.Model):
    sinh_vien = models.ForeignKey(SinhVien, on_delete=models.CASCADE)
    sach= models.ForeignKey(Sach, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0,validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    comment = models.CharField(max_length=100)