from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.db import models
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseRedirect

from metatron import Metatron
from maprule import fields
from authr.models import User
import requests

from core.lib import paginatedResponse
from core.lib.models import getorcreate

from .models import Link
from .models import Tag
from .models import Vote
from .sr import LinkSr


@api_view()
def get_links(request: Request) -> Response:
	"""returns a list of links"""
	return paginatedResponse(request, Link.objects.all(), LinkSr)

@api_view(["post"])
@permission_classes([IsAuthenticated])
def create_link(request: Request) -> Response:
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

	reform = lambda x: x.strip().lower()
	tags: list[Link] = [
		getorcreate(Tag, models.Q(name=reform(word)), name=reform(word)) \
		for word in data.get('tags', '').split(',')\
		if reform(word)]
	link = data['link'].strip()
	
	try:
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
	except requests.exceptions.ConnectionError:
		return Response({'error': f"Couldn't access the provided link: \"{link}\""}, status=400)


def open_link(request: WSGIRequest, tid: str):
	user: User = request.user
	link: Link = Link.objects.filter(trackingID=tid).first()

	if link == None:
		return render(request, '404.html', status=404)

	if user:
		getorcreate(
			Vote,
			models.Q(link=link, user=user),
			user=user, link=link, type=Vote.Type.UPVOTE)
	return HttpResponseRedirect(link.link)

@api_view(['post'])
@permission_classes([IsAuthenticated])
def down_vote(request: Request, tid:str) -> Response:
	user: User = request.user
	link: Link = Link.objects.filter(trackingID=tid).first()

	if link == None:
		return Response({'error': 'cant find link'}, status=404)

	vote: Vote = getorcreate(
		Vote,
		models.Q(link=link, user=user),
		user=user, link=link, type=Vote.Type.DOWNVOTE)
	vote.type = Vote.Type.DOWNVOTE
	vote.save()
	return Response(status=204)

@api_view(['post'])
@permission_classes([IsAuthenticated])
def up_vote(request: Request, tid:str) -> Response:
	user: User = request.user
	link: Link = Link.objects.filter(trackingID=tid).first()

	if link == None:
		return Response({'error': 'cant find link'}, status=404)

	vote: Vote = getorcreate(
		Vote,
		models.Q(link=link, user=user),
		user=user, link=link, type=Vote.Type.UPVOTE)
	vote.type = Vote.Type.UPVOTE
	vote.save()
	return Response(status=204)
