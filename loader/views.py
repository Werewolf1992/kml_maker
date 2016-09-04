# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from .engine import engine
from .models import Store


def upload_file(request):
    e = engine()
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            up = e.handle_uploaded_file(request.FILES['file'])
            for i in up:
                s = Store(**i)
                s.save()

            return HttpResponseRedirect('display')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def file_display(request):
    e = engine()
    store_objects = Store.objects.all()
    kml = e.kml_maker(store_objects)
    return render(request, 'display.html', {'kml': kml})