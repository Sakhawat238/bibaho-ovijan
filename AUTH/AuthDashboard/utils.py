# from django.contrib.auth.models import User
from AUTH.UserAuthentication.models import User

from django.contrib.sessions.models import Session
from django.utils import timezone


def get_current_user():
    active_sessions = Session.objects.filter(expire_date__gte=timezone.localtime(timezone.now()))
    user_id_list = []
    for session in active_sessions:
        data = session.get_decoded()
        user_id_list.append(data.get('_auth_user_id', None))
    return User.objects.filter(id__in=user_id_list).count()


def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor