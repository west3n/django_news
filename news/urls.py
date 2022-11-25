from django.urls import path
from .views import (
   NewsList, NewsDetails, NewsSearch, NewsCreate, NewsUpdate, NewsDelete, NewsSubscribe, upgrade_me)

urlpatterns = [
   path('', NewsList.as_view(), name='news_list'),
   path('<int:pk>', NewsDetails.as_view(), name='news_detail'),
   path('search/', NewsSearch.as_view(), name='news_search'),
   path('create/', NewsCreate.as_view(), name='news_create'),
   path('<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
   path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
   path('upgrade/', upgrade_me, name='upgrade'),
   path('subscribe/', NewsSubscribe.as_view(), name='news_subscribe')
]
