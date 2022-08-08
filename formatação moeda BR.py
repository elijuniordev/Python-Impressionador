from decimal import Decimal
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR')


valor = Decimal('1254897.25')
print(locale.currency(valor, grouping=True))