from django.shortcuts import render, redirect
from .forms import WipForm
from .models import WipReq
from .tables import WiplogTable
from django_tables2 import RequestConfig
from django.utils import timezone

def cs_home(request):
    return render(request, 'CServices/cs_home.html', {})

def cs_wipreq(request):
    if request.method == 'POST':
        form = WipForm(request.POST)
        if form.is_valid():
            post        = form.save(commit=False)
            post.author = request.user
            post.date   = timezone.now()
            post.save()
            return redirect('cs_wiplog')
    else:
        form = WipForm()
    return render(request, 'CServices/cs_wipreq.html', {'form': form})

def cs_wiplog(request):
    table = WiplogTable(WipReq.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'CServices/cs_wiplog.html', {'table': table})
