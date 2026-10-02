from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_employee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='title',
            new_name='full_name',
        ),
    ]
