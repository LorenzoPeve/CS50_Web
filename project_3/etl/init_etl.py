from datetime import datetime, timezone, timedelta
import django
import os
import sys


# Required for models to load
project_root =os.path.abspath(os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '..', 'mail'))
sys.path.insert(0, project_root)

os.environ['DJANGO_SETTINGS_MODULE'] = 'project3.settings'
django.setup()

EST = timezone(timedelta(hours=-5)) # US Eastern Time UTC-5

from mail.models import User, Email


admin = User.objects.create_superuser('admin', 'admin@example.com', '123')
user1 = User.objects.create_user(
    username="user1@example.com",
    email="user1@example.com",
    password="oXhqNLvLvF9gGfP3JYWg")
user1.save()

user2 = User.objects.create_user(
    username="user2@example.com",
    email="user2@example.com",
    password="DUmUPiMUwnF2rrhj4crh")
user2.save()

user3 = User.objects.create_user(
    username="user3@example.com",
    email="user3@example.com",
    password="Jgt4hFDdr8PiCmgZM8yD")
user3.save()

user4 = User.objects.create_user(
    username="user4@example.com",
    email="user4@example.com",
    password="yLTVxT2p4myb69vAAZ7k")
user4.save()


# Conversation between user 2 and 1 about US Open tennis tournament
# User 2 to User 1
email = Email.objects.create(**{
        "user": user2,
        "sender": user2,
        "subject": "US Open Tickets",
        "body": "Hi, I have extra US Open tickets. Are you interested?",
        "timestamp": datetime(2023, 9, 1, 13, 14, 37, tzinfo=EST),
        "read": True,
        "archived": False,
})
email.recipients.set([user1])

# User 1's response
email = Email.objects.create(**{
        "user": user1,
        "sender": user1,
        "subject": "Re: US Open Tickets",
        "body": "Yes, I'm interested. How much are you selling them for?",
        "timestamp": datetime(2023, 9, 1, 14, 13, 37, tzinfo=EST),
        "read": True,
        "archived": False,
})
email.recipients.set([user2])

# User 2's response
email = Email.objects.create(**{
        "user": user2,
        "sender": user2,
        "subject": "Re: US Open Tickets",
        "body": "Could you please specify which type of tickets you're interested in (e.g., single day, multi-day, or VIP passes)? Additionally, it would be helpful to know the number of tickets you are looking to purchase.",
        "timestamp": datetime(2023, 9, 1, 14, 14, 21, tzinfo=EST),
        "read": False,
        "archived": False,
})
email.recipients.set([user1])

# User 1's response
email = Email.objects.create(**{
        "user": user1,
        "sender": user1,
        "subject": "Re: US Open Tickets",
        "body": "I am interested in purchasing two single-day tickets for the US Open. Could you please provide me with the pricing details and the available dates for these tickets? ",
        "timestamp": datetime(2023, 9, 1, 14, 15, 37, tzinfo=EST),
        "read": False,
        "archived": False,
})
email.recipients.set([user2])


# Conversation between user 2 and 1 about US Open tennis tournament
email = Email.objects.create(**{
        "user": user1,
        "sender": user1,
        "subject": "Looking for a Car",
        "body": "Hi, I'm in the market for a new car. Do you have any recommendations or know of any good deals going on right now?Thanks!",
        "timestamp": datetime(2023, 6, 1, 14, 7, 7, tzinfo=EST),
        "read": True,
        "archived": False,
})

email.recipients.set([user3])

email = Email.objects.create(**{
        "user": user3,
        "sender": user3,
        "subject": "Re: Looking for a Car",
        "body": """I'd be happy to help you find the right car! To narrow down
some options, could you please provide me with more details about your preferences?
Are you looking for a specific make or model? Do you have a budget in mind, or
any specific features you want in the car? Let me know, and I'll do my best to assist you.
""",
        "timestamp": datetime(2023, 6, 1, 14, 7, 37, tzinfo=EST),
        "read": True,
        "archived": False,
})

email.recipients.set([user1])

email = Email.objects.create(**{
        "user": user1,
        "sender": user1,
        "subject": "Re: Looking for a Car",
        "body": """
I'm open to different makes and models, but I'm looking for a reliable and
fuel-efficient sedan. My budget is around $20,000. I'd prefer a car with low
mileage if possible. Do you have any suggestions in that price range?
""",
        "timestamp": datetime(2023, 6, 1, 14, 8, 7, tzinfo=EST),
        "read": True,
        "archived": False,
})

email.recipients.set([user3])

email = Email.objects.create(**{
        "user": user3,
        "sender": user3,
        "subject": "Re: Looking for a Car",
        "body": """
With a budget of $20,000, you have several good options for reliable and
fuel-efficient sedans. I recommend considering models like the Toyota Corolla,
Honda Civic, or the Hyundai Elantra. These cars are known for their
affordability, low maintenance costs, and excellent fuel efficiency.
""",
        "timestamp": datetime(2023, 6, 1, 14, 9, 25, tzinfo=EST),
        "read": True,
        "archived": False,
})

email.recipients.set([user1])