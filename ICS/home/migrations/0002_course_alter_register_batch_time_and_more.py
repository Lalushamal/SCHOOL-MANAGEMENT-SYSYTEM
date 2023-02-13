# Generated by Django 4.1 on 2023-01-12 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='register',
            name='batch_time',
            field=models.TextField(choices=[('9-12', '9-12'), ('12TO2', '12TO2'), ('2TO5', '2TO5')]),
        ),
        migrations.AlterField(
            model_name='register',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.course'),
        ),
    ]