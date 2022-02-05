from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PollForm, PollDeleteForm
from webapp.models import Poll, Answer, Choice
from webapp.views.base import SearchView


class PollView(SearchView):
    model = Poll
    context_object_name = "polls"
    template_name = "polls/index.html"
    paginate_by = 5
    paginate_orphans = 0
    search_fields = ["question__icontains"]
    ordering = '-created_at'

#
class PollCreate(CreateView):
    model = Poll
    form_class = PollForm
    template_name = "polls/create.html"

#
#
class PollDetailView(DetailView):
    template_name = 'polls/view.html'
    model = Poll

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        choice = self.object.choices.order_by("option")
        context['choices'] = choice
        return context
#
#
class PollUpdateView(UpdateView):
    form_class = PollForm
    template_name = "polls/update.html"
    model = Poll
#
#
class PollDeleteView(DeleteView):
    model = Poll
    template_name = "polls/delete.html"
    success_url = reverse_lazy('poll_index')
    form_class = PollDeleteForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method == "POST":
            kwargs['instance'] = self.object
        return kwargs

class PollAnswer(View):
    def get(self, request, *args, **kwargs):
        answer = Answer
        poll = get_object_or_404(Poll, pk=kwargs.get('pk'))
        return render(request, 'polls/answer.html', {'poll' : poll})

    def post(self, request, *args, **kwargs):
        choice_id = request.POST.get('choice')
        choice_id = Choice.objects.get(pk=choice_id)
        poll_id = kwargs['pk']
        poll_id = Poll.objects.get(pk=poll_id)
        Answer.objects.create(choice=choice_id,
                              poll=poll_id)

        return render(request, 'polls/done.html')







# class PollAnswer(View):
#     def get(self, request, *args, **kwargs):
#         form = ChoiceAnswerForm
#         context = self.get_context_data(form=form)
#         return render(request, self.template_name, context)

