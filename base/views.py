from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout


def home(request):
    return render(request, "home.html")

@api_view()
@permission_classes([IsAuthenticated])
def hello(requ):
    message = 'hello world'

    return Response(message)

def logout_view(request):
    logout(request)
    return redirect('/')

