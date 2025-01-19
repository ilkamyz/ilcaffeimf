from django import template

register = template.Library()


@register.filter
def conta(value, multiplier=0.4):
    #filtro che conta il tempo di lettura
    count = 1
    count = count + int(len(value.split()) * multiplier)
    print(count)
    if count < 60:
        return f"{count} secondi"
    else:
        a = count % 60
        if a > 1:
            return f"{int(count/60)} minuti e {a-1} secondi"
        else:
            return f"{int(count/60)} minuti"
