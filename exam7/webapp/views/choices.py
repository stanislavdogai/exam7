from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import ChoiceForm, ChoiceDeleteForm
from webapp.models import Choice, Poll


class ChoiceCreate(CreateView):
    model = Choice
    form_class = ChoiceForm
    template_name = "choices/create.html"


    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        choice = form.save(commit=False)
        choice.poll = poll
        choice.save()
        return redirect('poll_detail', pk=poll.pk)

class ChoiceUpdateView(UpdateView):
    form_class = ChoiceForm
    template_name = "choices/update.html"
    model = Choice

    def get_success_url(self):
        return reverse('poll_detail', kwargs={'pk': self.object.poll.pk}) #Нужно подправить


class ChoiceDeleteView(DeleteView):
    model = Choice
    template_name = "choices/delete.html"
    success_url = reverse_lazy('poll_detail')
    form_class = ChoiceDeleteForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method == "POST":
            kwargs['instance'] = self.object
        return kwargs