from datetime import date

from django import forms

from .models import Booking


SERVICE_CHOICES = [
    ('', 'Выберите услугу'),
    ('Маникюр & Педикюр', (
        ('Маникюр без покрытия — 400 с', 'Маникюр без покрытия — 400 с'),
        ('Маникюр с покрытием — 800 с', 'Маникюр с покрытием — 800 с'),
        ('Наращивание ногтей — 1 500 с', 'Наращивание ногтей — 1 500 с'),
        ('Педикюр с покрытием — 1 500 с', 'Педикюр с покрытием — 1 500 с'),
        ('Гигиенический педикюр — 800 с', 'Гигиенический педикюр — 800 с'),
    )),
    ('Макияж', (
        ('Дневной макияж — 1 000 с', 'Дневной макияж — 1 000 с'),
        ('Вечерний макияж — 1 200 с', 'Вечерний макияж — 1 200 с'),
        ('Свадебный макияж — 3 000 с', 'Свадебный макияж — 3 000 с'),
    )),
    ('Ресницы', (
        ('Классический объём — 1 000 с', 'Классический объём — 1 000 с'),
        ('Двойной объём 2D — 1 300 с', 'Двойной объём 2D — 1 300 с'),
        ('Мега объём — 1 700 с', 'Мега объём — 1 700 с'),
        ('Ламинирование ресниц — 1 000 с', 'Ламинирование ресниц — 1 000 с'),
    )),
    ('Волосы', (
        ('Стрижка — от 800 с', 'Стрижка — от 800 с'),
        ('Кератин — от 3 000 с', 'Кератин — от 3 000 с'),
        ('Окрашивание — уточнить цену', 'Окрашивание — уточнить цену'),
    )),
]

TIME_CHOICES = [('', 'Выберите время')] + [(f'{hour:02d}:00', f'{hour:02d}:00') for hour in range(9, 20)]


class BookingForm(forms.ModelForm):
    service = forms.ChoiceField(choices=SERVICE_CHOICES)
    appointment_time = forms.TimeField(
        input_formats=['%H:%M'],
        widget=forms.Select(choices=TIME_CHOICES),
    )

    class Meta:
        model = Booking
        fields = ['name', 'whatsapp', 'service', 'appointment_date', 'appointment_time', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Айгуль'}),
            'whatsapp': forms.TextInput(attrs={'placeholder': '+996 XXX XXX XXX', 'inputmode': 'tel'}),
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
            'comment': forms.Textarea(attrs={'placeholder': 'Пожелания или вопросы...', 'rows': 3, 'style': 'resize:vertical'}),
        }

    def clean_appointment_date(self):
        selected_date = self.cleaned_data['appointment_date']
        if selected_date < date.today():
            raise forms.ValidationError('Нельзя выбрать прошедшую дату.')
        return selected_date

    def clean_whatsapp(self):
        phone = self.cleaned_data['whatsapp'].strip()
        if len(phone) < 8:
            raise forms.ValidationError('Укажите корректный номер WhatsApp.')
        return phone

