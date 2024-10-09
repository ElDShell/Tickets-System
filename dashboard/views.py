from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from tickets.models import Ticket
# Create your views here.
#LoginRequiredMixin,
class Dashboard(TemplateView):
    template_name = 'dashboard.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #ADMIN
        if self.request.user.is_admin:
            context["all_tickets"] = Ticket.objects.all().count()
            context["table_tickets"] = Ticket.objects.all().order_by('-id')[:3]
            context["all_active_tickets"] = Ticket.objects.filter(status='Active').count()
            context["all_closed_tickets"] = Ticket.objects.filter(is_resolved=True).count()
            context["all_pending_tickets"] = Ticket.objects.filter(status='Pending').count()
        
        elif self.request.user.is_customer:
            context["all_tickets"] = Ticket.objects.filter(created_by=self.request.user).count()
            context["table_tickets"] = Ticket.objects.filter(created_by=self.request.user).order_by('-id')[:3]
            context["all_active_tickets"] = Ticket.objects.filter(created_by=self.request.user,status='Active').count()
            context["all_closed_tickets"] = Ticket.objects.filter(created_by=self.request.user,is_resolved=True).count()
            context["all_pending_tickets"] = Ticket.objects.filter(created_by=self.request.user,status='Pending').count()

        #Customer

        return context
class test(TemplateView):
    template_name = 'component.html'
        
    