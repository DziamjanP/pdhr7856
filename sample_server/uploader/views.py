from django.shortcuts import render
from django import forms
from django.views import View
from django.http import JsonResponse
from django.shortcuts import render

from .models import DataPiece

import json

class UploadJSONForm(forms.Form):
    file = forms.FileField()

class UploadJSONView(View):
    def get(self, request):
        form = UploadJSONForm()
        return render(request, 'upload.html', {'form': form})

    def post(self, request):
        form = UploadJSONForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            try:
                data = json.load(uploaded_file)
            except json.JSONDecodeError:
                return JsonResponse({'status': 400, 'message': 'Invalid JSON file.'}, status=400)
            
            if not 'name' in data:
                return JsonResponse({'status': 400, 'message': 'Field "name" not found.'}, status=400)
            if not 'date' in data:
                return JsonResponse({'status': 400, 'message': 'Field "date" not found.'}, status=400)

            dp = DataPiece(name=data['name'], date=data['date'])
            dp.save()
            
            return JsonResponse({'status':0, 'message': 'ok'}, status=200)
        
        return JsonResponse({'status': 400, 'message': 'Form is not valid.'}, status=400)
