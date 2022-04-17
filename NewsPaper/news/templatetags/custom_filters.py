from django import template

register = template.Library()

censor_words = ['boring', 'problems']


@register.filter()
def censor(value):
    for word in value.split():
        if word.strip('.,') in censor_words:
            value = value.replace(word, (word[:1] + ('*' * (len(word) - 1))))
    return value


