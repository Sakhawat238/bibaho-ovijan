from django.db import models
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver


class AuditLog(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    user = models.CharField(max_length=250, null=False, blank=False)
    user_ip = models.CharField(max_length=100, null=False, blank=False)
    device_info = models.CharField(max_length=500, null=True, blank=True)
    action_name = models.CharField(max_length=50, null=False, blank=False)
    table_name = models.CharField(max_length=250, null=True, blank=True)
    task_name = models.CharField(max_length=50, null=True, blank=True)
    action_details = models.CharField(max_length=200, null=True, blank=True)
    data = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.timestamp)+'_'+self.user

    class Meta:
        db_table = 'AUTH_LogWithAudit_AuditLog'



@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):  
    us = user.username
    x_f = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_f:
        uip = x_f.split(',')[0]
    else:
        uip = request.META.get('REMOTE_ADDR')
    try:
        deviceinfo = request.META['HTTP_USER_AGENT']
    except:
        deviceinfo = ''
    AuditLog.objects.create(user=us, user_ip=uip, action_name="login", device_info=deviceinfo, action_details=us+" logged into the system", table_name="user")



@receiver(user_logged_out)
def user_logged_out_callback(sender, request, user, **kwargs):  
    us = user.username
    x_f = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_f:
        uip = x_f.split(',')[0]
    else:
        uip = request.META.get('REMOTE_ADDR')
    try:
        deviceinfo = request.META['HTTP_USER_AGENT']
    except:
        deviceinfo = ''
    AuditLog.objects.create(user=us, user_ip=uip, device_info=deviceinfo, action_name="logout", action_details=us+" logged out from the system", table_name="user")