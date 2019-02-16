from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from . models import Tool
from . forms import AuthorizeToolForm

def tools(request):
    tools = Tool.objects.all()
    context = {'tools': tools}
    return render(request, 'tools.html', context)

def tool_page(request, tool_id):
    tool = get_object_or_404(Tool, pk=tool_id)
    context = {'tool': tool}
    return render(request, 'tool.html', context)

@login_required
@permission_required('tools.change_tool', 'tools.add_tool')
def authorize_user(request):
    if request.method == 'POST':
        form = AuthorizeToolForm(request.POST)
        if form.is_valid():
            tools = form.cleaned_data['authorize_tools']
            form.cleaned_data['user_to_authorize'].member.authorized_tools.add(*[tool.id for tool in tools])
            return HttpResponseRedirect(reverse('userinfo', args=[form.cleaned_data['user_to_authorize']]))
    else:
        form = AuthorizeToolForm()

    return render(request, 'authorize_user.html', {'form': form})
