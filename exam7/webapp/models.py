from django.db import models

from django.urls import reverse


class Poll(models.Model):
    question = models.CharField(max_length=300, null=False, blank=False, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('poll_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.pk}. {self.question}'

    class Meta:
        db_table = 'Poll'
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

class Choice(models.Model):
    option = models.TextField(max_length=500, null=False, blank=False, verbose_name='Вариант')
    poll = models.ForeignKey('webapp.Poll', on_delete=models.CASCADE, related_name='choices', verbose_name='Опрос')

    def __str__(self):
        return f'{self.pk}. {self.option}'

    class Meta:
        db_table = 'Choice'
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'

class Answer(models.Model):
    poll = models.ForeignKey('webapp.Poll', on_delete=models.PROTECT, related_name='answer_poll', verbose_name='Опрос')
    choice = models.ForeignKey('webapp.Choice', on_delete=models.PROTECT, related_name='answer_choice', verbose_name='Вариант')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Вопрос: {self.poll.question}\r\nОтвет:{self.choice.option}'

    class Meta:
        db_table = 'answer'
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

