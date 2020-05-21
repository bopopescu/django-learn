from django.shortcuts import render
from adminn.models import gudang_ikan,penjualan
# Create your views here.
def index(request):
	model = gudang_ikan.objects.all()
	context = {
	'judul' : 'Gudang Ikan',
	'nav':[
		['/penjualan','Gudang Ikan'],
		['/penjualan/jual','Penjualan Ikan'],
	],
	'ikan':model
	}
	return render(request,'admin/ikan.html',context)

def jual(request):
	model = penjualan.objects.all()
	gudang = gudang_ikan.objects.all()
	context = {
		'judul' : 'Penjualan Ikan',
		'nav':[
		['/penjualan','Gudang Ikan'],
		['/penjualan/jual','Penjualan Ikan'],
		],
		'penjualan':model,
		'gudang':gudang
	}
	return render(request,'penjualan/penjualan.html',context)