from django.shortcuts import redirect, render
from .models import Feed

# Create your views here.
def index(request):
    if request.method == 'GET':
        feeds = Feed.objects.order_by('-id')
        return render(request, 'feeds/index.html', {'feeds':feeds})
    elif request.method == 'POST':
        Feed.objects.create(content=request.POST['content'])
        return redirect('feeds:index')

def new(request):
    return render(request, 'feeds/new.html')

def show(request, id):
    feed = Feed.objects.get(id=id)
    return render(request, 'feeds/show.html', {'feed': feed})

def delete(request, id):
    feed = Feed.objects.get(id=id)
    feed.delete()
    return redirect('/')

def update(request, id):
    feed = Feed.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'feeds/update.html', {'feed': feed})
    elif request.method == 'POST':
        feed.content = request.POST['content']
        feed.save()
        return redirect('feeds:index')