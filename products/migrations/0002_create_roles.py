from django.db import migrations


def create_roles(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    # Оператор — работа с лидами
    operator_group, _ = Group.objects.get_or_create(name='Оператор')
    lead_perms = Permission.objects.filter(codename__in=['add_lead', 'change_lead', 'view_lead', 'delete_lead'])
    operator_group.permissions.set(lead_perms)

    # Маркетолог — услуги и реклама
    marketer_group, _ = Group.objects.get_or_create(name='Маркетолог')
    product_perms = Permission.objects.filter(codename__in=['add_product', 'change_product', 'view_product', 'delete_product'])
    ad_perms = Permission.objects.filter(codename__in=['add_advertisement', 'change_advertisement', 'view_advertisement', 'delete_advertisement'])
    marketer_group.permissions.set(product_perms | ad_perms)

    # Менеджер — контракты и активные клиенты
    manager_group, _ = Group.objects.get_or_create(name='Менеджер')
    contract_perms = Permission.objects.filter(codename__in=['add_contract', 'change_contract', 'view_contract', 'delete_contract'])
    customer_perms = Permission.objects.filter(codename__in=['add_customer', 'change_customer', 'view_customer', 'delete_customer'])
    manager_group.permissions.set(contract_perms | customer_perms)


def remove_roles(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.filter(name__in=['Оператор', 'Маркетолог', 'Менеджер']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('leads', '0001_initial'),
        ('advertisements', '0001_initial'),
        ('contracts', '0001_initial'),
        ('customers', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.RunPython(create_roles, remove_roles),
    ]
