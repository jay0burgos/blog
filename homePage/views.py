from django.shortcuts import render, redirect
from .models import message, comment
from home.models import User
from django.http import HttpResponsePermanentRedirect

#TODO put in a log out method that redirects to logout
#TODO after setting up the updatting through an unorder 
        #list, do some ajax

def index(request):
    if not 'user_id' in request.session:
        return redirect('/')
    else:
        content = {
            'user': User.objects.get(id = request.session['user_id']),
            'messages': message.objects.all(),
            'comments': comment.objects.all()
        }
        return render(request, 'homePage/index.html', content)
def create(request):
    if not 'user_id' in request.session:
        return redirect('/')
    else:
        user_in_session = User.objects.get(id = request.session['user_id'])
        print(user_in_session)
        message.objects.postMessage(request.POST, user_in_session)
        return redirect('/')
def logout(request):
    return redirect('/logout')

