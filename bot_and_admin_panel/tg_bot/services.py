from core.models import Text, User


def create_user(user_id):
    User.objects.get_or_create(
        user_id=user_id[0]
    )


def get_text():
    return Text.objects.order_by('?').first()
