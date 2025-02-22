from django.shortcuts import render

# Create your views here.
def test_home(request):
    return render(request, "testapp/testindex.html")