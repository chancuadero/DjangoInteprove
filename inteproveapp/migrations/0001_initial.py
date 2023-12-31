# Generated by Django 4.1.6 on 2023-05-27 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('investorprofileid', models.AutoField(primary_key=True, serialize=False)),
                ('profilename', models.TextField(max_length=255)),
                ('profiletype', models.TextField(max_length=255)),
                ('status', models.CharField(default='Not Started', max_length=20)),
                ('taskid', models.CharField(max_length=20, null=True)),
                ('date', models.DateField()),
                ('allocated', models.CharField(default='No', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=15)),
                ('firstname', models.CharField(max_length=15)),
                ('lastname', models.CharField(max_length=15)),
                ('type', models.CharField(choices=[('R', 'Researcher'), ('S', 'Supervisor')], default='R', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Researcher',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inteproveapp.user')),
                ('researcherid', models.CharField(default=1, max_length=50)),
            ],
            bases=('inteproveapp.user',),
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inteproveapp.user')),
                ('supervisorid', models.CharField(default=2, max_length=50)),
            ],
            bases=('inteproveapp.user',),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('projectid', models.AutoField(primary_key=True, serialize=False)),
                ('projectname', models.CharField(default='Tier 8', max_length=255)),
                ('investorprofileid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inteproveapp.investor')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inteproveapp.user')),
            ],
        ),
    ]
