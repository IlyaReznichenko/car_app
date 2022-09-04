from django.db import models

class CarsModel(models.Model):
    vin_code = models.CharField('VIN-код', max_length=17, blank=False)
    brand = models.CharField('Марка', max_length=20, blank=False)
    model = models.CharField('Модель', max_length=30, blank=False)
    configuration = models.CharField('Комплектация', max_length=30, blank=False)
    price = models.PositiveIntegerField('Цена', blank=False)

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)

class CustomerModel(models.Model):
    full_name = models.CharField('ФИО', max_length=75, blank=False)
    date_of_birth = models.DateField('Дата рождения', auto_now=False, auto_now_add=False)
    driving_license_number = models.CharField('Номер водительского удостоверения', max_length=10)
    car = models.ForeignKey(CarsModel, on_delete=models.CASCADE)

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)