from django.shortcuts import render, redirect
from .models import Student

# Home + Add
def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")

        if name and email and age:
            Student.objects.create(
                name=name,
                email=email,
                age=int(age)
            )
            return redirect('show')

    return render(request, "index.html")


# Show Data
def show(request):
    data = Student.objects.all()
    return render(request, "show.html", {"data": data})


# Delete
def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('show')


# Edit
def edit(request, id):
    student = Student.objects.get(id=id)
    return render(request, "edit.html", {"student": student})


# Update
def update(request, id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        student.name = request.POST.get("name")
        student.email = request.POST.get("email")
        student.age = request.POST.get("age")
        student.save()
        return redirect('show')

    return render(request, "edit.html", {"student": student})