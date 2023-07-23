from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from AUTH.utils import module_permission_required, UserCustomNav
from .utils import *
import psutil


@module_permission_required('Authorization')
def AuthDashboard(request):
    active_user_count = get_current_user()
    total_user_count = User.objects.all().count()
    cpu_physical_core_count = psutil.cpu_count(logical=False)
    cpu_total_core_count = psutil.cpu_count(logical=True)
    cpu_freq = psutil.cpu_freq()
    cpu_usage = psutil.cpu_percent()
    total_virtual_memory = psutil.virtual_memory()
    total_used_memory = get_size(total_virtual_memory.used)
    partitions = psutil.disk_partitions()
    disk_info_list = []
    for partition in partitions:
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        disk_info_list.append({
            'drive': partition.device,
            'total': get_size(partition_usage.total),
            'used': get_size(partition_usage.used),
            'percent': partition_usage.percent
        })
    net_io = psutil.net_io_counters()
    total_bytes_sent = get_size(net_io.bytes_sent)
    total_bytes_received = get_size(net_io.bytes_recv)
    total_packets_sent = net_io.packets_sent
    total_packets_received = net_io.packets_recv
    total_receiving_errors = net_io.errin
    total_sending_errors = net_io.errout
    total_receiving_packet_drops = net_io.dropin
    total_sending_packet_drops = net_io.dropout
    context = {
        'cnav' : UserCustomNav(request,'Authorization'),
        'auc': active_user_count,
        'tuc': total_user_count,
        'cpcc': cpu_physical_core_count,
        'cptc': cpu_total_core_count,
        'cf': cpu_freq,
        'cu': cpu_usage,
        'tvm': get_size(total_virtual_memory.total),
        'tum': total_used_memory,
        'tvmp': total_virtual_memory.percent,
        'dil': disk_info_list,
        'tbr': total_bytes_received,
        'tbs': total_bytes_sent,
        'tps': total_packets_sent,
        'tpr': total_packets_received,
        'tre': total_receiving_errors,
        'tse': total_sending_errors,
        'trpd': total_receiving_packet_drops,
        'tspd': total_sending_packet_drops
    }
    return render(request, 'AUTH/AuthDashboard/V1.html', context)
