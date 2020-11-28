# Generated by Django 3.1.2 on 2020-11-23 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myBlogApp', '0004_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(max_length=1000),
        ),
        migrations.CreateModel(
            name='Postcomment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myBlogApp.postcomment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myBlogApp.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
