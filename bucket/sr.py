from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import StringRelatedField
from rest_framework.serializers import SerializerMethodField

from .models import Link
from .models import Vote

from os import environ

class LinkSr(ModelSerializer):
    tags = StringRelatedField(many=True)
    baseUrl = SerializerMethodField()
    trackingUrl = SerializerMethodField()
    voteCount = SerializerMethodField()

    class Meta:
        fields = [
            'title',
            'tags',
            'public',
            'date_posted',
            'image',
            'baseUrl',
            'trackingUrl',
            'voteCount',
        ]
        model = Link

    def get_baseUrl(self, obj:Link) -> str:
        url = obj.link.split("://")
        if len(url) > 1:
            url = url[1]
        return url.split('/')[0]
    
    def get_trackingUrl(self, obj:Link) -> str:
        host = environ.get('API_DOMAIN_NAME', '')
        return f'{host}/bucket/i/{obj.trackingID}/'

    def get_voteCount(self, obj:Link) -> dict[str, int]:
        return dict(
            upvote=Vote.objects.filter(link=obj, type=Vote.Type.UPVOTE).count(),
            downvote=Vote.objects.filter(link=obj, type=Vote.Type.DOWNVOTE).count(),)
