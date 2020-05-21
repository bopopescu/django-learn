from django.db import models

# Create your models here.
class harga_ikan(models.Model):
    jenis_ikan = models.TextField()
    harga_per_kg = models.IntegerField()

class area_ikan(models.Model):
    area_ikan = models.TextField()

class gudang_ikan(models.Model):
    tanggal_masuk = models.DateField(auto_now_add=True)
    juragan = models.CharField(max_length=50)
    berat = models.IntegerField()
    id_harga = models.ForeignKey('harga_ikan',on_delete=models.CASCADE)
    id_area = models.ForeignKey('area_ikan',on_delete=models.CASCADE,null = True)

class userr(models.Model):
    nama = models.CharField(max_length=50)
    alamat = models.TextField()
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    status = models.CharField(max_length=20, default="Aktif")
    jabatan = models.CharField(max_length=22)


class penjualan(models.Model):
    tanggal_penjualan=models.DateField(auto_now_add=True)
    total_berat = models.IntegerField()
    total_harga = models.IntegerField()
    id_ikan = models.ForeignKey('gudang_ikan',on_delete=models.CASCADE)
