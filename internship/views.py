from django.shortcuts import render , redirect 
from .forms import NewItemForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render ,get_object_or_404
from .models import Item , Category



# Create your views here.
def internships(request):
    items=Item.objects.filter(is_active=True)
    return render(request,'internships.html',{
        'items':items,
    })
    

@login_required
def new(request):

    if request.method=='POST':
        form = NewItemForm(request.POST,request.FILES)

        if form.is_valid():
            item=form.save(commit=False)
            item.created_by=request.user
            item.save()


            return redirect('browse')
    else:   

        form = NewItemForm()

    return render(request,'form.html',{
        'form':form,
        'title':'New item',
    })



def delete(request,pk):
    item=get_object_or_404(Item,pk=pk,created_by=request.user)
    item.delete()

    return redirect('browse')




@login_required
def edit(request,pk):
    item=get_object_or_404(Item,pk=pk,created_by=request.user)

    if request.method=='POST':
        form = EditItemForm(request.POST,request.FILES,instance=item)

        if form.is_valid():
            form.save()          
            return redirect('item:detail',pk=item.id)
    else:   
        form = EditItemForm(instance=item)


    return render(request,'form.html',{
        'form':form,
        'title':'Edit item',
    })

