from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import AuditLog
from AUTH.utils import DetailPermissions, view_permission_required, UserCustomNav


@view_permission_required
def LogWithAuditManagement(request, task_name="Audit", action="main"):
    r = request.GET
    uname = r.get('uname')
    keyword = r.get('keyword')
    action = r.get('action')
    sdate = r.get('search_date')
    all_audits = AuditLog.objects.all().order_by('-timestamp')
    if uname:
        all_audits = all_audits.filter(user__icontains=uname)
    if keyword:
        all_audits = all_audits.filter(Q(action_details__icontains=keyword)| Q(data__icontains=keyword)).order_by('-timestamp')
    if action:
        all_audits = all_audits.filter(action_name__icontains=action).order_by('-timestamp')
    if sdate:
        all_audits = all_audits.filter(timestamp__contains=sdate).order_by('-timestamp')
    
    paginator = Paginator(all_audits,20)
    page = request.GET.get('page')
    audits = paginator.get_page(page)

    context = {
        'audits' : audits,
        'privilege':DetailPermissions(request,task_name),
        'cnav': UserCustomNav(request, 'Operation'),
        
    }
    return render(request, 'AUTH/LogWithAudit/LogWithAuditManagement.html', context)


@view_permission_required
def LogWithAuditDetailsView(request, id, task_name="Audit", action="view"):
    audit = get_object_or_404(AuditLog, id = id)
    context = {
        'audit': audit,
        'cnav': UserCustomNav(request, 'Operation'),
    }
    return render(request, 'AUTH/LogWithAudit/LogWithAuditDetailsView.html', context)


def audit_update(request, action, table, task, details, prev):
    us = request.user.username
    x_f = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_f:
        uip = x_f.split(',')[0]
    else:
        uip = request.META.get('REMOTE_ADDR')
    try:
        deviceinfo = request.META['HTTP_USER_AGENT']
    except:
        deviceinfo = ''
    details = us + ' ' + details
    audit = AuditLog(user=us, user_ip=uip, device_info=deviceinfo, action_name=action, table_name=table, task_name=task, action_details=details, data = prev)
    audit.save()