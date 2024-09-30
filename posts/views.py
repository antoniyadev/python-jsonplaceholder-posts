from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Fetch and display posts


def index(request):
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = response.json()

    # Paginate posts
    paginator = Paginator(posts, 10)  # Show 10 posts per page
    page = request.GET.get('page')

    try:
        paginated_posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page.
        paginated_posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver the last page.
        paginated_posts = paginator.page(paginator.num_pages)

    return render(request, 'posts/index.html', {'posts': paginated_posts})

# Fetch and display comments for a specific post


def show(request, post_id):
    post_response = requests.get(
        f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    comments_response = requests.get(
        f'https://jsonplaceholder.typicode.com/posts/{post_id}/comments')

    post = post_response.json()
    comments = comments_response.json()

    for comment in comments:
        comment['author_name'] = comment['email'].split('@')[0]

    return render(request, 'posts/show.html', {'post': post, 'comments': comments})
