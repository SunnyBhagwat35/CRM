from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import Group, User


from .models import Customer

def customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)
        Customer.objects.create(
            user = instance,
            name = instance.username,
        )
        print("customer profile created...!!!")
    else:
        print("something went wrong")

# def customer_profile(sender, instance, **kwargs):
#     if instance.username:
#         print("profile in creatingg...!!!")
#     else:
#         print("something went wrong username not present")

# pre_save.connect(customer_profile, sender=User)
post_save.connect(customer_profile, sender=User)