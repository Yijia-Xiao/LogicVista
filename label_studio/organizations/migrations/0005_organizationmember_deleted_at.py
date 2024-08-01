# Generated by Django 3.2.20 on 2023-10-23 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0004_organization_contact_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationmember',
            name='deleted_at',
            field=models.DateTimeField(db_index=True, default=None, help_text='Timestamp indicating when the organization member was marked as deleted.  If NULL, the member is not considered deleted.', null=True, verbose_name='deleted at'),
        ),
    ]
