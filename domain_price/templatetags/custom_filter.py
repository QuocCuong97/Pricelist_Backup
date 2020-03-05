from django import template


register = template.Library()


def currency(value):
    new_value = str(value)
    if len(new_value) > 3 and len(new_value) <= 6:
        result = new_value[:-3] + '.' + new_value[-3:]
    elif len(new_value) > 6 and len(new_value) <= 9:
        result = new_value[:-6] + '.' + new_value[-6:-3] + '.' + new_value[-3:]
    else:
        pass
    return result


register.filter('currency', currency)