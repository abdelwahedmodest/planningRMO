from django.shortcuts import render
from  core  import  settings
import redis

def my_view(request):
    # Connect to Redis
    r = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)

    # Set a value
    r.set('my_key', 'my_value')

    # Get a value
    value = r.get('my_key')

    return render(request, 'my_template.html', {'value': value})

