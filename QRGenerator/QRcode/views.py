from django.shortcuts import render
from qrcode import *

# Create your views here.
data = None
def qrcode_fun(request):
    global data
    if request.method == 'POST':
        data=request.POST['data']
        img = make(data)
        img.save("static/images/test.png")
    else:
        pass
    return render(request,"index.html",{'data':data})