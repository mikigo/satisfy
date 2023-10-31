from ninja import NinjaAPI
from django.conf import settings
from location.models import Location
from location.views import LocationSchema

api = NinjaAPI(
    title=settings.PROJECT_NAME.title() + " API",
    version="1.0.0",
    description="""
    Authoer: mikigo
    """,
)


@api.get("/hello")
def hello(request):
    res = {"res": "mikigo"}
    return res

@api.get("/location", response=LocationSchema)
def get_location_info(request):
    res = Location.objects.all()
    return res