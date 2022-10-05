from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Todo
from .serializers import TodoSerializer


@api_view(['GET'])
def getAllTodos(request):

    todos = Todo.objects.all()

    serializer = TodoSerializer(todos, many=True)

    return Response(serializer.data)
