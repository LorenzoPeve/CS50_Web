from datetime import datetime, timedelta
import django
import os
import sys

# Required for models to load
project_root =os.path.abspath(os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '..', 'commerce'))
sys.path.insert(0, project_root)

os.environ['DJANGO_SETTINGS_MODULE'] ='commerce.settings'
django.setup()


from auctions.models import Listing, User, Comment


# Creating three UFC-related users
user1 =User(
    username="conormcgregor",
    email="conor@ufc.com",
    first_name="Conor",
    last_name="McGregor"
)
user1.set_password("notorious")
user1.save()

user2 =User(
    username="amandanunes",
    email="amanda@ufc.com",
    first_name="Amanda",
    last_name="Nunes"
)
user2.set_password("lioness")
user2.save()

user3 =User(
    username="khabibnurmagomedov",
    email="khabib@ufc.com",
    first_name="Khabib",
    last_name="Nurmagomedov"
)
user3.set_password("eagle")
user3.save()


listing1 =Listing(   
    title='Toyota Corolla',
    description='Toyota Corolla 2014 80,000 miles',
    current_bid=14000,
    category='Automotive',
    image_url="https://portfolio8aff35a6cba45be.blob.core.windows.net/djangoapp/corolla.png",
    owner=user2
)
listing1.save()


listing2 =Listing(  
    title='Porsche',
    description='Porsche 911 Like NEW!',
    current_bid=80000,
    category='Automotive',
    image_url="https://portfolio8aff35a6cba45be.blob.core.windows.net/djangoapp/porsche.png",
    owner=user1
)
listing2.save()

listing3 =Listing( 
    title='Subaru',
    description='1 out of 40',
    current_bid=140000,
    category='Automotive',
    image_url="https://portfolio8aff35a6cba45be.blob.core.windows.net/djangoapp/subaru.png",
    owner=user1
)
listing3.save()

listing4 =Listing( 
    title='Tesla',
    description='Tesla Model 3 - You will never go back to gas',
    current_bid=80000,
    category='Automotive',
    image_url="https://portfolio8aff35a6cba45be.blob.core.windows.net/djangoapp/tesla.png",
    owner=user1
)
listing4.save()

listing5 =Listing(
    title='Luxury Sedan - 2022 Mercedes-Benz S-Class',
    description="This 2022 Mercedes-Benz S-Class is the epitome of luxury and performance. With its sleek design, advanced technology, and powerful engine, it's a car that's sure to turn heads on the road. Whether you're commuting in the city or embarking on a cross-country road trip, this sedan offers an unparalleled driving experience.",
    current_bid=150000,
    category='Automotive',
    image_url="https://portfolio8aff35a6cba45be.blob.core.windows.net/djangoapp/tesla.png",
    owner=user3
)
listing5.save()

comm_1 =Comment(
    listing=listing1,
    author=user1,
    date=datetime.now() - timedelta(days=3),
    comment='Looks great! What is the VIN number?'
)
comm_1.save()

comm_2 =Comment(
    listing=listing1,
    author=user2,
    date=datetime.now() - timedelta(days=2),
    comment='It is V12324-328-12312'
)
comm_2.save()

comm_3 =Comment(
    listing=listing1,
    author=user1,
    date=datetime.now() - timedelta(days=1),
    comment='Thanks! I will be placing a bid soon.'
)
comm_3.save()