from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.authtoken.models import Token

from .models import User
from maprule import fields

from core.lib.rule import EmailField
from core.lib.rule import PasswordField

def loginRule(force=True) -> fields.Dictionary:
	return fields.Dictionary(dict(
		email=EmailField(),
		password=PasswordField() if force else fields.String()
	))

@api_view(['post'])
def login(request: Request) -> Response:
	rule = loginRule(force=False)
	if not rule.compare(request.data):
		return Response({'error': rule.error})
	data: dict = request.data

	user:User = User.objects.filter(email=data['email']).first()

	if not user:
		return Response({'error': 'user not found'}, status=404)

	if not user.check_password(data['password']):
		return Response({'error': 'incorrect password'}, status=400)

	token:Token = Token.objects.filter(user=user).first()
	if token:
		# delete old token
		token.delete()
	token = Token.objects.create(user=user).key

	return Response(dict(
		email=user.email,
		token=token
	))


@api_view(['post'])
def signup(request: Request) -> Response:
	rule = loginRule()
	if not rule.compare(request.data):
		return Response({'error': rule.error})
	data: dict = request.data
	
	_other_user = User.objects.filter(email=data['email']).first()
	if _other_user:
		return Response({'error': 'user already exists'}, status=status.HTTP_409_CONFLICT)
	
	user = User(email=data['email'])
	user.set_password(data['password'])
	user.save()

	token = Token.objects.create(user=user).key

	return Response(dict(
		email=user.email,
		token=token
	))


@api_view(['get'])
@permission_classes([IsAuthenticated])
def user(request: Request) -> Response:
	user:User = request.user
	return Response(dict(
		email=user.email
	))

@api_view(['post'])
@permission_classes([IsAuthenticated])
def logout(request: Request) -> Response:
	user = request.user
	token:Token = Token.objects.filter(user=user).first()
	if token:
		# delete old token
		token.delete()
	return Response(status=204)