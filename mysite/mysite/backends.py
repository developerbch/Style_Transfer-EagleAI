from firebase_admin import auth
from illusion.models import MyUser


class FirebaseBackend:
    def authenticate(self, request, uid=None):
        try:
            auth.get_user(uid)
            return MyUser.objects.get(uid=uid)
        except MyUser.DoesNotExist:
            return MyUser.objects.create(uid=uid)
        except (auth.AuthError, ValueError):
            return None