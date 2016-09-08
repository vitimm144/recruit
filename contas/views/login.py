from django.views import View
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect


class Login(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return render_to_response('login.html')

    def post(self, request, *args, **kwargs):

        logout(request)
        email = password = ''
        if request.POST:
            username = request.POST['email']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
