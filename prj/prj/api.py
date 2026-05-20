from ninja import NinjaAPI, Schema
from ninja.orm import ModelSchema
from app.models import Meme

api = NinjaAPI()

class Message(Schema):
    message : str

class MemeSchema(ModelSchema):
    class Meta:
        model = Meme
        fields = "__all__"

    user_username: str | None = None

    @classmethod
    def resolve_user_username(cls, obj):
        try:
            return obj.user.username
        except Exception:
            return None

@api.get("/memes")
def list_memes(request):
    memes = Meme.objects.all()
    return {"memes": [MemeSchema.from_orm(meme) for meme in memes]}

@api.get("/meme/{meme_id}", response={200: MemeSchema, 404: Message})
def get_meme(request, meme_id: int):
    try:
        meme = Meme.objects.get(id=meme_id)
        return MemeSchema.from_orm(meme)
    except Meme.DoesNotExist:
        return 404, {"message": "Meme not found"}