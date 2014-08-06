from django.db import models
from datetime import datetime

# Create your models here.

ASSET_INVENTORY = (
    ('MEDICAL', 'MEDICAL'),
    ('ELECTRO', 'ELECTRO-MECHANICAL'),
    ('FURNITURE', 'FURNITURE'),
)


class Asset(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    category = models.CharField(max_length=100, choices=ASSET_INVENTORY, verbose_name='category')
    acquired_on = models.DateField(null=False, verbose_name='Equipment Delivery Date')
    service_period = models.PositiveIntegerField(verbose_name='Service Interval')
    last_service_date = models.DateField(verbose_name='Last Service Date', blank=True)
    service_due = models.BooleanField(default=False, verbose_name='Due for Service?')

    def __unicode__(self):

        return u'%s - %s' % (self.name, self.category)

    class Meta:
        verbose_name = 'asset'
        verbose_name_plural = 'Fixed Assets'

    def due_for_service(self):

        """ Calculate when equipment is due for service
        """

        #get today's date

        today = datetime.date.today()

        #Calculate due date for service based on last service date and the service interval

        service_due_date = self.last_service_date + datetime.timedelta(self.service_period)

        # Setting service due boolean field

        if service_due_date > today:
            self.service_due = True





