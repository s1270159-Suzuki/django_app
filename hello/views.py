from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloForm

class HelloView(TemplateView):

  def __init__(self):
    self.params = {
      'title':'Hello',
      'form': HelloForm(),
      'result':None
    }

  def get(self, request):
    return render(request, 'hello/index.html', self.params)

  def post(self, request):
    ch = request.POST.getlist('choice')
    result = '<ol class="list-group"><b>selected:</b>'
    for item in ch:
      result += '<li class="list-group-item">' + item + '</li>'
    result += '</ol>'
    self.params['result'] = result
    self.params['form'] = HelloForm(request.POST)
    return render(request, 'hello/index.html', self.params)

#def index(request):
#  params = {
#    'title':'Hello',
#    'message':'your data:',
#    'form':HelloForm()
#  }
#  if(request.method == 'POST'):
#    params['message'] = '名前:' + request.POST['name'] + \
#      '<br>メール:' + request.POST['mail'] + \
#      '<br>年齢:' + request.POST['age']
#    params['form'] = HelloForm(request.POST)
#  return render(request, 'hello/index.html', params)

#def form(request):
#  msg = request.POST['msg']
#  params = {
#    'title':'Hello/Form',
#    'msg':'こんにちは、' + msg + 'さん。',
#  }
#  return render(request, 'hello/index.html', params)