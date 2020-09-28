
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'test.html')

def analyze(request):
    data = request.POST.get('text')
    punc = request.POST.get('removepunc')
    caps = request.POST.get('fullcaps')
    line = request.POST.get('newlineremove')
    space = request.POST.get('spaceremover')
    count = request.POST.get('charcount')
    new_data = 'NONE(default output)'
    data_type = 'empty'
    data_out = {'purpose':data_type,'analyzed_text':new_data}
    if punc:
        punc_data = '''.,:;'"}{[]\|<>?/+-*&^%$#@!'''
        new_data = ''
        data_type = 'Remove Punctuations'
        for i in data:
            if i not in punc_data:
                new_data += i
    elif caps:
        new_data = data.upper()
        data_type = 'Full caps'
    elif line:
        new_data = data
        data_type = 'New Line Remover'
        '''
        for i in data:
            if i != '\n' and i != '\r':
                new_data += i '''
        new_data = new_data.replace('\n','')
        new_data = new_data.replace('\r', '')

    elif space:
        new_data = data.replace(' ','')
        data_type = 'Space Remover'
    elif count:
        new_data = len(data)
        data_type = 'Character Count'
    elif data:
        new_data = data

    data_out = {'purpose':data_type,'analyzed_text':new_data}
    return render(request,'output.html',data_out)



    #Jinja templating