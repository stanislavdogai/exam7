from django.urls import path

from webapp.views.choices import ChoiceCreate, ChoiceUpdateView, ChoiceDeleteView
from webapp.views.polls import PollView, PollCreate, PollDetailView, PollUpdateView, PollDeleteView, PollAnswer

urlpatterns = [
    path('', PollView.as_view(), name='poll_index'),
    path('poll/create', PollCreate.as_view(), name='poll_create'),
    path('poll<int:pk>/detail', PollDetailView.as_view(), name='poll_detail'),
    path('poll<int:pk>/update', PollUpdateView.as_view(), name='poll_update'),
    path('poll<int:pk>/delete', PollDeleteView.as_view(), name='poll_delete'),
    path('poll<int:pk>/choice_add', ChoiceCreate.as_view(), name='poll_add_choice'),
    path('poll/<int:pk>choice_update', ChoiceUpdateView.as_view(), name='poll_update_choice'),
    path('poll/<int:pk>choice_delete', ChoiceDeleteView.as_view(), name='poll_delete_choice'),
    path('poll/<int:pk>/answer', PollAnswer.as_view(), name='poll_answer')
]