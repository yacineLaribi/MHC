from django.shortcuts import render , redirect ,get_object_or_404
from .forms import NewRequestForm
from .models import NewRequestModel
from internship.models import Item
# Create your views here.

def NewRequest(request):
    if request.method=='POST':
        form = NewRequestForm(request.POST,request.FILES)

        if form.is_valid():
            request=form.save(commit=False)
            request.requested_by=request.user
            # request.requested_to=Item.created_by
            request.save()


            return redirect('browse')
        else:   
            form = NewRequestForm()

    return render(request,'form.html',{
        'form':form,
        'title':'Request for Internship',
    })
