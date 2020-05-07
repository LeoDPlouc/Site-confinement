# Generated by Django 3.0.6 on 2020-05-07 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id_client', models.BigIntegerField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('mail', models.CharField(max_length=50)),
                ('nom', models.CharField(max_length=20, null=True)),
                ('tel', models.CharField(max_length=20, null=True)),
                ('adresse', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id_produit', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='commande_produit',
            fields=[
                ('id_commande_produit', models.BigIntegerField(primary_key=True, serialize=False)),
                ('confirm', models.BooleanField(default=False)),
                ('description', models.CharField(max_length=20)),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConfinAide.Client')),
                ('id_produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConfinAide.Produit')),
            ],
        ),
    ]
