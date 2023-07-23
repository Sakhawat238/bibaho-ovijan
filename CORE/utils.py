from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from bibahoovijan import settings
import string
import random
import os


def getCommonResponse(success, msg):
    sts = 200 if success else 400
    CommonResponse = {
        'success': success,
        'msg': msg
    }
    return JsonResponse(CommonResponse, status=sts, safe=True)


def generate_unique_id_fixed_length_v1(size):
    chars = list(set(string.ascii_uppercase + string.ascii_lowercase +  string.digits))
    return ''.join(random.choices(chars, k=size))


def change_file_name(filename):
    extension = filename.split(".")[1]
    changed_file_name = generate_unique_id_fixed_length_v1(15)
    return "%s.%s" % (changed_file_name, extension)


def file_upload_server(myfile, folder_name, base_url):
    try:
        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, folder_name), base_url=base_url)
        filename = fs.save(myfile.name, myfile.file)
        return fs.url(filename)
    except Exception as e:
        return None