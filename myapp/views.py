from django.shortcuts import render

# Create your views here.
def home(request):
      print('i am home view')
      return render(request, 'myapp/home.html')

def about(request):
      print('i am about view')

      return render(request, 'myapp/about.html')