from django.contrib import admin

# Register your models here.
from . import models

admin.site.register([
    models.Bookmark,
    models.Link,
    models.Tag,
    models.Vote
])
