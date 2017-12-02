from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^$', views.home,name='home'),
    url(r'^autocomplete/get_book', views.AutoCompleteView.as_view(), name='autocomplete')
]