from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.db import models
from metatron import Metatron
from maprule import fields
from authr.models import User
from core.lib.models import getorcreate

from .models import Link
from .models import Tag
from .sr import LinkSr


class ListCreateLinkApiView(APIView):
    permissions_classes = [IsAuthenticatedOrReadOnly]
    def get(self, _: Request) -> Response:
        """returns a list of links"""
        return Response(LinkSr(Link.objects.all(), many=True).data)

    def create(self, request: Request) -> Response:
        # ...
        user: User = request.user
        rule = fields.Dictionary(dict(
            title=fields.String(max_length=200, min_length=2),
            link=fields.String(max_length=2000),
            public=fields.Boolean(),
            tags=fields.String(nullable=True)
        ))

        data: dict[str, str|bool] = request.data

        if not rule.compare(data):
            return Response({'error': rule.error}, status=400)

        tags: list[Link] = [
            getorcreate(Tag, models.Q(name=word.strip()), name=word.strip()) \
            for word in data.get('tags', '').split(',')\
            if word.strip()]
        link = data['link'].strip()
        
        mt = Metatron(link, schemas=['og'])
        mt.traverse()
        
        og = mt.get('og') or {}
        image = None if type(i:=og.get('image') or None) != str else i

        instance = Link.create(
            author=user,
            title=data['title'],
            link=link,
            public=data['public'],
            tags=tags,
            image=image)

        return Response(LinkSr(instance).data)
