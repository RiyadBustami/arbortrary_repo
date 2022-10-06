from django.shortcuts import redirect, render,HttpResponse
from arbortrary_app.models import *
from datetime import datetime
from django.contrib import messages

# Create your views here.
def dashboard(request):
    context={
        'logged_user':User.objects.get(id=request.session['id']),
        'trees':Tree.objects.all(),
    }
    return render(request,'dashboard.html',context)

def plant_new_tree(request):
    if not 'id' in request.session:
        return redirect('/')
    context={
        'logged_user':User.objects.get(id=request.session['id']),
    }
    return render(request,'plant.html',context)

def add_new_plant(request):
    if not 'id' in request.session:
        return redirect('/')
    if request.method=='POST':
        errors=Tree.objects.tree_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/dashboard/new/tree/')
        else:
            species=request.POST['species']
            location=request.POST['location']
            reason=request.POST['reason']
            date_planted=request.POST['date_planted']
            planted_by=User.objects.get(id=request.session['id'])
            Tree.objects.create(species=species,location=location,reason=reason
                                    ,date_planted=date_planted,planted_by=planted_by)
            return redirect('/dashboard/new/tree/')

    else:
        return redirect('/')

def manage_trees(request): 
    if not 'id' in request.session:
        return redirect('/')
    context={
        'logged_user':User.objects.get(id=request.session['id']),
    }
    return render(request,"my_trees.html",context)

def show_tree(request,tree_id):
    if not 'id' in request.session:
        return redirect('/')
    try:
        tree_to_show=Tree.objects.get(id=tree_id)
    except:
        return redirect('/')
    else:
        context={
            'logged_user':User.objects.get(id=request.session['id']),
            'tree_to_show':tree_to_show,
        }

        return render(request,'show_tree.html',context)

def add_visit(request,tree_id):
    if not 'id' in request.session:
        return redirect('/')
    try:
        visited_tree=Tree.objects.get(id=tree_id)
    except:
        return redirect('/')
    else:
        visitor=User.objects.get(id=request.session['id'])
        visited_tree.visited_by.add(visitor)
        visited_tree.num_of_visits+=1
        visited_tree.save()
        return redirect('/dashboard/show/'+str(tree_id)+'/')


def delete_tree(request,tree_id):
    if not 'id' in request.session:
        return redirect('/')
    try:
        tb_deleted_tree=Tree.objects.get(id=tree_id)
    except:
        return redirect('/')
    else:
        if request.session['id']==tb_deleted_tree.planted_by.id:
            tb_deleted_tree.delete()
            return redirect('/dashboard/user/account/')
        else:
            return redirect('/')    

def edit_tree(request,tree_id):
    if not 'id' in request.session:
        return redirect('/')
    try:
        tb_edited_tree=Tree.objects.get(id=tree_id)
    except:
        
            return redirect('/') 
    else:
        if request.session['id']==tb_edited_tree.planted_by.id:
            tree_to_edit=Tree.objects.get(id=tree_id)
            tree_planting_date=datetime.strftime(tree_to_edit.date_planted,'%Y-%m-%d')
            context={
                'logged_user':User.objects.get(id=request.session['id']),
                'tree_to_edit':tree_to_edit,
                'tree_planting_date':tree_planting_date,
            }
            return render(request,'edit_tree.html',context)


def update_tree(request,tree_id):
    if not 'id' in request.session:
        return redirect('/')
    try:
        tb_edited_tree=Tree.objects.get(id=tree_id)
    except:
        
            return redirect('/') 
    else:
        if request.session['id']==tb_edited_tree.planted_by.id:
            if request.method == 'POST':
                errors=Tree.objects.tree_validator(request.POST)
                if len(errors)>0:
                    for key, value in errors.items():
                        messages.error(request, value)
                    return redirect('/dashboard/edit/'+str(tb_edited_tree.id)+'/')
                else:
                    tb_edited_tree.species=request.POST['species']
                    tb_edited_tree.location=request.POST['location']
                    tb_edited_tree.reason=request.POST['reason']
                    tb_edited_tree.date_planted=request.POST['date_planted']
                    tb_edited_tree.save()
                    return redirect('/dashboard/show/'+str(tb_edited_tree.id)+'/')
            else:
                return redirect('/')
            

