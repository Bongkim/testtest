from django.shortcuts import redirect, render
from .models import Feed, Comment
from django.http import JsonResponse

# Create your views here.
def index(request):
    if request.method == 'GET':
        feeds = Feed.objects.order_by('-id')
        return render(request, 'feeds/index.html', {'feeds':feeds})
    elif request.method == 'POST':
        Feed.objects.create(content=request.POST['content'], author=request.user)
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

def create_comment(request, id):
    content = request.POST['content']
    Comment.objects.create(feed_id=id, content=content, author=request.user)
    return JsonResponse({
        "id": comment.id,
        "content": content,
    })

def delete_comment(reqeust, id, cid):
    comment = Comment.objects.get(id=cid)
    comment.delete()
    return redirect(f'/feeds/{id}/')

def like(request, id):
    feed = Feed.objects.get(id=id)
    is_liked_by_me = feed.like_users.filter(id=request.user.id).exists()
    if is_liked_by_me:
        feed.like_users.remove(request.user)
    else:
        feed.like_users.add(request.user)
    # return redirect (request.GET.get('next','/'))
    return JsonResponse({
        'feedLikeCount': feed.like_set.count(), 
    })

def comment_like(request, id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    is_liked_by_me = comment.like_users.filter(id=request.user.id).exists()
    if is_liked_by_me:
        comment.like_users.remove(request.user)
    else:
        comment.like_users.add(request.user)
    return redirect(request.GET.get('next', '/'))

def create_nested_comment(request, feed_id, comment_id):
    feed = Feed.objects.get(id=feed_id)
    comment = Comment.objects.get(id=comment_id)
    if request.method == "POST":
        Comment.objects.create(
            author=request.user, feed_id=feed_id, parent_comment_id=comment_id, content=request.POST['content']
        )
        return redirect(f"/feeds/{feed_id}/")
    return render(request, 'feeds/new_nested_comment.html', {'feed': feed, 'comment': comment})

