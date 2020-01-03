from django.shortcuts import render
from .forms import UploadForm
from .models import uploaded
from django.conf import settings 
# Create your views here.


def edit(request):
    if request.method=='POST':
        id=request.POST['id']
        data=uploaded.objects.get(id=id)
        form=UploadForm(initial={'charfield': data.charfield,'filefield': data.filefield })
        return render(request, 'edit.html', {'form':form,'id':id}) 


def task1(request):

    change=False

    if request.method=='POST':

        #while editing
        if 'id' in request.POST:
            charchange=False
            formchange=False
            id=request.POST['id']
            find=uploaded.objects.get(id=id)

            new_char=find.charfield
            new_file=find.filefield

            new_char= request.POST['charfield']
            if 'filefield' in request.POST and request.POST['filefield']:
                new_file= request.FILES['filefield']
                print("ok11")
            elif 'filefield' in request.FILES: 
                new_file= request.FILES['filefield']
                print("ok21")

            if find:
                if find.charfield != new_char:
                    print()
                    print('charfield for file_id:',id,'changed' )
                    print('old value:',find.charfield)
                    print('new value:',new_char)
                    print()
                    change=True

                if find.filefield != new_file:
                    print()
                    print('filefield for file_id:',id,'changed' )
                    print('old value:',find.filefield)
                    print('new value:',new_file)
                    print()
                    change=True

                if change:
                    _data = uploaded.objects.get(id=id)
                    _data.filefield=new_file
                    _data.charfield=new_char
                    _data.save()
                        
        #while uploading
        else:
            change=False
            form=UploadForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                data = uploaded.objects.latest('id')
                data = uploaded.objects.get(id=data.id)
                count=0

                #large operration on content of file
                with open(settings.MEDIA_ROOT+'/'+str(data.filefield), 'rb') as f:
                    while True:
                        fdata = f.read(4)
                        for i in range(1000):  
                            count+=1
                        if not fdata:
                            break
                #assignig charfield as large operation on filefield          
                data.charfield+=str(count)
                data.save()
                change=True 
                new_char = request.POST['charfield']
                new_file = request.FILES['filefield']
                print()
                print("New data added:")
                print("charfield =", new_char)
                print("filefield= ", new_file)
                print()

    existing_data = uploaded.objects.all() 
    form = UploadForm()           
    return render(request, 'task1.html', {'form': form,'existing_data':existing_data,'change':change})    
    

