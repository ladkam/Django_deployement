import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','second_project.settings')

import django
# Import settings
django.setup()

import random
from apptwo.models import user
from faker import Faker

fakegen = Faker()

def populate(N=100):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Get Topic for Entry

        # Create Fake Data for entry
        fake_mail = fakegen.email()
        fake_name = fakegen.name()
        fake_last = fakegen.name()

        # Create new Webpage Entry

        # Create Fake Access Record for that page
        # Could add more of these if you wanted...
        new = user.objects.get_or_create(FirstName=fake_name,LastName=fake_last,email=fake_mail)[0]


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')
