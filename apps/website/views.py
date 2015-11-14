# coding:utf-8
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView
from services.models import Service, ServiceStatus
from suscription.forms import SuscriptionForm


class Home(FormView):
    template_name = 'index.html'
    form_class = SuscriptionForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        context['statuses'] = ServiceStatus.objects.all()[:10]
        return context

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Successfully suscribed!')
        return super(Home, self).form_valid(form)
