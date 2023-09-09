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


from auctions.models import Listing, User, Comment, Bid


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
    title='2014 Toyota Corolla LE',
    description="""This 2014 Toyota Corolla LE is a reliable and fuel-efficient sedan with only 80,000 miles on the odometer. It's the perfect choice for daily commuting and city driving.""",
    current_bid=14000,
    category='Automotive',
    image_url='https://portfolio8aff35a6cba45be.blob.core.windows.net/djangoapp/corolla.png',
    owner=user2
)
listing1.save()


listing2 =Listing(  
    title='2019 Porsche 911 Carrera',
    description="""This 2019 Porsche 911 Carrera is in immaculate condition, truly like new! With only a few thousand miles on the odometer, it's a rare find for Porsche enthusiasts. Own a piece of automotive excellence today!""",
    current_bid=125000,
    category='Automotive',
    image_url="https://portfolio8aff35a6cba45be.blob.core.windows.net/djangoapp/porsche.jpg",
    owner=user1
)
listing2.save()

listing3 =Listing( 
    title='Rare 1998 Subaru Impreza 22B STi',
    description="""The 1998 Subaru Impreza 22B STi is a limited-production, rally-inspired legend, with only 400 units ever made.""",
    current_bid=80000,
    category='Automotive',
    image_url="https://portfolio8aff35a6cba45be.blob.core.windows.net/djangoapp/subaru.jpg",
    owner=user1
)
listing3.save()

listing4 =Listing( 
    title='2022 Tesla Model 3 Long Range',
    description="""Experience the future of driving with this 2022 Tesla Model 3 Long Range. Say goodbye to gas stations and hello to electric luxury.""",
    current_bid=80000,
    category='Automotive',
    image_url="https://portfolio8aff35a6cba45be.blob.core.windows.net/djangoapp/tesla.png",
    owner=user1
)
listing4.save()

listing5 =Listing(
    title='Luxury Sedan - 2022 Mercedes-Benz S-Class',
    description="""This 2022 Mercedes-Benz S-Class is the epitome of luxury and performance. Sleek design, advanced technology, and powerful engine. Unparallel driving experience.""",
    current_bid=150000,
    category='Automotive',
    image_url="https://portfolio8aff35a6cba45be.blob.core.windows.net/djangoapp/benz.png",
    owner=user3
)
listing5.save()

comm_1 =Comment(
    listing=listing1,
    author=user1,
    date=datetime.now() - timedelta(minutes=73),
    comment='Looks great! What is the VIN number?'
)
comm_1.save()

comm_2 =Comment(
    listing=listing1,
    author=user2,
    date=datetime.now() - timedelta(minutes=44),
    comment='It is V12324-328-12312'
)
comm_2.save()

comm_3 =Comment(
    listing=listing1,
    author=user1,
    date=datetime.now() - timedelta(minutes=10),
    comment='Thanks! I will be placing a bid soon.'
)
comm_3.save()


bid_1 = Bid(
    user=user1,
    listing=listing1,
    date=datetime.now() - timedelta(minutes=23),
    price=15000
)
bid_1.save()

bid_2 = Bid(
    user=user3,
    listing=listing1,
    date=datetime.now() - timedelta(minutes=15),
    price=15500
)
bid_2.save()

bid_3 = Bid(
    user=user1,
    listing=listing1,
    date=datetime.now() - timedelta(minutes=7),
    price=1800
)
bid_3.save()

listing1 = Listing(
    title='Wilson Pro Staff RF97',
    description="""The Wilson Pro Staff RF97 is a professional-grade tennis racket, favored by Roger Federer. With its precision and power, it's the perfect choice for advanced players looking to dominate the court.""",
    current_bid=250.00,
    category="Sports & Outdoors",
    image_url='https://portfolio8aff35a6cba45be.blob.core.windows.net/djangoapp/wilson.jpg',
    owner=user1
)
listing1.save()

# Listing 2 - Babolat Pure Drive
listing2 = Listing(
    title='Babolat Pure Drive',
    description="""The Babolat Pure Drive is known for its versatility and power. Whether you are a beginner or an intermediate player, this racket's combination of control and spin will elevate your game.""",
    current_bid=150.00,
    category="Sports & Outdoors",
    image_url='https://portfolio8aff35a6cba45be.blob.core.windows.net/djangoapp/babolat.jpg',
    owner=user2
)
listing2.save()

# Listing 3 - Head Graphene 360 Speed
listing3 = Listing(
    title='Head Graphene 360 Speed',
    description="""The Head Graphene 360 Speed offers exceptional maneuverability and control. It's a favorite among players who enjoy an agile racket that allows for precise shot placement.""",
    current_bid=180.00,
    category="Sports & Outdoors",
    image_url='https://portfolio8aff35a6cba45be.blob.core.windows.net/djangoapp/head.jpg',
    owner=user1
)
listing3.save()