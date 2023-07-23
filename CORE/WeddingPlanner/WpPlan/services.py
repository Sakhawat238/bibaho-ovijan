from .models import Checklist, Note, Directory


def AddCheckList(userid, description):
    try:
        C = Checklist(user_id=userid, description=description)
        C.save()
        return True
    except:
        return False
    

def GetCheckList(userid):
    return Checklist.objects.filter(user_id=userid).all()


def MarkCheckListComplete(userid, id):
    try:
        Checklist.objects.filter(user_id=userid, id=id).update(is_completed=True)
        return True
    except:
        return False
    

def  DeleteCheckList(userid, id):
    try:
        Checklist.objects.filter(user_id=userid, id=id).delete()
        return True
    except:
        return False


def AddNote(userid, title, description):
    try:
        N = Note(user_id=userid, title=title, description=description)
        N.save()
        return True
    except:
        return False


def GetNotes(userid):
    return Note.objects.filter(user_id=userid).all()


def  DeleteNote(userid, id):
    try:
        Note.objects.filter(user_id=userid, id=id).delete()
        return True
    except:
        return False
    

def AddDirectory(userid, serviceid, sellerinfo, remarks):
    try:
        D = Directory(user_id=userid, service_id=serviceid, seller_info=sellerinfo, remarks=remarks)
        D.save()
        return True
    except:
        return False


def GetDirectory(userid):
    Dir = Directory.objects.select_related('service').filter(user_id=userid).all()
    list = {}
    for d in Dir:
        if d.service.title in list:
            list[d.service.title].append(d)
        else:
            list[d.service.title] = [d]
    return list


def  DeleteDirectory(userid, id):
    try:
        Directory.objects.filter(user_id=userid, id=id).delete()
        return True
    except:
        return False