from django.shortcuts import render, get_object_or_404
from .models import ChaiVariety

# Create your views here.
def test_home(request):
    chais = ChaiVariety.objects.all()  #this returns in an array format
    return render(request, "testapp/testindex.html", {'chais' : chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk = chai_id)
    return render(request, "testapp/chai_detail.html", {"chai" : chai})