from django.urls import path

from . import views

app_name = 'thuvienbk'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
# trang login cho sv
# trang list nhung cuon sach da muon 
# trang list nhung cuon sach da mua
# trang list tat ca nhung cuon sach trong thu vien, moi cuon co' the rating va comment