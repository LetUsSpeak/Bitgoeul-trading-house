from django.urls import path
from eventapp.views import EventList, EventDetail, EventCreateView

app_name = 'eventapp'

urlpatterns = [
    path('', EventList.as_view(), name="event-list"),
    path('<int:pk>/', EventDetail.as_view(), name="event-detail"),
    path('create/', EventCreateView.as_view(), name='create')
]