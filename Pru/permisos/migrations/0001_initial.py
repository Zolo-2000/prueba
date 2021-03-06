# Generated by Django 3.0.4 on 2020-03-16 20:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_ausencia', models.PositiveSmallIntegerField(choices=[(1, 'CARGO A VACACIONES'), (2, 'ENFERMEDAD'), (3, 'COMPENSACION'), (4, 'CALAMIDAD'), (5, 'PRESENTAR CERTIFICADO')], default=1)),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_desde', models.DateTimeField()),
                ('fecha_hasta', models.DateTimeField()),
                ('dias', models.PositiveSmallIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
