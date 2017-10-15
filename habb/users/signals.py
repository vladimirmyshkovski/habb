from .models import User
#from django.db.models import signals
#from tastypie.models import create_api_key

#signals.post_save.connect(create_api_key, sender=User)

@receiver(post_save, sender=User)
def create_etc_and_btc(sender, instance, created, **kwargs):
	if created:
		instance.generate_token()