from ninja import NinjaAPI

api = NinjaAPI(
    title="Satisfy",
    version="1.0.0",
    description="""
    Authoer: mikigo
    """,
)


@api.get("/hello")
def hello(request):
    res = {"res": "mikigo"}
    return res
