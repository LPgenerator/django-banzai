# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0430\u0439\u043b\u0430')),
                ('file', models.FileField(upload_to=b'django_banzai/attachments', verbose_name='\u0444\u0430\u0439\u043b \u0432\u043b\u043e\u0436\u0435\u043d\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u0432\u043b\u043e\u0436\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u0432\u043b\u043e\u0436\u0435\u043d\u0438\u044f',
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=b'django_banzai/package', verbose_name='\u043f\u0430\u043a\u0435\u0442 \u0432 xml-\u0444\u043e\u0440\u043c\u0430\u0442\u0435')),
                ('status', models.CharField(blank=True, max_length=4, verbose_name='\u0441\u0442\u0430\u0442\u0443\u0441', choices=[(b'S001', '\u041f\u0430\u043a\u0435\u0442 \u043d\u0435 \u0431\u044b\u043b \u043d\u0430\u0439\u0434\u0435\u043d \u043f\u043e \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u043e\u043c\u0443 URL'), (b'S002', '\u041f\u0430\u043a\u0435\u0442 \u0437\u0430\u0433\u0440\u0443\u0436\u0435\u043d \u043d\u0430 \u0441\u0435\u0440\u0432\u0435\u0440'), (b'S004', '\u041f\u0430\u043a\u0435\u0442 \u0440\u0430\u0441\u0441\u044b\u043b\u0430\u0435\u0442\u0441\u044f'), (b'S005', '\u041f\u0430\u043a\u0435\u0442 \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d, \u043e\u0436\u0438\u0434\u0430\u0435\u043c \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438 \u043e \u043f\u0430\u043a\u0435\u0442\u0435 \u0438\u0437 \u0441\u0438\u0441\u0442\u0435\u043c\u044b'), (b'S006', '\u0412\u043e \u0432\u0440\u0435\u043c\u044f \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438 \u043f\u0440\u043e\u0438\u0437\u043e\u0448\u043b\u0438 \u043e\u0448\u0438\u0431\u043a\u0438'), (b'S007', '\u041d\u0435\u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u044b\u0439 \u0444\u043e\u0440\u043c\u0430\u0442 \u043f\u0430\u043a\u0435\u0442\u0430'), (b'S008', '\u041f\u0440\u0435\u0432\u044b\u0448\u0435\u043d\u043e \u0432\u0440\u0435\u043c\u044f \u043e\u0436\u0438\u0434\u0430\u043d\u0438\u044f \u043e\u0442\u0432\u0435\u0442\u0430 \u0441\u0435\u0440\u0432\u0435\u0440\u0430'), (b'S009', '\u041f\u0430\u043a\u0435\u0442 \u043f\u043e\u043b\u0443\u0447\u0435\u043d'), (b'S010', '\u041f\u0430\u043a\u0435\u0442 \u043f\u0440\u043e\u0432\u0435\u0440\u044f\u0435\u0442\u0441\u044f'), (b'S011', '\u041f\u0430\u043a\u0435\u0442 \u043e\u0431\u0440\u0430\u0431\u0430\u0442\u044b\u0432\u0430\u0435\u0442\u0441\u044f (\u0444\u043e\u0440\u043c\u0438\u0440\u0443\u044e\u0442\u0441\u044f \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f)'), (b'S012', '\u041f\u0430\u043a\u0435\u0442 \u043f\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d \u0432 \u043e\u0447\u0435\u0440\u0435\u0434\u044c \u043d\u0430 \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u0435'), (b'S013', '\u041f\u0430\u043a\u0435\u0442 \u0443\u0434\u0430\u043b\u0435\u043d. \u0420\u0430\u0441\u0441\u044b\u043b\u043a\u0430 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0439 \u043f\u0440\u0435\u043a\u0440\u0430\u0449\u0435\u043d\u0430'), (b'S015', '\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0430\u0434\u0440\u0435\u0441\u0430\u0442\u043e\u0432 \u043f\u0440\u0435\u0432\u044b\u0448\u0430\u0435\u0442 \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d\u043d\u044b\u0439 \u043b\u0438\u043c\u0438\u0442'), (b'S018', '\u041f\u0430\u043a\u0435\u0442 \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d. \u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u0430\u043a\u0435\u0442\u0435 \u0443\u0434\u0430\u043b\u0435\u043d\u0430'), (b'S019', '\u041f\u0430\u043a\u0435\u0442 \u043f\u0440\u043e\u0432\u0435\u0440\u0435\u043d, \u0431\u0443\u0434\u0435\u0442 \u0440\u0430\u0437\u043e\u0441\u043b\u0430\u043d \u0432 \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f'), (b'E000', '\u0421\u0435\u043a\u0440\u0435\u0442\u043d\u044b\u0439 \u043a\u043b\u044e\u0447, \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u044b\u0439 \u0432 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430\u0445 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438, \u043d\u0435 \u043e\u043f\u043e\u0437\u043d\u0430\u043d'), (b'E001', '\u041d\u0435 \u043f\u0435\u0440\u0435\u0434\u0430\u043d URL'), (b'E002', '\u041d\u0435 \u043f\u0435\u0440\u0435\u0434\u0430\u043d pack_id'), (b'E003', '\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u0430\u043a\u0435\u0442\u0435 \u043d\u0435 \u043d\u0430\u0439\u0434\u0435\u043d\u0430'), (b'E004', '\u041d\u0435\u0434\u043e\u0441\u0442\u0430\u0442\u043e\u0447\u043d\u043e \u0442\u0440\u0430\u0444\u0438\u043a\u0430'), (b'E005', '\u041d\u0435 \u043e\u043f\u043b\u0430\u0447\u0435\u043d \u0442\u0430\u0440\u0438\u0444'), (b'E006', '\u041d\u0435\u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u0432 \u043f\u0430\u043a\u0435\u0442\u0435')])),
                ('pack_id', models.CharField(max_length=100, verbose_name='ID \u043f\u0430\u043a\u0435\u0442\u0430 \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0435', blank=True)),
                ('emails_all', models.PositiveIntegerField(verbose_name='email\u043e\u0432 \u0432\u0441\u0435\u0433\u043e')),
                ('emails_correct', models.PositiveIntegerField(default=0, verbose_name='email\u043e\u0432 \u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u044b\u0445')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='\u043f\u0430\u043a\u0435\u0442 \u0441\u043e\u0437\u0434\u0430\u043d')),
                ('description', models.CharField(max_length=100, verbose_name='\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u0430\u043a\u0435\u0442\u0430', blank=True)),
            ],
            options={
                'verbose_name': '\u043f\u0430\u043a\u0435\u0442',
                'verbose_name_plural': '\u043f\u0430\u043a\u0435\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(blank=True, max_length=4, verbose_name='\u0441\u0442\u0430\u0442\u0443\u0441', choices=[(b'S001', '\u041f\u0430\u043a\u0435\u0442 \u043d\u0435 \u0431\u044b\u043b \u043d\u0430\u0439\u0434\u0435\u043d \u043f\u043e \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u043e\u043c\u0443 URL'), (b'S002', '\u041f\u0430\u043a\u0435\u0442 \u0437\u0430\u0433\u0440\u0443\u0436\u0435\u043d \u043d\u0430 \u0441\u0435\u0440\u0432\u0435\u0440'), (b'S004', '\u041f\u0430\u043a\u0435\u0442 \u0440\u0430\u0441\u0441\u044b\u043b\u0430\u0435\u0442\u0441\u044f'), (b'S005', '\u041f\u0430\u043a\u0435\u0442 \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d, \u043e\u0436\u0438\u0434\u0430\u0435\u043c \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438 \u043e \u043f\u0430\u043a\u0435\u0442\u0435 \u0438\u0437 \u0441\u0438\u0441\u0442\u0435\u043c\u044b'), (b'S006', '\u0412\u043e \u0432\u0440\u0435\u043c\u044f \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438 \u043f\u0440\u043e\u0438\u0437\u043e\u0448\u043b\u0438 \u043e\u0448\u0438\u0431\u043a\u0438'), (b'S007', '\u041d\u0435\u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u044b\u0439 \u0444\u043e\u0440\u043c\u0430\u0442 \u043f\u0430\u043a\u0435\u0442\u0430'), (b'S008', '\u041f\u0440\u0435\u0432\u044b\u0448\u0435\u043d\u043e \u0432\u0440\u0435\u043c\u044f \u043e\u0436\u0438\u0434\u0430\u043d\u0438\u044f \u043e\u0442\u0432\u0435\u0442\u0430 \u0441\u0435\u0440\u0432\u0435\u0440\u0430'), (b'S009', '\u041f\u0430\u043a\u0435\u0442 \u043f\u043e\u043b\u0443\u0447\u0435\u043d'), (b'S010', '\u041f\u0430\u043a\u0435\u0442 \u043f\u0440\u043e\u0432\u0435\u0440\u044f\u0435\u0442\u0441\u044f'), (b'S011', '\u041f\u0430\u043a\u0435\u0442 \u043e\u0431\u0440\u0430\u0431\u0430\u0442\u044b\u0432\u0430\u0435\u0442\u0441\u044f (\u0444\u043e\u0440\u043c\u0438\u0440\u0443\u044e\u0442\u0441\u044f \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f)'), (b'S012', '\u041f\u0430\u043a\u0435\u0442 \u043f\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d \u0432 \u043e\u0447\u0435\u0440\u0435\u0434\u044c \u043d\u0430 \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u0435'), (b'S013', '\u041f\u0430\u043a\u0435\u0442 \u0443\u0434\u0430\u043b\u0435\u043d. \u0420\u0430\u0441\u0441\u044b\u043b\u043a\u0430 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0439 \u043f\u0440\u0435\u043a\u0440\u0430\u0449\u0435\u043d\u0430'), (b'S015', '\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0430\u0434\u0440\u0435\u0441\u0430\u0442\u043e\u0432 \u043f\u0440\u0435\u0432\u044b\u0448\u0430\u0435\u0442 \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d\u043d\u044b\u0439 \u043b\u0438\u043c\u0438\u0442'), (b'S018', '\u041f\u0430\u043a\u0435\u0442 \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d. \u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u0430\u043a\u0435\u0442\u0435 \u0443\u0434\u0430\u043b\u0435\u043d\u0430'), (b'S019', '\u041f\u0430\u043a\u0435\u0442 \u043f\u0440\u043e\u0432\u0435\u0440\u0435\u043d, \u0431\u0443\u0434\u0435\u0442 \u0440\u0430\u0437\u043e\u0441\u043b\u0430\u043d \u0432 \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f'), (b'E000', '\u0421\u0435\u043a\u0440\u0435\u0442\u043d\u044b\u0439 \u043a\u043b\u044e\u0447, \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u044b\u0439 \u0432 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430\u0445 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438, \u043d\u0435 \u043e\u043f\u043e\u0437\u043d\u0430\u043d'), (b'E001', '\u041d\u0435 \u043f\u0435\u0440\u0435\u0434\u0430\u043d URL'), (b'E002', '\u041d\u0435 \u043f\u0435\u0440\u0435\u0434\u0430\u043d pack_id'), (b'E003', '\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u0430\u043a\u0435\u0442\u0435 \u043d\u0435 \u043d\u0430\u0439\u0434\u0435\u043d\u0430'), (b'E004', '\u041d\u0435\u0434\u043e\u0441\u0442\u0430\u0442\u043e\u0447\u043d\u043e \u0442\u0440\u0430\u0444\u0438\u043a\u0430'), (b'E005', '\u041d\u0435 \u043e\u043f\u043b\u0430\u0447\u0435\u043d \u0442\u0430\u0440\u0438\u0444'), (b'E006', '\u041d\u0435\u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u0432 \u043f\u0430\u043a\u0435\u0442\u0435')])),
                ('email', models.EmailField(max_length=254, verbose_name='email', blank=True)),
                ('reject_code', models.CharField(max_length=250, verbose_name='\u043a\u043e\u0434 \u043e\u0448\u0438\u0431\u043a\u0438', blank=True)),
                ('reject_message', models.TextField(verbose_name='\u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u043e\u0431 \u043e\u0448\u0438\u0431\u043a\u0435', blank=True)),
                ('package', models.ForeignKey(related_name='reports', verbose_name='\u043f\u0430\u043a\u0435\u0442', to='banzai.Package')),
            ],
            options={
                'verbose_name': '\u043e\u0442\u0447\u0451\u0442',
                'verbose_name_plural': '\u043e\u0442\u0447\u0451\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='ReportFBL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(blank=True, max_length=4, verbose_name='\u0441\u0442\u0430\u0442\u0443\u0441', choices=[(b'S001', '\u041f\u0430\u043a\u0435\u0442 \u043d\u0435 \u0431\u044b\u043b \u043d\u0430\u0439\u0434\u0435\u043d \u043f\u043e \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u043e\u043c\u0443 URL'), (b'S002', '\u041f\u0430\u043a\u0435\u0442 \u0437\u0430\u0433\u0440\u0443\u0436\u0435\u043d \u043d\u0430 \u0441\u0435\u0440\u0432\u0435\u0440'), (b'S004', '\u041f\u0430\u043a\u0435\u0442 \u0440\u0430\u0441\u0441\u044b\u043b\u0430\u0435\u0442\u0441\u044f'), (b'S005', '\u041f\u0430\u043a\u0435\u0442 \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d, \u043e\u0436\u0438\u0434\u0430\u0435\u043c \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438 \u043e \u043f\u0430\u043a\u0435\u0442\u0435 \u0438\u0437 \u0441\u0438\u0441\u0442\u0435\u043c\u044b'), (b'S006', '\u0412\u043e \u0432\u0440\u0435\u043c\u044f \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438 \u043f\u0440\u043e\u0438\u0437\u043e\u0448\u043b\u0438 \u043e\u0448\u0438\u0431\u043a\u0438'), (b'S007', '\u041d\u0435\u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u044b\u0439 \u0444\u043e\u0440\u043c\u0430\u0442 \u043f\u0430\u043a\u0435\u0442\u0430'), (b'S008', '\u041f\u0440\u0435\u0432\u044b\u0448\u0435\u043d\u043e \u0432\u0440\u0435\u043c\u044f \u043e\u0436\u0438\u0434\u0430\u043d\u0438\u044f \u043e\u0442\u0432\u0435\u0442\u0430 \u0441\u0435\u0440\u0432\u0435\u0440\u0430'), (b'S009', '\u041f\u0430\u043a\u0435\u0442 \u043f\u043e\u043b\u0443\u0447\u0435\u043d'), (b'S010', '\u041f\u0430\u043a\u0435\u0442 \u043f\u0440\u043e\u0432\u0435\u0440\u044f\u0435\u0442\u0441\u044f'), (b'S011', '\u041f\u0430\u043a\u0435\u0442 \u043e\u0431\u0440\u0430\u0431\u0430\u0442\u044b\u0432\u0430\u0435\u0442\u0441\u044f (\u0444\u043e\u0440\u043c\u0438\u0440\u0443\u044e\u0442\u0441\u044f \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f)'), (b'S012', '\u041f\u0430\u043a\u0435\u0442 \u043f\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d \u0432 \u043e\u0447\u0435\u0440\u0435\u0434\u044c \u043d\u0430 \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u0435'), (b'S013', '\u041f\u0430\u043a\u0435\u0442 \u0443\u0434\u0430\u043b\u0435\u043d. \u0420\u0430\u0441\u0441\u044b\u043b\u043a\u0430 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0439 \u043f\u0440\u0435\u043a\u0440\u0430\u0449\u0435\u043d\u0430'), (b'S015', '\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0430\u0434\u0440\u0435\u0441\u0430\u0442\u043e\u0432 \u043f\u0440\u0435\u0432\u044b\u0448\u0430\u0435\u0442 \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d\u043d\u044b\u0439 \u043b\u0438\u043c\u0438\u0442'), (b'S018', '\u041f\u0430\u043a\u0435\u0442 \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d. \u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u0430\u043a\u0435\u0442\u0435 \u0443\u0434\u0430\u043b\u0435\u043d\u0430'), (b'S019', '\u041f\u0430\u043a\u0435\u0442 \u043f\u0440\u043e\u0432\u0435\u0440\u0435\u043d, \u0431\u0443\u0434\u0435\u0442 \u0440\u0430\u0437\u043e\u0441\u043b\u0430\u043d \u0432 \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f'), (b'E000', '\u0421\u0435\u043a\u0440\u0435\u0442\u043d\u044b\u0439 \u043a\u043b\u044e\u0447, \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u044b\u0439 \u0432 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430\u0445 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438, \u043d\u0435 \u043e\u043f\u043e\u0437\u043d\u0430\u043d'), (b'E001', '\u041d\u0435 \u043f\u0435\u0440\u0435\u0434\u0430\u043d URL'), (b'E002', '\u041d\u0435 \u043f\u0435\u0440\u0435\u0434\u0430\u043d pack_id'), (b'E003', '\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u0430\u043a\u0435\u0442\u0435 \u043d\u0435 \u043d\u0430\u0439\u0434\u0435\u043d\u0430'), (b'E004', '\u041d\u0435\u0434\u043e\u0441\u0442\u0430\u0442\u043e\u0447\u043d\u043e \u0442\u0440\u0430\u0444\u0438\u043a\u0430'), (b'E005', '\u041d\u0435 \u043e\u043f\u043b\u0430\u0447\u0435\u043d \u0442\u0430\u0440\u0438\u0444'), (b'E006', '\u041d\u0435\u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u0432 \u043f\u0430\u043a\u0435\u0442\u0435')])),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('package', models.ForeignKey(related_name='reports_fbl', verbose_name='\u043f\u0430\u043a\u0435\u0442', to='banzai.Package')),
            ],
            options={
                'verbose_name': '\u043e\u0442\u0447\u0451\u0442 \u043e FBL',
                'verbose_name_plural': '\u043e\u0442\u0447\u0451\u0442\u044b \u043e FBL',
            },
        ),
        migrations.AddField(
            model_name='attachment',
            name='package',
            field=models.ForeignKey(related_name='attachments', verbose_name='\u043f\u0430\u043a\u0435\u0442', to='banzai.Package'),
        ),
    ]
