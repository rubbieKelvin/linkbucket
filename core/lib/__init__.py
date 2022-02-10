from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.serializers import ModelSerializer

from django.db import models

from typing import Any
from typing import Type
from typing import cast

def paginatedResponse(request: Request, queryset:models.QuerySet, sr:Type[ModelSerializer], sr_context:dict[str, Any]|None=None) -> Response:
	""" returns a paginated list of items.
	"""
	pg = PageNumberPagination()

	res = pg.paginate_queryset(queryset, request)
	res = sr(res, many=True, context=sr_context or {}).data
	return pg.get_paginated_response(res)
