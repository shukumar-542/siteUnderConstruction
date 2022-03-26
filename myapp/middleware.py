from urllib import response
from django.shortcuts import HttpResponse, render
class underConstructionMiddleware:
      def __init__(self, get_response):
            self.get_response = get_response

      def __call__(self, request):
            print('after call view')
            # response = self.get_response(request)
            response = render(request,'myapp/construction.html')
            print('before call view')
            return response