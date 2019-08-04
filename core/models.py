from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name


class ImoCalculation(models.Model):
	name = models.CharField(max_length=50, blank=False)
	imo_param_a = models.CharField(max_length=50, blank=True, null=True)
	imo_param_b = models.CharField(max_length=50, blank=True, null=True)
	imo_param_c = models.CharField(max_length=50, blank=True, null=True)
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.name

class DnvglCalculation(models.Model):
	name = models.CharField(max_length=50, blank=False)
	dnvgl_param1 = models.CharField(max_length=50, blank=True, null=True)
	dnvgl_param2 = models.CharField(max_length=50, blank=True, null=True)
	dnvgl_param3 = models.CharField(max_length=50, blank=True, null=True)
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	def __str__(self):
		return self.name