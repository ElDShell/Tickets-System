from django.urls import path
from  . import views

urlpatterns = [
    path("create/ticket/", views.CreateTicket.as_view(), name="create_ticket"),
    path("update/ticket/<int:pk>/", views.UpdateTicket.as_view(), name="update_ticket"),
    path("detail/ticket/<int:pk>/", views.TicketDetails.as_view(), name="detail_ticket"),
    
    path("list", views.TicketList.as_view(), name="tickets_list"),
    path("queue", views.TicketQueue.as_view(), name="tickets_queue"),
    path("workspace", views.WorkSpace.as_view(), name="workspace"),
    path("all-closed-ticket", views.AllClosedTiceket.as_view(), name="all_closed_ticket"),
    
    path("accept/ticket/<int:pk>/", views.AcceptTicketView.as_view(), name="accept_ticket"),
    path("close/ticket/<int:pk>/", views.CloseTicketView.as_view(), name="close_ticket"),
    path("delete/ticket/<int:pk>/", views.DeleteTicket.as_view(), name="delete_ticket"),
    
]
