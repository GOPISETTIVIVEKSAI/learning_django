from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    #return HttpResponse(
     #    """<h1>Welcome to Website Bro inka em chestham codding tappa ekkuvu aiythey dobbidhi code jagraktha </h1>
      #   <h5>Bavvundanna</h5>
       # <p>Mathu vadalara</p>""")
    return render(request, 'home.html')
