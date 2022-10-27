
from django.db import models
from django.utils import timezone
from django.urls import reverse
import uuid


# Create your models here.


class ProjectFacility (models.Model):
    """Model representing a project facilities."""
    
    name = models.CharField(max_length=200, help_text='Enter a product feature (e.g. Swimming-pool CCTV Solar-power)')

    class meta :
        verbose_name = "Facility"
        verbose_name_plural = "Facilities"


    def __str__(self):
        """String for representing the Model object."""
        return self.name





class Project (models.Model):
        """Model representing a project."""

        name = models.CharField(max_length=250)
       

        description = models.TextField(max_length=1000, help_text='Enter a brief description of the project')
        location = models.CharField(max_length=300)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        hectares = models.DecimalField(max_digits=6, decimal_places=1, help_text="Enter the number of hectares",null=True, blank=True,)
        
        facilities = models.ManyToManyField(ProjectFacility, help_text='Select a feature for this project')
        image= models.ImageField(upload_to='images/')

    

        PROJECT_STATUS = (
        ('Not started', 'Not started'),
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
    )

        status = models.CharField(
        max_length=50,
        choices= PROJECT_STATUS,
        blank=True,
        default='Not started',
        help_text='Project work status',
    )

        PROJECT_PURPOSE = (
        ('Residential', 'Residential'),
        ('Commercial', 'Commercial'),
        ('Others', 'Others'),
    )

        purpose = models.CharField(
        max_length=50,
        choices= PROJECT_PURPOSE,
        blank=True,
        default='Residential',
        help_text='Project purpose',
    )

        class meta :
            ordering = ['-name'] 
            verbose_name = 'Projects'

    
        def __str__(self):
            """String for representing the Model object."""
            return self.name
        
        def get_absolute_url(self):

            """Returns the URL to access a detail record for this project."""
            return reverse('project_detail', args=[str(self.id)])


class HouseFeature (models.Model):
    """Model representing a product feature."""
    
    name = models.CharField(max_length=200, help_text='Enter a product feature (e.g. Fan Kitchen-cabinet wardropes)')

    class meta :
        verbose_name_plural = 'Features' 


    def __str__(self):
        """String for representing the Model object."""
        return self.name



class HouseType (models.Model):
    """Model representing a project HouseType."""

    house_name = models.CharField(max_length=250, null= True, blank= True)
    house_specification = models.CharField(max_length=300, help_text='Enter a brief specification of the product')
    house_floor_area = models.PositiveBigIntegerField(help_text="Enter the net floor area for the product")
    features = models.ManyToManyField(HouseFeature, help_text='Select a feature for this product')
    units = models.PositiveIntegerField(null= True, blank=True)
    house_outright_payment = models.DecimalField(max_digits=12, decimal_places=2, help_text="Enter the outright payment price", default= 0)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


    class meta :
            ordering = ['-house_name'] 
            verbose_name = 'HouseTypes'

    
    def __str__(self):
            """String for representing the Model object."""
            return self.house_name