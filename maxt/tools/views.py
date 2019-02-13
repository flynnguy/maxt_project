from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from . models import Tool

def tools(request):
    tools = Tool.objects.all()
    context = {'tools': tools}
    return render(request, 'tools.html', context)

def tool_page(request, tool_id):
    tool = get_object_or_404(Tool, pk=tool_id)
    context = {'tool': tool}
    return render(request, 'tool.html', context)
