from django.shortcuts import render,redirect
from .models import Product
from django.http import HttpResponse
from django.views import View

class Home(View):
    def get(self,request):
        return render(request,'home.html')
class InsertInput(View):
    def get(self,request):
        return render(request,'productinput.html')
class Insert(View):
    def get(self,request):
        p_id=int(request.GET["t1"])
        p_name=request.GET["t2"]
        p_cost=float(request.GET["t3"])
        p_mfd=request.GET["t4"]
        p=Product(pid=p_id,pname=p_name,pcost=p_cost,pmfd=p_mfd)
        p.save()
        return HttpResponse("product inserted successfully")
class Display(View):
    def get(self,request):
        qs=Product.objects.all()
        condic={"records":qs}
        return render(request,'display.html',context=condic)

class DeleteInput(View):
    def get(self,request):
        qs=Product.objects.all()
        condic={"records":qs}
        return render(request,'deleteinput.html',context=condic)

class Delete(View):
    def get(self,request):
        p_id=int(request.GET["t1"])
        p=Product.objects.get(pid=p_id)
        p.delete()
        return redirect('/productapp/display')

class UpdateInput(View):
    def get(self,request):
        qs = Product.objects.all()
        condic = {"records": qs}
        return render(request, 'updateinput.html', context=condic)

class UpdateDetails(View):
    def get(self,request):
        p_id=int(request.GET["t1"])
        prod=Product.objects.get(pid=p_id)
        condic={'rec':prod}
        return render(request,'update.html',context=condic)

class Update(View):
    def get(self,request):
        p_id=int(request.GET["t1"])
        prod=Product.objects.get(pid=p_id)
        prod.pname=request.GET["t2"]
        prod.pcost=float(request.GET["t3"])
        prod.pmfdt=request.GET["t4"]
        prod.save()
        return redirect('/productapp/display')




# Create your views here.
