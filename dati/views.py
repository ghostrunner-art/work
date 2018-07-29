from django.shortcuts import render


def dati(request):
    context = {}
    context['nihao'] = ''
    return render(request,'dati/dati.html',context)


