from django.db import models


class CallHistory(models.Model):
    fio = models.CharField('ФИО', max_length=100)
    date = models.DateTimeField('Дата обращения')
    text = models.CharField('Тип обращения', max_length=300)
    clientId = models.ForeignKey('ClientInfo', on_delete=models.CASCADE)##################
    bankId = models.ForeignKey('Bank', on_delete=models.CASCADE)##########################

    names = ["id", "ФИО студента", "Дата", "Куда выдается справка", "id студента", "Тип справки"]

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'История обращений за справкой'
        verbose_name_plural = 'История обращений за справкой'


class ClientInfo(models.Model):
    address = models.CharField('Адрес', max_length=150)
    age = models.IntegerField('Возраст', default=0)
    phoneNumber = models.IntegerField('Номер телефона', default=0)
    clientId = models.OneToOneField('ClientGroup', on_delete=models.CASCADE)

    names = ["id", "Адрес", "Возраст", "Номер телефона", "id студента"]

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Информация о студентах'
        verbose_name_plural = 'Информация о студентах'


class ClientGroup(models.Model):
    isRelible = models.BooleanField('Бакалавр', default=False)
    isVIP = models.BooleanField('Магистр', default=False)
    type = models.CharField('Курс студента', max_length=50)

    names = ["id", "Бакалавр", "Магистр", "Курс студента"]

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Группа студентов'
        verbose_name_plural = 'Группы студентов'


class Bank(models.Model):
    bankName = models.CharField('Название справки', max_length=50)
    address = models.CharField('Адрес', max_length=150)
    bankType = models.ManyToManyField('BankType')############################

    names = ["id", "Название справки", "Адрес", "Тип справки"]

    def __str__(self):
        return self.bankName

    class Meta:
        verbose_name = 'Справка'
        verbose_name_plural = 'Справка'


class BankType(models.Model):
    bankType = models.CharField('Тип справки', max_length=100)

    names = ["id", "Тип справки"]

    def __str__(self):
        return self.bankType

    class Meta:
        verbose_name = 'Тип справки'
        verbose_name_plural = 'Тип справки'


# class User(models.Model):
#     login = models.CharField(max_length=150, default="")
#     password = models.CharField(max_length=150, default="")
#     role = models.CharField(max_length=150, default="client")
#
#     names = ["Индекс", "Логин", "Пароль", "Роль"]
#     title = "Пользователи"
#
#     class Meta:
#         verbose_name = 'Тип банка'
#         verbose_name_plural = 'Типы банков'
#
#
#     def __str__(self):
#         return str(self.login)
#
