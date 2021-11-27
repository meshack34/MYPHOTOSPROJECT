
from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Article

# Create views
def news_today(request):
    date = dt.date.today()
    news = Article.todays_news()
    return render(request, 'my-photos/daily-photos.html',{'date': date,"news":news})

def past_days_news(request,past_date):
    
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_today)
    
    news = Article.days_news(date)
    return render(request, 'my-photos/my-gallery.html', {"date":date,"news":news})
