from django.shortcuts import render
from .models import harga_ikan,gudang_ikan,area_ikan,penjualan,userr

# Create your views here.
def index(request):
	model = gudang_ikan.objects.all()
	context = {
	'judul' : 'Gudang Ikan',
	'nav':[
		['/','Gudang Ikan'],
		['/jual','Penjualan Ikan'],
		['/harga','Harga Ikan'],
        ['/area','Area Ikan'],
        ['/user','Data Pengguna'],
	],
	'ikan':model
	}
	return render(request,'admin/ikan.html',context)

def jual(request):
	model = penjualan.objects.all()
	context = {
		'judul' : 'Penjualan Ikan',
		'nav':[
			['/','Gudang Ikan'],
			['/jual','Penjualan Ikan'],
			['/harga','Harga Ikan'],
            ['/area','Area Ikan'],
            ['/user','Data Pengguna'],
		],
		'penjualan':model
	}
	return render(request,'admin/penjualan.html',context)

def harga(request):
	if request.method == 'POST':
		harga_ikan.objects.create(
		jenis_ikan = request.POST['jenis'],
    	harga_per_kg = request.POST['harga'],
    	),
	else :
		print("gagal nih"),

	model = harga_ikan.objects.all()
	context = {
		'judul' : 'Harga Ikan',
		'nav':[
			['/','Gudang Ikan'],
			['/jual','Penjualan Ikan'],
			['/harga','Harga Ikan'],
            ['/area','Area Ikan'],
            ['/user','Data Pengguna'],
		],
		'harga':model
	}
	return render(request,'admin/harga.html',context)

def area(request):
	if request.method == 'POST':
		area_ikan.objects.create(
  		area_ikan = request.POST['area'],
    	)
	else :
		
		print("gagal nih"),

	model = area_ikan.objects.all()
	context = {
		'judul' : 'Area Ikan',
		'nav':[
			['/','Gudang Ikan'],
			['/jual','Penjualan Ikan'],
			['/harga','Harga Ikan'],
            ['/area','Area Ikan'],
            ['/user','Data Pengguna'],
		],
		'area':model
	}
	return render(request,'admin/area.html',context)

def user(request):
	if request.method == 'POST':
		userr.objects.create(
  		nama = request.POST['nama'],
		alamat = request.POST['alamat'],
		username = request.POST['username'],
		password = request.POST['password'],
		jabatan = request.POST['jenis'],
    	)
	else :
		print("gagal nih"),
	model = userr.objects.all()
	context = {
		'judul' : 'Data Pengguna',
		'nav':[
			['/','Gudang Ikan'],
			['/jual','Penjualan Ikan'],
			['/harga','Harga Ikan'],
            ['/area','Area Ikan'],
            ['/user','Data Pengguna'],
		],
		'user':model,
		'pengguna':[
			['1','Administrator'],
			['2','Karyawan Penerimaan'],
			['3','Karyawan Pembersihan'],
			['4','Karyawan Penjualan'],
		],
	}
	return render(request,'admin/user.html',context)