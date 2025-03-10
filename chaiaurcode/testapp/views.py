from django.shortcuts import render, get_object_or_404
from .models import ChaiVariety, Store
from .forms import chaivarietyform

# Create your views here.
def test_home(request):
    chais = ChaiVariety.objects.all()  #this returns in an array format
    return render(request, "testapp/testindex.html", {'chais' : chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk = chai_id)
    return render(request, "testapp/chai_detail.html", {"chai" : chai})

def chai_stores(request):
    stores = None
    if request.method == "POST":
        form = chaivarietyform(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_variety']
            stores = Store.objects.filter(chai_varieties=chai_variety)
    else:
        form = chaivarietyform()
    return render(request, "testapp/chai_stores.html", {'form': form, 'stores': stores})