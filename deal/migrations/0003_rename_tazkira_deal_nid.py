# Generated by Django 4.2.3 on 2024-11-10 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0002_alter_deal_agent_alter_deal_deal_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deal',
            old_name='tazkira',
            new_name='nid',
        ),
    ]