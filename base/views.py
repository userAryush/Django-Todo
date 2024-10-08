from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.

# HOME VIEW
# request garda objects ma aauxa tara response pathauda json or http ma pathaune
# home view will display home page in response
# request compulsory linei parxa ani request aayesi repsonse pathaunei parxa
def home(request): # home page ko url hit garda request janxa tei yo home vitra jko param wala request ho
    
    # query to bring all the data of Todo model database's table
    todo_obj = Todo.objects.all()   
    data = {'todos':todo_obj}
    return render(request, 'home.html', context=data)  
    # render sends the html file as response
    
#todo_obj = Todo.objects.all()-> databasetable.attribute.method,, object le query gareko vayera sabei data will be a object jun class lai call gareko tesei ko object hunxa,, generally database bata data lyauda data haru raw vayera tuple ma aauthyo ani value haru index garnu parthyo so garo hunthyo tara ahile objects use garera garda sabei data object aauxa so tesko attribute ta easily call garna milyo

# data = {'todo':todo_obj} -> variable ko data directly pathauna milena kina vane data lai etikei frontend lai pathayo vane ta tesle kasari call garxaso teslai key assign garera pathaune 

#context param bata chai data lai frontend ma pathaune ho





# frontend le backend lai data in json(quotation"" vitra key:value) format ma pathauxa when clicked on submit ani yei data lera database ma query garnu paro or create garne
def create(request):
    if request.method == 'POST':
        #form ko field vitra ko name parameter ma j cha tei tya fill gareko value harko key hunxa junchei ya get garne ma lekheko cha
        name = request.POST.get('name')  #request.POST ma aauxa data ani tei bata data haru get garne
        degree = request.POST.get('degree')
        description = request.POST.get('description')
        status = request.POST.get('status')
        number = request.POST.get('number')
        if number == "":
            number= None 

        Todo.objects.create(name=name, degree=degree, description=description, job_status=status, number=number)#db ma create garxa,, key haru model ko attribute ho
        return redirect('home')
    
    
    return render(request, 'create.html',  )


def edit(request, pk): # url ma pk aayesi ya pani param rakhna paro
    todo_obj = Todo.objects.get(id=pk)#get method le euta mtra data lyaune kam garxa tara k ko adhar ma lyaune tyo chai param ma pathauna paro
    data = {'todo':todo_obj}
    if request.method == 'POST':
        name = request.POST.get('name')  #request.POST ma aauxa data ani json ma ni hunxa so tei bata data haru get garne
        degree = request.POST.get('degree')
        description = request.POST.get('description')
        status = request.POST.get('status')
        number = request.POST.get('number')  
          
        todo_obj.name = name
        todo_obj.degree = degree
        todo_obj.description = description
        todo_obj.job_status = status
        todo_obj.number = number
        if number == "":
            todo_obj.number= None 
        todo_obj.save()
        return redirect('home')
        
            
    return render(request, 'edit.html',context=data)

def delete(request,pk):
    todo = Todo.objects.get(id=pk)
    # todo = Todo.objects.filter(name='delete garna ko lagi certain kura') yesari chai milne data haru ekei choti delete garna milo 
    todo.delete()
    return redirect('home') # redirect le request ma aako url lai arko url ma pass garna milxa

def deleteall(request):
    all_todo = Todo.objects.all()
    all_todo.delete()
    return redirect('home')