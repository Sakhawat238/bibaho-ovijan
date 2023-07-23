from django.db import models

class OTP(models.Model):
    contact = models.CharField(max_length=250, null=False)
    code = models.IntegerField(null=False)
    timestamp = models.DateTimeField(auto_now=True)
    resend_count = models.IntegerField(default=0)
    is_mobile = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=True)
    is_archived = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contact + ' OTP: ' + str(self.code) + ' || ' + str(self.timestamp)

    class Meta:
        ordering = ['-timestamp']


