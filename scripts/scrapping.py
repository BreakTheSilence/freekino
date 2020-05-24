import sys, os, django, json

project_dir = "C:/Users/Kirill/PycharmProjects/djng/djng"

sys.path.append(project_dir)

os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

django.setup()

from player.models import Films

Films.objects.all().delete()
print(Films.objects.all())

with open("forkk.json", encoding="utf8") as json_file:
    data = json.load(json_file)
    for i in range(len(data)):
        print(f"Adding film {data[i]['title']}")
        f = Films()
        f.title = data[i]["title"]
        f.link = data[i]["link"]
        f.description = data[i]["description"]
        f.save()

print(F"Ready")
