from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView,UpdateView,ListView,DetailView,RedirectView,DeleteView
from .models import *

# Create your views here.
class CreateTicket(LoginRequiredMixin,CreateView):
    model = Ticket
    fields = ('title','content')
    template_name = 'create_ticket.html'

    def form_valid(self, form):
        ticket =  form.save(commit=False)

        ticket.created_by = self.request.user
        ticket.status = 'Pending'
        
        ticket.save()
        messages.success(self.request,'Ticket Created succesfully...')
        return redirect('dashboard')
    
    def form_invalid(self, form):
        messages.warning(self.request,'Something gone wrong please try again later!!!')
        return self.render_to_response(self.get_context_data(form=form))     

class UpdateTicket(UpdateView):
    model = Ticket
    fields = ('title', 'content')
    template_name = 'update_ticket.html'
    success_url=  reverse_lazy('dashboard')
    context_object_name = 'ticket'
    
    def dispatch(self, request: HttpRequest, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_resolved:
            messages.warning(request, 'This ticket has already been resolved and cannot be updated.')
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request,'Ticket Updated succesfully...')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request,'Something gone wrong please try again later!!!')
        return super().form_invalid(form)

class  TicketList(ListView):
    model = Ticket
    template_name = 'all_tickets.html'
    context_object_name = 'tickets'
    def get_queryset(self) :
        return Ticket.objects.filter(created_by =self.request.user)

class TicketQueue(ListView):
    model = Ticket
    template_name = 'tickets_queue.html'
    context_object_name = 'tickets'
    
    def get_queryset(self) :
        return Ticket.objects.filter(status='Pending')
    
class WorkSpace(ListView):
    model = Ticket
    template_name = 'workspace.html'
    context_object_name = 'tickets'
    def get_queryset(self) :
        return Ticket.objects.filter(assigned_to=self.request.user,is_resolved=False)

class AllClosedTiceket(ListView):
    model = Ticket
    template_name = 'all_closed_ticket.html'
    context_object_name= 'tickets'
    def get_queryset(self) :
        return Ticket.objects.filter(assigned_to=self.request.user,is_resolved=True)


class AcceptTicketView(RedirectView):
    pattern_name = 'tickets_queue'
    
    def get_redirect_url(self, *args, **kwargs):
        ticket = get_object_or_404(Ticket, pk=kwargs['pk'])
        ticket.status = 'Active'
        ticket.accepted_date = timezone.now()
        ticket.assigned_to = self.request.user
        ticket.save()
        messages.success(self.request,'Ticket Accepted Successfully...')
        return reverse(self.pattern_name)
    
class CloseTicketView(RedirectView):
    pattern_name = 'all_closed_ticket'
    
    def get_redirect_url(self, *args, **kwargs):
        ticket = get_object_or_404(Ticket,pk=kwargs['pk'])
        ticket.status = 'Complated'
        ticket.closed_date = timezone.now()
        ticket.is_resolved = True
        ticket.save()
        messages.warning(self.request,'Ticket Closed Successfully...',extra_tags='danger')
        return reverse(self.pattern_name)

class TicketDetails(DetailView):
    model = Ticket
    template_name = 'ticket_detail.html'
    context_object_name = 'ticket'
    
class DeleteTicket(DeleteView):
    model = Ticket 
    template_name = None
    context_object_name = 'ticket'
    
    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER',reverse_lazy('dashboard'))
    
    def delete(self, request, *args, **kwargs):
        ticket = self.get_object()
        messages.warning(request,'Ticket has been Deleted!!!!..')
        return super().delete(request, *args, **kwargs)
    
