from django.shortcuts                     import render, get_object_or_404, redirect
from django.utils                         import timezone
from django.contrib.auth.decorators       import login_required
from django.contrib.auth.models           import User
from .models                              import Event, Userdetail
from .forms                               import EventForm

def event_list(request):
  eventxs                       = Event.objects.filter(is_live=True,event_date__gte=timezone.now()).order_by('event_date')
  events                        = []

  if request.user.is_authenticated():
    user                        = User.objects.get(id=request.user.id)
    userdetail                  = user.userdetail
    for eventx in eventxs:
      if user.is_superuser      == True:
        editable                = '1'
      elif eventx.author         == userdetail:
        editable                = '1'
      elif eventx.schememanager  == userdetail:
        editable                = '1'
      else:
        editable                = '0'
      event                     = [ eventx, editable ]
      events.append(event)
  else:
    for eventx in eventxs:
      editable                  = '0'
      event                     = [ eventx, editable ]   
      events.append(event)
  return render(request, 'ogevents/event_list.html', {'events': events, 'period':'1'})

def event_list_past(request):
  eventxs = Event.objects.filter(is_live=True,event_date__lt=timezone.now()).order_by('-event_date')
  events                        = []

  if request.user.is_authenticated():
    user                        = User.objects.get(id=request.user.id)
    userdetail                  = user.userdetail
    for eventx in eventxs:
      if user.is_superuser      == True:
        editable                = '1'
      elif eventx.author         == userdetail:
        editable                = '1'
      elif eventx.schememanager  == userdetail:
        editable                = '1'
      else:
        editable                = '0'
      event                     = [ eventx, editable ]
      events.append(event)
  else:
    for eventx in eventxs:
      editable                  = '0'
      event                     = [ eventx, editable ]   
      events.append(event)
  return render(request, 'ogevents/event_list.html', {'events': events, 'period':'0'})

@login_required
def event_detail(request, pk):
  event = get_object_or_404(Event, pk=pk)
  return render(request, 'ogevents/event_detail.html', {'event': event})

@login_required
def event_new(request):
  if request.method              == "POST":
    form                         = EventForm(request.POST)
    if form.is_valid():
      event                      = form.save(commit=False)
      if event.event_date < timezone.localtime(timezone.now()).date():
        return render(request, 'ogevents/event_edit.html', {'form': form})
      user                       = User.objects.get(id=request.user.id)
      userdetail                 = user.userdetail

      schememanager              = Userdetail.objects.get(schememanager=userdetail.schememanager,is_schememanager=True)
      event.author_name          = user.username
      event.author               = userdetail
      event.schememanager        = schememanager
      event.save()

      return redirect('ogevents.views.event_list')
  else:
    form = EventForm()
  return render(request, 'ogevents/event_edit.html', {'form': form})

@login_required
def event_new_past(request):
  if request.method              == "POST":
    form                         = EventForm(request.POST)
    if form.is_valid():
      event                      = form.save(commit=False)

      user                       = User.objects.get(id=request.user.id)
      userdetail                 = user.userdetail

      schememanager              = Userdetail.objects.get(schememanager=userdetail.schememanager,is_schememanager=True)
      event.author_name          = user.username
      event.author               = userdetail
      event.schememanager        = schememanager
      event.save()

      return redirect('ogevents.views.event_list_past')
  else:
    form = EventForm()
  return render(request, 'ogevents/event_edit.html', {'form': form})

@login_required
def event_edit(request, period, pk):
  event                          = get_object_or_404(Event, pk=pk)

  if request.method              == "POST":
    form = EventForm(request.POST, instance=event)
    if form.is_valid():
      event                      = form.save(commit=False)

      user = User.objects.get(id=request.user.id)
      userdetail                 = user.userdetail

      if user.is_superuser       == True:
        pass
      elif event.author          == userdetail:
        pass
      elif event.schememanager   == userdetail:
        pass
      else:
        return render(request, 'ogevents/event_edit.html', {'form': form})

      event.author_name          = user.username
      event.author               = userdetail
      event.save()

      if period == '1':
        return redirect('ogevents.views.event_list')
      else:
        return redirect('ogevents.views.event_list_past')
  else:
    form = EventForm(instance=event)
  return render(request, 'ogevents/event_edit.html', {'form': form})

@login_required
def event_remove(request, period, pk):
  event = get_object_or_404(Event, pk=pk)
  
  user                           = User.objects.get(id=request.user.id)
  userdetail                     = user.userdetail

  if user.is_superuser           == True:
    event.delete()
  elif event.author              == userdetail:
    event.delete()
  elif event.schememanager       == userdetail:
    event.delete()
  else:
    pass
    # error message
  
  if period == '1':
    return redirect('ogevents.views.event_list')
  else:
    return redirect('ogevents.views.event_list_past')
