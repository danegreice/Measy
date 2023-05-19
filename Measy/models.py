from django.db import models

class Metric(models.Model):
    name = models.CharField('Nome', max_length=50)
    ty = models.CharField('Tipo', max_length=50)
    description = models.TextField('Descrição')

    def __str__(self):
        return self.name

class Manager(models.Model):
    cpf = models.CharField(primary_key=True, max_length=14)
    name = models.CharField('Nome', max_length=50)
    email = models.EmailField('E-mail', max_length=50)
    phone = models.CharField('Telefone', max_length=16)
    login = models.CharField('Login', max_length=100)
    password = models.CharField('Password', max_length=100)

    def __str__(self):
        return self.cpf, self.name, self.login, self.password, self.email, self.phone

class Evaluation(models.Model):
    manager = models.ForeignKey(Manager, on_delete=models.PROTECT)
    metric = models.ForeignKey(Metric, on_delete=models.PROTECT)
    grade = models.IntegerField('Nota')
    comment = models.TextField('Comentário')

    def __str__(self):
        return f'{self.metric} - {self.manager}: {self.grade}'

class Project(models.Model):
    name = models.CharField('Nome', max_length=50)
    ty = models.CharField('Tipo', max_length=50)
    size = models.CharField('Tamanho do projeto',max_length=50)
    methodology = models.CharField('Metodologia utilizada',max_length=50)
    manager = models.ForeignKey(Manager, on_delete=models.PROTECT)
    description = models.TextField('Descrição')

    def __str__(self):
        return self.name