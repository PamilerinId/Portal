from django.conf.urls import url
from lateReg import views

urlpatterns = [
    url(r'^reg-status/(?P<pk>[0-9]+)/$', views.RegStatusAPIView.as_view()),

    url(r'^late-reg/$', views.LateRegAPIView.as_view(), name='late_reg'),
    url(r'^late-reg/(?P<pk>[0-9]+)/$', views.LateRegDetailAPIView.as_view(), name='late_reg_detail'),

    url(r'^late-reg-log/$', views.LogAPIView.as_view()),
    url(r'^late-reg-log/(?P<pk>[0-9]+)/$', views.LogDetailAPIView.as_view()),
]