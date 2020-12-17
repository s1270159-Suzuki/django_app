from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend, Message
from .forms import FriendForm, MessageForm
from .forms import FindForm
from .forms import CheckForm
from django.views.generic import ListView
from django.views.generic import DetailView
from django.db.models import Q
from django.db.models import Count,Sum,Avg,Min,Max
from django.core.paginator import Paginator

class FriendList(ListView):
  model = Friend

class FriendDetail(DetailView):
  model = Friend

def index(request, num=1):
  data = Friend.objects.all()
  page = Paginator(data, 3)
  params = {
    'title': 'Hello',
    'message': '',
    'data': page.get_page(num),
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

def find(request):
  if(request.method == 'POST'):
    msg = request.POST['find']
    form = FindForm(request.POST)
    sql = 'select * from hello_friend'
    if(msg != ''):
      sql += ' where ' + msg
    data = Friend.objects.raw(sql)
    msg = sql
  else:
    msg = 'search words...'
    form = FindForm()
    data = Friend.objects.all()
  params = {
    'title': 'Hello',
    'message': msg,
    'form': form,
    'data': data,
  }
  return render(request, 'hello/find.html', params)

def check(request):
  params = {
    'title': 'Hello',
    'message':'check validation.',
    'form': FriendForm(),
  }
  if(request.method == 'POST'):
    obj = Friend()
    form = FriendForm(request.POST, instance=obj)
    params['form'] = form
    if(form.is_valid()):
      params['message'] = 'OK!'
    else:
      params['message'] = 'no good.'
  return render(request, 'hello/check.html', params)

def message(request, page=1):
  if(request.method == 'POST'):
    obj = Message()
    form = MessageForm(request.POST, instance=obj)
    form.save()
  data = Message.objects.all().reverse()
  pagination = Paginator(data, 5)
  params = {
    'title': 'Message',
    'form': MessageForm(),
    'data': pagination.get_page(page),
  }
  return render(request, 'hello/message.html', params)

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