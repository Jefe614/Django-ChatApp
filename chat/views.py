from django.shortcuts import render, redirect 
from django.shortcuts import render, get_object_or_404
from .models import Friend
from .models import  Message
from django.contrib.auth.decorators import login_required
from .forms import MessageForm
from django.http import JsonResponse



# Create your views here.
def homepage(request):
    friends = Friend.objects.all()
    return render(request, 'home.html',{'friends':friends})

def splash_view(request):
    return render(request, 'splash.html')

def details(request, pk):
    friend = get_object_or_404(Friend, id=pk)
    messages = Message.objects.filter(friend=friend)

    for message in messages:
        # Set is_sent based on whether the message is sent by the current user
        message.is_sent = message.sender == request.user  # Adjust this based on your Message model structure
        message.save()
    return render(request, 'detail.html',{'friend':friend, 'messages':messages})    


def friends_list(request):
    friends = Friend.objects.all()
    
    return render(request, 'friend_list.html', {'friends': friends})

@login_required
def profile(request):
    return render(request, 'profile.html')


def send_message(request, pk):
    friend = get_object_or_404(Friend, id=pk)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            Message.objects.create(friend=friend, content=content)

    return redirect('detail', pk=pk)

# views.py
from django.http import JsonResponse

@login_required
def send_message(request, pk):
    if request.method == 'POST':
       
        content = request.POST.get('content', None)
        is_sent = True
        
        

    return JsonResponse({'is_sent': is_sent, 'content': content}, status=400)
