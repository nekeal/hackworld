import sys, os, django, requests
# sys.path.append("/path/to/store") #here store is root folder(means parent).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hackworld.settings")
django.setup()
from django.views.generic import CreateView
from people.models import City, Skill
api_key = "x4CimYBEUJ9n5xt6"
data = requests.get(f"https://trendyskills.com/service?q=keywords&like=&key={api_key}")
print(data)