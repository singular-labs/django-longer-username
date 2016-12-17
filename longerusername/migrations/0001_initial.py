# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings

from longerusername import MAX_USERNAME_LENGTH


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL)
    ]

    operations = [
        migrations.RunSQL(
            sql=[
                ("ALTER TABLE auth_user MODIFY username VARCHAR(%s);", [MAX_USERNAME_LENGTH])
            ],
            reverse_sql=[
                ("ALTER TABLE auth_user MODIFY username VARCHAR(35);", [])
            ]
        )
    ]
