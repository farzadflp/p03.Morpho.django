from djongo import models


class DHT11(models.Model):
    name = models.CharField()
    description = models.CharField()
    temperature = models.CharField()
    humidity = models.CharField()
    gpio = models.CharField()
    status = models.CharField()
    unit_temp = models.CharField(default='celsius')
    unit_humidity = models.CharField(default='%')
    frequency = models.IntegerField(default=5000)

    def __str__(self):
        return f'temperature:{self.temperature}\n' \
               f'humidity:{self.humidity}'


class PIR(models.Model):
    name = models.CharField()
    description = models.CharField()
    value = models.BooleanField()
    lock = models.BooleanField()
    gpio = models.IntegerField()
    status = models.BooleanField()

    def __str__(self):
        return f'value:{self.value}\n' \
               f'lock:{self.lock}'


class Actuator(models.Model):
    name = models.CharField()
    description = models.CharField()
    value = models.BooleanField()
    gpio = models.IntegerField()
    status = models.BooleanField()
    def __str__(self):
        return f'value:{self.value}'
