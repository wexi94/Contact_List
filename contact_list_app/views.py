from django.shortcuts import render, redirect

from contact_list_app.models import Contact


def index(request):
    contacts=Contact.objects.all()
    search_input = request.GET.get('search-area')
    if search_input:
        contacts = Contact.objects.filter(Full_Name__icontains=search_input)
    else:
        contacts = Contact.objects.all()
        search_input = ''
    return render(request,'index.html',{'contacts':contacts, 'search_input': search_input})
def addContact(request):
    if request.method=='POST':
        new_contact=Contact(
            Full_Name=request.POST['fullname'],
            Relationship=request.POST['relationship'],
            Email=request.POST['email'],
            Phone_No=request.POST['phone-number'],
            Address=request.POST['address']
        )
        new_contact.save()
        return redirect('/')
    return render(request,'add.html')


def Contactprofile(request, pk):
    contact=Contact.objects.get(id=pk)
    return render(request,'contact-profile.html',{'contact': contact})

def editContact(request, pk):
    contact = Contact.objects.get(id=pk)
    if request.method=='POST':
        contact.Full_Name=request.POST['fullname']
        contact.Relationship = request.POST['relationship']
        contact.Email = request.POST['email']
        contact.Phone_No = request.POST['phone-number']
        contact.Address = request.POST['address']
        contact.save()
        return redirect('/profile/'+str(contact.id))
    return render(request,'edit.html',{'contact': contact})

def deleteContact(request, pk):
    contact=Contact.objects.get(id=pk)
    if request.method=='POST':
        contact.delete()
        return redirect('/')
    return render(request,'delete.html',{'contact': contact})