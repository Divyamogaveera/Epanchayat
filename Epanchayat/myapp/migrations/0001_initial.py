# Generated by Django 3.2.3 on 2021-10-22 15:18

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.TextField(max_length=30, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(blank=True, max_length=150)),
                ('date_joined', models.DateTimeField(default=datetime.datetime.now)),
                ('email', models.EmailField(max_length=225, unique=True, verbose_name='email address')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('I prefer not to say', 'I prefer not to say')], max_length=20)),
                ('phone', models.IntegerField()),
                ('wardno', models.IntegerField()),
                ('Birth_date', models.DateField(blank=True, help_text='YY-MM-DD')),
                ('grampanchayat', models.CharField(help_text='Enter your panchayat', max_length=40)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='approve1',
            fields=[
                ('app_id', models.AutoField(primary_key=True, serialize=False)),
                ('income_no', models.CharField(blank=True, max_length=300, null=True, unique=True)),
                ('name', models.CharField(default='', max_length=100)),
                ('houseno', models.CharField(blank=True, max_length=8, unique=True)),
                ('decision', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='approve2',
            fields=[
                ('app_id', models.AutoField(primary_key=True, serialize=False)),
                ('job_no', models.CharField(blank=True, max_length=300, null=True, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('decision', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='approve3',
            fields=[
                ('app_id', models.AutoField(primary_key=True, serialize=False)),
                ('gas_no', models.CharField(blank=True, max_length=300, null=True, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('ration_no', models.CharField(blank=True, max_length=10, unique=True)),
                ('decision', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='approve4',
            fields=[
                ('app_id', models.AutoField(primary_key=True, serialize=False)),
                ('curr_no', models.CharField(blank=True, max_length=300, null=True, unique=True)),
                ('service_name', models.CharField(default='abcd', max_length=100, null=True)),
                ('keyno', models.CharField(blank=True, max_length=80, unique=True)),
                ('decision', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='imgsall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allimg', models.ImageField(blank=True, upload_to='allimg')),
                ('document', models.FileField(blank=True, upload_to='document')),
            ],
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('service_id', models.AutoField(primary_key=True, serialize=False)),
                ('service_name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('requirements', models.CharField(blank=True, max_length=300)),
                ('user', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='service_Z',
            fields=[
                ('curr_id', models.AutoField(primary_key=True, serialize=False)),
                ('service_name', models.CharField(default='', max_length=100, null=True)),
                ('name', models.CharField(max_length=100)),
                ('house_no', models.CharField(blank=True, max_length=8)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHERS', 'OTHERS')], max_length=50)),
                ('village', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('pin', models.PositiveIntegerField()),
                ('state', models.CharField(choices=[('karnataka', 'karnataka'), ('andrapradesh', 'andrapradesh')], max_length=100)),
                ('mobile', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('panchayat', models.CharField(choices=[('aloor', 'aloor'), ('kota', 'kota'), ('Kundapur', 'Kundapur')], max_length=100)),
                ('keyno', models.CharField(max_length=80, unique=True)),
                ('bpl_img', models.FileField(blank=True, upload_to='rationimg')),
                ('adhar_img', models.FileField(blank=True, upload_to='adharimg')),
                ('bnk_img', models.FileField(blank=True, upload_to='bankimg')),
                ('user_img', models.FileField(blank=True, upload_to='profileimg')),
                ('vote_img', models.FileField(blank=True, upload_to='voteimg')),
                ('pan_img', models.FileField(blank=True, upload_to='panimg')),
                ('incm_img', models.FileField(blank=True, upload_to='incmimg')),
                ('cst_img', models.FileField(blank=True, upload_to='cstimg')),
                ('scldoc', models.FileField(blank=True, upload_to='sclimg')),
                ('otdc_img', models.FileField(blank=True, upload_to='panimg')),
                ('servicez_id', models.ForeignKey(default='4', on_delete=django.db.models.deletion.PROTECT, to='myapp.service')),
                ('user', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='service_C',
            fields=[
                ('gas_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('ration_no', models.CharField(blank=True, max_length=10, unique=True)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHERS', 'OTHERS')], max_length=50)),
                ('village', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('pin', models.PositiveIntegerField()),
                ('state', models.CharField(choices=[('karnataka', 'karnataka'), ('andrapradesh', 'andrapradesh')], max_length=100)),
                ('mobile', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('panchayat', models.CharField(choices=[('aloor', 'aloor'), ('kota', 'kota'), ('Kundapur', 'Kundapur')], max_length=100)),
                ('bpl_img', models.FileField(blank=True, upload_to='rationimg')),
                ('adhar_img', models.FileField(blank=True, upload_to='adharimg')),
                ('bnk_img', models.FileField(blank=True, upload_to='bankimg')),
                ('user_img', models.FileField(blank=True, upload_to='profileimg')),
                ('servicec_id', models.ForeignKey(default='3', on_delete=django.db.models.deletion.PROTECT, to='myapp.service')),
                ('user', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service_B',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHERS', 'OTHERS')], max_length=50)),
                ('village', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('pin', models.PositiveIntegerField()),
                ('state', models.CharField(choices=[('karnataka', 'karnataka'), ('andrapradesh', 'andrapradesh')], max_length=100)),
                ('mobile', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('panchayat', models.CharField(choices=[('aloor', 'aloor'), ('kota', 'kota'), ('Kundapur', 'Kundapur')], max_length=100)),
                ('job_panchayat', models.CharField(choices=[('Aloor', 'Aloor'), ('Kota', 'Kota'), ('Kundapur', 'Kundapur')], max_length=100)),
                ('profile_img', models.FileField(blank=True, upload_to='profileimg')),
                ('hscssc', models.FileField(blank=True, upload_to='school')),
                ('document', models.FileField(blank=True, upload_to='doc')),
                ('serviceb_id', models.ForeignKey(default='2', on_delete=django.db.models.deletion.PROTECT, to='myapp.service')),
                ('user', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='service_A',
            fields=[
                ('income_id', models.AutoField(primary_key=True, serialize=False)),
                ('service_name', models.CharField(blank=True, max_length=50)),
                ('house_no', models.CharField(blank=True, max_length=8, unique=True)),
                ('user_name', models.CharField(default='', max_length=100)),
                ('user_image', models.FileField(blank=True, upload_to='images/')),
                ('firstname', models.CharField(max_length=122)),
                ('lastname', models.CharField(blank=True, max_length=250)),
                ('email', models.EmailField(max_length=30)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=20)),
                ('wardno', models.IntegerField(default=0)),
                ('grampanchayat', models.CharField(blank=True, choices=[('aloor', 'aloor'), ('kota', 'kota'), ('Kundapur', 'Kundapur')], max_length=40)),
                ('phone', models.CharField(max_length=12, null=True)),
                ('village', models.CharField(max_length=150, verbose_name='address')),
                ('city', models.CharField(default='kundapura', max_length=100, verbose_name='city')),
                ('state', models.CharField(choices=[('KARNATAKA', 'KARNATAKA'), ('TAMILNADU', 'TAMILNADU')], max_length=50)),
                ('pin_code', models.CharField(max_length=100, verbose_name='pin_code')),
                ('adhar_no', models.CharField(default='', max_length=12)),
                ('adhar_img', models.FileField(blank=True, upload_to='images/')),
                ('incom_proof', models.FileField(default='', upload_to='images/')),
                ('vote', models.FileField(default='', upload_to='images/')),
                ('apply_date', models.DateField(null=True)),
                ('servicea_id', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='myapp.service')),
                ('user', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=122)),
                ('email', models.EmailField(max_length=250)),
                ('phone', models.CharField(max_length=12)),
                ('wardno', models.IntegerField(default=0)),
                ('grampanchayat', models.CharField(max_length=50)),
                ('rate', models.TextField()),
                ('adinfo', models.TextField()),
                ('date', models.DateField()),
                ('user', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=122)),
                ('email', models.EmailField(max_length=250)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('I prefer not to say', 'I prefer not to say')], max_length=20)),
                ('phone', models.CharField(max_length=12)),
                ('grampanchayat', models.CharField(max_length=50)),
                ('wardno', models.IntegerField(default=0)),
                ('info', models.TextField()),
                ('adinfo', models.TextField()),
                ('date', models.DateField()),
                ('user', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('complaints_id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=122)),
                ('lastname', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=30)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('I prefer not to say', 'I prefer not to say')], max_length=20)),
                ('wardno', models.IntegerField(default=0)),
                ('grampanchayat', models.CharField(blank=True, max_length=40)),
                ('complaint', models.TextField()),
                ('date', models.DateField()),
                ('user', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
