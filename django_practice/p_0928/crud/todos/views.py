from django.shortcuts import render, redirect


from .models import Todo

# Create your views here.
def index(request):
    _todos = Todo.objects.all()
    context = {
        "todos": _todos,
    }

    return render(request, 'todos/index.html', context)

def create(request):
    content = request.GET.get("content___")
    Todo.objects.create(content=content)
 
    return redirect('todos:index')

def delete(request, todo_pk):
    todo = Todo.objects.get(pk = todo_pk)
    todo.delete()

    return redirect('todos:index')


"""
redirect
1. 사용자가 create 요청
2. 서버에서 index 요청
3. 사용자에게는 index 응답

"""