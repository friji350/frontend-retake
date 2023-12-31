from django.db import models

class Item(models.Model):
    class Meta():
        db_table = 'all_items'
        verbose_name = 'all items'
        verbose_name_plural = 'all items'

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    img = models.CharField(max_length=200)
    description = models.CharField(max_length=200)


# Create your models here.















# CharField- Используется для определения строк фиксированной длины от короткой до средней. Вы должны указать max_length для хранения данных.
# TextField - используется для больших строк произвольной длины. Вы можете указать max_length для поля, но это используется только тогда, когда поле отображается в формах (оно не применяется на уровне базы данных).
# IntegerField- это поле для хранения значений (целого числа) и для проверки введённых значений в виде целых чисел в формах.
# DateField и DateTimeField - используются для хранения / представления дат и информации о дате / времени (как Python datetime.date и datetime.datetime, соответственно). Эти поля могут дополнительно объявлять (взаимоисключающие) параметры auto_now=True (для установки поля на текущую дату каждый раз, когда модель сохраняется), auto_now_add (только для установки даты, когда модель была впервые создана) и по умолчанию (чтобы установить дату по умолчанию, которую пользователь может переустановить).
# EmailField - используется для хранения и проверки адресов электронной почты. Пройдем позже при регистрации
# FileField и ImageField - используются для загрузки файлов и изображений соответственно ( ImageField просто добавляет дополнительную проверку, что загруженный файл является изображением). Они имеют параметры для определения того, как и где хранятся загруженные файлы.
# AutoField - это особый тип IntegerField, который автоматически увеличивается. Первичный ключ этого типа автоматически добавляется в вашу модель, если вы явно не укажете его.
# ForeignKey - Используется для указания отношения «один ко многим» к другой модели базы данных (например, автомобиль имеет одного производителя, но производитель может делать много автомобилей). «Одна» сторона отношения - это модель, содержащая ключ.
# ManyToManyField - используется для определения отношения «многие ко многим» (например, книга может иметь несколько жанров, и каждый жанр может содержать несколько книг). В нашем приложении для библиотек мы будем использовать их аналогично ForeignKeys, но их можно использовать более сложными способами для описания отношений между группами. Они имеют параметр on_delete, чтобы определить, что происходит, когда связанная запись удаляется (например, значение models.SET_NULL просто установило бы значение NULL)