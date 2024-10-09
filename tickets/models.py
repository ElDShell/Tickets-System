from django.db import models

# Create your models here.
from users.models import User
import uuid
# Create your models here.
class Ticket(models.Model):
    STATUS = (
        ('Pending','PENDING'),
        ('Active','ACTIVE'),
        ('Complated','COMPLATED'),
    )
    number = models.UUIDField(max_length=100,default=uuid.uuid4,)
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    created_by = models.ForeignKey(User,related_name='tickets_created',on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User,related_name='tickets_assigned',on_delete=models.DO_NOTHING,null=True,blank=True) 
    
    created_at = models.DateField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)
    accepted_date = models.DateField(blank=True,null=True)
    closed_date = models.DateField(blank=True,null=True)
    status = models.CharField(choices=STATUS,max_length=9)
    def __str__(self) -> str:
        return self.title