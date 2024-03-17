from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import Task


def get_context() -> dict[str]:
    return {
        "todo_list": Task.objects.all()
    }

@csrf_exempt
@require_POST
def create_todo(request: HttpRequest) -> HttpResponse:
    title = request.POST.get('title')
    if title.strip() != '':
        Task.objects.create(text = title)
    return redirect('index')

def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'app/index.html', get_context())

def delete_todo(request: HttpRequest, pk: int) -> HttpResponse:
    task = Task.objects.get(pk = pk)
    task.delete()
    return redirect('index')