from django.db import models


class Booking(models.Model):
    name = models.CharField('Имя клиента', max_length=120)
    whatsapp = models.CharField('WhatsApp', max_length=30)
    service = models.CharField('Услуга', max_length=200)
    appointment_date = models.DateField('Дата записи')
    appointment_time = models.TimeField('Время записи')
    comment = models.TextField('Комментарий', blank=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['-appointment_date', '-appointment_time', '-created_at']

    def __str__(self):
        return f'{self.name} — {self.service} ({self.appointment_date} {self.appointment_time})'
