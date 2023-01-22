# Generated by Django 4.1.2 on 2022-12-03 07:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('Doct_name', models.CharField(max_length=200)),
                ('opdate', models.DateField()),
                ('time_slot', models.TimeField()),
                ('p_problem', models.TextField()),
                ('tokenNum', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.CharField(max_length=100)),
                ('dep_head', models.CharField(max_length=100)),
                ('dep_location', models.CharField(max_length=100)),
                ('dep_phone', models.PositiveBigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doc_name', models.CharField(max_length=200)),
                ('doc_dob', models.DateField()),
                ('doc_specialization', models.CharField(blank=True, max_length=200, null=True)),
                ('doc_experience', models.CharField(blank=True, max_length=200, null=True)),
                ('doc_age', models.IntegerField()),
                ('doc_designation', models.CharField(max_length=200)),
                ('doc_qualification', models.CharField(max_length=200)),
                ('doc_depart', models.CharField(max_length=200)),
                ('doc_phone', models.IntegerField()),
                ('doc_gender', models.CharField(choices=[('.....', '.....'), ('Male', 'MALE'), ('Female', 'FEMALE')], default='.....', max_length=10)),
                ('doc_Martial', models.CharField(choices=[('.....', '......'), ('MARRIED', 'MARRIED'), ('SINGLE', 'SINGLE'), ('DIVERCED', 'DIVERCED')], default='.....', max_length=10)),
                ('doc_email', models.EmailField(max_length=254)),
                ('doc_address', models.CharField(blank=True, max_length=300, null=True)),
                ('doc_img', models.ImageField(blank=True, null=True, upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_name', models.CharField(max_length=60)),
                ('patient_dob', models.DateField()),
                ('patient_sex', models.CharField(choices=[('.....', '.....'), ('Male', 'MALE'), ('Female', 'FEMALE')], default='.....', max_length=20)),
                ('patient_martial', models.CharField(choices=[('.....', '......'), ('MARRIED', 'MARRIED'), ('SINGLE', 'SINGLE'), ('DIVERCED', 'DIVERCED')], default='.....', max_length=20)),
                ('patient_number', models.IntegerField(help_text='patient phone number')),
                ('patient_email', models.EmailField(max_length=254)),
                ('patient_height', models.FloatField(blank=True, null=True)),
                ('patient_weight', models.FloatField(blank=True, null=True)),
                ('patient_medicationHistory', models.TextField(blank=True, null=True)),
                ('emer_name', models.CharField(blank=True, max_length=200, null=True)),
                ('patient_img', models.ImageField(blank=True, default='images/default.jpg', null=True, upload_to='')),
                ('emer_contact', models.IntegerField(default=1)),
                ('emer_relation', models.CharField(blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
