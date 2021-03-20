import factory
import datetime
import random
from ejercicio_2.models import Company


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    year_constitution = str(random.randint(1900, 2021))
    name = factory.Sequence(lambda n: 'Company %d' % n)
    rut = factory.Sequence(lambda n: str((int(n) % 10)) * 8)
    dv = factory.Iterator(list(map(str, range(10))) + ['k'])
    address = factory.Sequence(lambda n: 'Address #%s street' % n)
    contact_phone = str(random.randint(11111111, 99999999))
    created = factory.LazyFunction(datetime.datetime.now)
