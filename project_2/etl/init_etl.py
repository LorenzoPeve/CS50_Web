
import django
import os
import sys

# Required for models to load
project_root = os.path.abspath(os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '..', 'commerce'))
sys.path.insert(0, project_root)

os.environ['DJANGO_SETTINGS_MODULE'] = 'commerce.settings'
django.setup()


from auctions.models import Listing


def etl():
    data = [
        {
            'title': 'Toyota Corolla',
            'description': 'Toyota Corolla 2014 80,000 miles',
            'current_bid': 14000,
            'category': 'Automotive',
            'image_url': "https://portfolio8aff35a6cba45be.blob.core.windows.net/djangoapp/corolla.png",
        },
        {
            'title': 'Porsche',
            'description': 'Porsche 911 Like NEW!',
            'current_bid': 80000,
            'category': 'Automotive',
            'image_url': "https://portfolio8aff35a6cba45be.blob.core.windows.net/djangoapp/porsche.png"
        },
        {
            'title': 'Subaru',
            'description': '1 out of 40',
            'current_bid': 140000,
            'category': 'Automotive',
            'image_url': "https://portfolio8aff35a6cba45be.blob.core.windows.net/djangoapp/subaru.png"
        },
        {
            'title': 'Tesla',
            'description': 'Tesla Model 3 - You will never go back to gas',
            'current_bid': 80000,
            'category': 'Automotive',
            'image_url': "https://portfolio8aff35a6cba45be.blob.core.windows.net/djangoapp/tesla.png"
        },
        {
            'title': 'Luxury Sedan - 2022 Mercedes-Benz S-Class',
            'description': "This 2022 Mercedes-Benz S-Class is the epitome of luxury and performance. With its sleek design, advanced technology, and powerful engine, it's a car that's sure to turn heads on the road. Whether you're commuting in the city or embarking on a cross-country road trip, this sedan offers an unparalleled driving experience.",
            'current_bid': 150000,
            'category': 'Automotive',
            'image_url': "https://portfolio8aff35a6cba45be.blob.core.windows.net/djangoapp/tesla.png"



        }

    ]

    for item_data in data:
        Listing.objects.create(**item_data)

if __name__ == '__main__':
    etl()