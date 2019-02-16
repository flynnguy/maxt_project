import csv
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from . models import Member


def index(request):
    context = {}
    return render(request, 'index.html', context)

def rfid_csv(request):
    members = Member.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="rfid.csv"'

    writer = csv.writer(response)
    for member in members:
        if member.user.is_active:
            writer.writerow([member.user.username])
        else:
            writer.writerow(['*'+member.user.username])

    return response

def userinfo(request, username):
    member = get_object_or_404(Member, user__username=username)
    context = {'member': member}
    return render(request, 'member.html', context)
