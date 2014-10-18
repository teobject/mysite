from django.db import models
# Create your models here.
class IpAddressTable(models.Model):
    ip_id = models.BigIntegerField(unique=True)
    ip_address = models.TextField()
    ip_type = models.TextField()
    subnet_id = models.BigIntegerField()
    project_id = models.IntegerField()
    use_status_id = models.IntegerField()
    owner_name = models.TextField()
    insert_time = models.DateTimeField()
    update_time = models.DateTimeField()
    remarks = models.TextField(blank=True)
    class Meta:
        db_table = u'ip_address_table'
