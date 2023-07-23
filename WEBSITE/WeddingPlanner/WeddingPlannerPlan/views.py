from django.shortcuts import render, redirect
from django.http import JsonResponse
from CORE.WeddingPlanner.WpPlan.services import (AddCheckList, GetCheckList, DeleteCheckList, MarkCheckListComplete,
                                                 AddNote, GetNotes, AddDirectory, GetDirectory)
from CORE.WeddingPlanner.WpService.services import get_service_list_min
from WEBSITE.utils import visitor_required

@visitor_required()
def WeddingPlanChecklist(request):
    context = {
        "data": GetCheckList(request.user.id)
    }
    return render(request, 'WEBSITE/WeddingPlanner/WeddingCheckList.html', context)


@visitor_required()
def AddWeddingPlanChecklist(request):
    r = request.GET
    desc = r.get('desc')
    success = AddCheckList(request.user.id, desc)
    return JsonResponse({
        "success": success
    })


@visitor_required()
def MarkWeddingPlanChecklistComplete(request, id):
    MarkCheckListComplete(request.user.id, id)
    return redirect("WeddingPlanChecklist")


@visitor_required()
def DeleteWeddingPlanChecklist(request, id):
    DeleteCheckList(request.user.id, id)
    return redirect("WeddingPlanChecklist")


@visitor_required()
def WeddingPlanNote(request):
    context = {
        "data": GetNotes(request.user.id)
    }
    return render(request, 'WEBSITE/WeddingPlanner/WeddingNote.html', context)


@visitor_required()
def AddWeddingPlanNote(request):
    r = request.GET
    title = r.get('title')
    desc = r.get('desc')
    success = AddNote(request.user.id, title, desc)
    return JsonResponse({
        "success": success
    })


@visitor_required()
def WeddingPlanDirectory(request):
    context = {
        "services": get_service_list_min(),
        "data": GetDirectory(request.user.id)
    }
    return render(request, 'WEBSITE/WeddingPlanner/WeddingDirectory.html', context)


@visitor_required()
def AddWeddingPlanDirectory(request):
    r = request.GET
    serviceid = r.get('service')
    seller = r.get('seller')
    remarks = r.get('remarks')
    success = AddDirectory(request.user.id, serviceid, seller, remarks)
    return JsonResponse({
        "success": success
    })

