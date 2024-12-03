from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import NoteSerializer
from .models import Note


@csrf_exempt
def notes(request):
    if(request.method == 'GET'):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif(request.method == 'POST'):
        data = JSONParser().parse(request)
        serializer = NoteSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def note_detail(request, pk):
    try:
        note = Note.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)  
    if(request.method == 'PUT'):
        data = JSONParser().parse(request) 
        serializer = NoteSerializer(note, data=data)
        if(serializer.is_valid()):  
            serializer.save() 
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif(request.method == 'DELETE'):
        note.delete() 
        return HttpResponse(status=204) 



