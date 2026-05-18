from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import BookingForm


def home(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Ваша заявка принята. Мы свяжемся с вами в WhatsApp для подтверждения записи.',
            )
            return HttpResponseRedirect(f"{reverse('salon:home')}#booking")
    else:
        form = BookingForm()

    return render(request, 'salon/home.html', {'form': form})
