from django.shortcuts import render
from adminn.models import gudang_ikan,harga_ikan
# Create your views here.
def penerimaan(request):
	if request.method == 'POST':
		gudang_ikan.objects.create(
		juragan = request.POST['juragan'],
    	berat = request.POST['berat'],
    	id_harga = harga_ikan.objects.get(id=request.POST['jenis']),
    	),
	else :
		print("gagal nih"),
	model = gudang_ikan.objects.all()
	harga = harga_ikan.objects.all()
	context = {
	'judul' : 'Gudang Ikan',
	'nav':[
		['/penerimaan','Gudang Ikan'],
	],
	'ikan':model,
	'harga':harga,
	}
	return render(request,'penerimaan/ikan.html',context)
def pembersihan(request):
	model = gudang_ikan.objects.all()
	context = {
	'judul' : 'Gudang Ikan',
	'nav':[
		['/pembersihan','Gudang Ikan'],
	],
	'ikan':model
	}
	return render(request,'pembersihan/ikan.html',context)
