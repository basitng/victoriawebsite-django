from django.urls import path
from dashboard.views import about, blog, blogDetail, contact, eventDetail, events, gallery, home, ministry, sermonDetail, sermons

urlpatterns = [
    path('', home, name="index"),
    path('about/', about, name="about"),
    path('blog', blog, name="blog"),
    path('blog-details/', blogDetail, name="blog-details"),
    path('event-details/', eventDetail, name="event-details"),
    path('sermon-details/', sermonDetail, name="sermon-details"),
    path('sermons/', sermons, name="sermons"),
    path('ministry/', ministry, name="ministry"),
    path('events/', events, name="events"),
    path('gallery/', gallery, name="gallery"),
    path('contact/', contact, name="contact"),

]
