
import sys
import os

# os.environ['DJANGO_SETTINGS_MODULE'] = 'project_2.settings'

project_root = os.path.abspath(os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '..'))

sys.path.insert(0, project_root)



from auctions.models import Listing


def etl():
    data = [
        {
            'title': 'Toyota Corolla',
            'description': 'Toyota Corolla 2014 80,000 miles',
            'current_bid': 14000 ,
            'image_url': "https://portfolio8aff35a6cba45be.blob.core.windows.net/djangoapp/corolla.png",
        },
        {
            'title': 'Porsche',
            'description': 'Porsche 911 Like NEW!',
            'current_bid': 80000,
            'image_url': "https://portfolio8aff35a6cba45be.blob.core.windows.net/djangoapp/porsche.png"
        },
        {
            'title': 'Subaru',
            'description': '1 out of 40',
            'current_bid': 140000,
            'image_url': "https://portfolio8aff35a6cba45be.blob.core.windows.net/djangoapp/subaru.png"
        },
        {
            'title': 'Tesla',
            'description': 'Tesla Model 3 - You will never go back to gas',
            'current_bid': 80000,
            'image_url': "https://portfolio8aff35a6cba45be.blob.core.windows.net/djangoapp/tesla.png"
        }
    ]

    for item_data in data:
        Listing.objects.create(**item_data)

if __name__ == '__main__':
    etl()