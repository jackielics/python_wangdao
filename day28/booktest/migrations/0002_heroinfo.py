# Generated by Django 3.2 on 2023-03-15 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=20)),
                ('hgender', models.BooleanField(default=False)),
                ('hcomment', models.CharField(max_length=100)),
                ('hbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booktest.bookinfo')),
            ],
        ),
    ]
