from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    #return HttpResponse(
     #    """<h1>Welcome to Website Bro inka em chestham codding tappa ekkuvu aiythey dobbidhi code jagraktha </h1>
      #   <h5>Bavvundanna</h5>
       # <p>Mathu vadalara</p>""")
    plants=[
            {'name':'rose','price':100},
            {'name':'lily','price':100},
            {'name':'Tulip','price':'100'}
       ]
    message="go green"
    return render(request,'home.html',context={"plants":plants,"msg":message})
def index(request):
   return render(request,'index.html')
def contact(request):
   return render(request,'contact.html')

def nursery(request):
   plants=[
      {'name':'Rose','price':99},
      {'name':'lilly','price':85},
      {'name':'Tulip','price':100},
   ]
   message="prices"
   return render(request,'nursery.html',context={"plants":plants,"msg":message})
def base(request):
   return render(request,'base.html')
