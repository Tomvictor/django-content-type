from core.models import *


# create some projects
p1 = Project.objects.create(name = "my first project")
p2 = Project.objects.create(name = "my second project")
p3 = Project.objects.create(name = "my third project")
p4 = Project.objects.create(name = "my fourth project")
p5 = Project.objects.create(name = "my fifth project")
p6 = Project.objects.create(name = "my sixth project")
p7 = Project.objects.create(name = "my seventh project")

# list all projects
projects = Project.objects.all()
print(f"project count : {projects.count()}")
for project in projects:
    print(f"project id : {project.id} | {project.name}")

# imo calculations

imo1 = ImoCalculation.objects.create(
    name= "first calculation",
    project = p1
)

imo2 = ImoCalculation.objects.create(
    name= "second calculation",
    project = p1
)

imo3 = ImoCalculation.objects.create(
    name= "second calculation",
    project = p1
)

dnv1 = DnvglCalculation.objects.create(
    name= "dnvgl1",
    project = p1
)

dnv2 = DnvglCalculation.objects.create(
    name= "dnvgl2",
    project = p1
)