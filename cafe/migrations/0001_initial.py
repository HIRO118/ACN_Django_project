# Generated by Django 2.2.4 on 2019-08-05 15:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, verbose_name='カフェの名前')),
                ('desc', models.TextField(blank=True, verbose_name='カフェの説明')),
                ('img', models.TextField(blank=True, verbose_name='カフェの写真')),
                ('goeglemap', models.TextField(blank=True, verbose_name='位置情報')),
                ('instagram_link', models.TextField(verbose_name='インスタ')),
                ('phone_number', models.CharField(blank=True, max_length=20, verbose_name='電話番号')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
            ],
        ),
        migrations.CreateModel(
            name='CloseStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, verbose_name='最寄駅名')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='名無し', max_length=30, verbose_name='お名前')),
                ('text', models.TextField(verbose_name='本文')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cafe.Cafe', verbose_name='紐づくカフェ')),
            ],
        ),
        migrations.AddField(
            model_name='cafe',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cafe.CloseStation', verbose_name='最寄駅'),
        ),
    ]
