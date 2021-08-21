from django.urls import path, include
from .views import SquadAPIview, MembersAPIview, SquadListView

urlpatterns = [
    path('members/', MembersAPIview.as_view(), name='members'),
    path('squad/', SquadAPIview.as_view(), name='squad'),
    path('search/', SquadListView.as_view(), name='search'),
]
