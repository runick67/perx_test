import wtforms


class TaskForm(wtforms.Form):

    count = wtforms.IntegerField(
        'Количество элементов', description='Количество элементов')
    delta = wtforms.FloatField(
        'Дельта между элементами', description='Дельта')
    start = wtforms.FloatField(
        'Стартовое значение', description='Стартовое значение')
    interval = wtforms.FloatField(
        'Интервал в секундах между итерациями', description='Интервал')

    def validate_count(self, field):
        if not field.errors and field.data < 2:
            raise wtforms.ValidationError('Неверное число элементов')

    def validate_interval(self, field):
        if not field.errors and field.data < 0:
            raise wtforms.ValidationError('Интервал не может быть меньше нуля')
