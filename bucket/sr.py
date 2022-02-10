from rest_framework.serializers import ModelSerializer
from .models import Link

class LinkSr(ModelSerializer):
    class Meta:
        fields = [
            'id'
            'title'
            'link'
            'image'
            'date_posted'
            'public'
            'author'
            'tags',
            'trackable_link'
        ]
        model = Link
