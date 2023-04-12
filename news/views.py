from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import News
from .forms import NewsForm

def news_list(request):
    news_list = News.objects.filter(is_visible=True).order_by('-pub_date')
    paginator = Paginator(news_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news/news_list.html', {'page_obj': page_obj})

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})
