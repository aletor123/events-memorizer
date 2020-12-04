import factory


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'event.Event'
    title = factory.Sequence(lambda x: f'title_{x}')
    place = factory.Sequence(lambda x: f'place_{x}')
    description = factory.Sequence(lambda x: f'description_{x}')
