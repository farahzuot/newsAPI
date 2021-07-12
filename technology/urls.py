from django.urls import path,include

from .views import newsListCreateView , newsDetailsView
urlpatterns = [
    path('', newsListCreateView.as_view(), name='listView'),
    path('<int:pk>', newsDetailsView.as_view(), name='detailsView'),
]
