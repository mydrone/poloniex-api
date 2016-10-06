from django.db import models

class Log(models.Model):
    action = models.TextField()
    parameters = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '[{}] : {} a été exécuté avec les paramètres {}'.format(self.timestamp, self.action, self.parameters)

class ApiCredentials(models.Model):
    key = models.TextField()
    secret = models.TextField()