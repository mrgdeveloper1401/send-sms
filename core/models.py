from django.db import models
from django_jalali.db import models as jmodels
from django.utils.timezone import now
from core.manager import SoftDeleteQuerySet, SoftDeleteManager


class SoftDeleteModel(models.Model):
    deleted_at = jmodels.jDateTimeField(blank=True, null=True, editable=False)
    is_deleted = models.BooleanField(default=False, editable=False)

    objects = SoftDeleteManager()

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = now()
        self.is_deleted = True
        self.save()

    class Meta:
        abstract = True
