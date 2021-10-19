from django.db import models
from django.db.models.base import Model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class TaggedItemManager(models.Manager):
    def get_tags_for(self, obj_type, obj_id):
        # Get Tagged Products
        content_type = ContentType.objects.get_for_model(obj_type)
        return TaggedItem.objects \
            .select_related('tag') \
            .filter(
                content_type=content_type,
                object_id=obj_id  # this should be got dynamically
            )


class Tag(models.Model):
    label = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.label


class TaggedItem(models.Model):
    objects = TaggedItemManager()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
