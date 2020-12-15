from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend
from .forms import FriendForm
from django.views.generic import ListView
from django.views.generic import DetailView

class FriendList(ListView):
  model = Friend

class FriendDetail(DetailView):
  model = Friend

def index(request):
  data = Friend.objects.all()
  params = {
    'title': 'Hello',
    'data': data
  }
  return render(request, 'hello/index.html', params)

#create model
def create(request):
  if(request.method == 'POST'):
    obj = Friend()
    friend = FriendForm(request.POST, instance=obj)
    friend.save()
    return redirect(to='/hello')
  params = {
    'title': 'Hello',
    'form': FriendForm(),
  }
  return render(request, 'hello/create.html', params)

def edit(request, num):
  obj = Friend.objects.get(id=num)
  if(request.method == 'POST'):
    friend = FriendForm(request.POST, instance=obj)
    friend.save()
    return redirect(to='/hello')
  params = {
    'title': 'Hello',
    'id': num,
    'form': FriendForm(instance=obj),
  }
  return render(request, 'hello/edit.html', params)

def delete(request, num):
  friend = Friend.objects.get(id=num)
  if(request.method == 'POST'):
    friend.delete()
    return redirect(to='/hello')
  params = {
    'title': 'Hello',
    'id': num,
    'obj': friend,
  }
  return render(request, 'hello/delete.html', params)

#class HelloView(TemplateView):
#
#  def __init__(self):
#    self.params = {
#      'title':'Hello',
#      'form': HelloForm(),
#      'result':None
#    }
#
#  def get(self, request):
#    return render(request, 'hello/index.html', self.params)
#
#  def post(self, request):
#    ch = request.POST.getlist('choice')
#    result = '<ol class="list-group"><b>selected:</b>'
#    for item in ch:
#      result += '<li class="list-group-item">' + item + '</li>'
#    result += '</ol>'
#    self.params['result'] = result
#    self.params['form'] = HelloForm(request.POST)
#    return render(request, 'hello/index.html', self.params)

#def form(request):
#  msg = request.POST['msg']
#  params = {
#    'title':'Hello/Form',
#    'msg':'こんにちは、' + msg + 'さん。',
#  }
#  return render(request, 'hello/index.html', params)