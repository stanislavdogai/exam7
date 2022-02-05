from django.db import models

# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=300, null=False, blank=False, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True)

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