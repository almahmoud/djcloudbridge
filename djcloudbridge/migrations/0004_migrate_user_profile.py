# Generated by Django 2.1.1 on 2018-11-01 12:08
from django.db import migrations, models
from django.template.defaultfilters import slugify


def gen_user_profile(apps, schema_editor):
    UserModel = apps.get_model("auth.User")
    UserProfileModel = apps.get_model('djcloudbridge.UserProfile')
    for user in UserModel.objects.all():
        # Manually create slug because the save() method does not get
        # called during migrations
        UserProfileModel.objects.get_or_create(
            slug=slugify(user.username), user=user)


class Migration(migrations.Migration):

    dependencies = [
        ('djcloudbridge', '0003_move_azure_cloud_fields_to_creds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credentials',
            name='default',
            field=models.BooleanField(blank=True, default=False, help_text='If set, use as default credentials for the selected cloud'),
        ),
        migrations.RunPython(gen_user_profile, reverse_code=migrations.RunPython.noop)
    ]
