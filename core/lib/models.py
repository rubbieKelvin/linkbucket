from django.db import models
from typing import Any

def getorcreate(model:type[models.Model], *get:models.Q, **create:Any) -> models.Model:
    instance = model.objects.filter(*get).first()
    if instance:
        return instance
    instance = model(**create)
    instance.save()
    return instance
