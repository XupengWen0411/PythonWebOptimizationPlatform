from django.urls import path,re_path
from One_APP import views
urlpatterns = [
    path('bar',views.Chart_View.as_view(),name = 'ChartView'),
    path('index',views.Index_View,name = 'IndexView')
]