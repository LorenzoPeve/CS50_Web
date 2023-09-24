from datetime import datetime
import django
import os
import sys

# Required for models to load
project_root = os.path.abspath(os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '..', 'network'))

sys.path.insert(0, project_root)

os.environ['DJANGO_SETTINGS_MODULE'] = 'project4.settings'
django.setup()


from network.models import User, Post, Following
from network.models import EST

admin = User.objects.create_superuser('admin', 'admin@example.com', '123')
user1 = User.objects.create_user(
    first_name='Carlos',
    last_name='Sainz',
    username="SmoothOperator",
    email="user1@example.com",
    password="123")
user1.save()
  
user2 = User.objects.create_user(
    first_name='Conor',
    last_name='Mcgregor',
    username="TheNotoriousMMA",
    email="cm@example.com",
    password="123")
user2.save()

user3 = User.objects.create_user(
    first_name='Alex',
    last_name='Pereira',
    username="PoatanMMA",
    email="ap@example.com",
    password="123")
user3.save()

user4 = User.objects.create_user(
    first_name='Novak',
    last_name='Djokovic',
    username="NoleTennis",
    email="nd@example.com",
    password="123")
user4.save()

p1 = Post(
    user=user1,
    content="""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi feugiat ultricies
metus at dignissim. Aliquam tincidunt, elit at scelerisque lacinia, mi libero
ornare libero, sit amet dictum libero nunc suscipit tellus. Phasellus hendrerit,
elit et blandit ullamcorper, tellus est tincidunt sem, quis laoreet erat felis
nec turpis. 
""",
    created_at=datetime(2023, 9, 9, 1, 14, 15, tzinfo=EST),
    updated_at=datetime(2023, 9, 9, 1, 14, 15, tzinfo=EST),
)
p1.save()

p2 = Post(
    user=user1,
    content="""Ut sed tellus sed lorem congue mollis.""",
    created_at=datetime(2023, 9, 12, 0, 28, 40, tzinfo=EST),
    updated_at=datetime(2023, 9, 12, 0, 28, 40, tzinfo=EST),
)
p2.save()

p3 = Post(
    user=user1,
    content="""
Interdum et malesuada fames ac ante ipsum primis in faucibus. Etiam mollis
tortor elit, tincidunt venenatis neque viverra scelerisque
""",
    created_at=datetime(2023, 9, 19, 2, 19, 26, tzinfo=EST),
    updated_at=datetime(2023, 9, 19, 2, 19, 26, tzinfo=EST),
)
p3.save()

p4 = Post(
    user=user2,
    content="""
Etiam tempor sem eget tortor fermentum blandit. Nullam neque risus, convallis
a quam sit amet, hendrerit sollicitudin magna.
""",
    created_at=datetime(2023, 9, 1, 14, 2, 50, tzinfo=EST),
    updated_at=datetime(2023, 9, 1, 14, 2, 50, tzinfo=EST),
)
p4.save()

p5 = Post(
    user=user2,
    content="""
Mauris venenatis ipsum quis libero hendrerit, nec molestie enim consectetur.
Suspendisse et risus eget dui pretium tincidunt.
""",
    created_at=datetime(2023, 9, 7, 3, 13, 42, tzinfo=EST),
    updated_at=datetime(2023, 9, 7, 3, 13, 42, tzinfo=EST),
)
p5.save()

p6 = Post(
    user=user2,
    content="""
Etiam condimentum nunc neque, id finibus magna dapibus sed.
""",
    created_at=datetime(2023, 9, 20, 21, 10, 3, tzinfo=EST),
    updated_at=datetime(2023, 9, 20, 21, 10, 3, tzinfo=EST),
)
p6.save()

p7 = Post(
    user=user2,
    content="""
Sed nec maximus urna
""",
    created_at=datetime(2023, 9, 3, 16, 25, 50, tzinfo=EST),
    updated_at=datetime(2023, 9, 3, 16, 25, 50, tzinfo=EST),
)
p7.save()

p8 = Post(
    user=user3,
    content="""
Aenean sit amet tellus nec ex consectetur maximus.
""",
    created_at=datetime(2023, 9, 9, 7, 20, 20, tzinfo=EST),
    updated_at=datetime(2023, 9, 9, 7, 20, 20, tzinfo=EST),
)
p8.save()

p9 = Post(
    user=user3,
    content="""
Dianzi laggiu lascia storia eccolo riposi pel all. Consunta oh piramide no
dovresti lucidita proseguo tremante.
""",
    created_at=datetime(2023, 9, 6, 19, 26, 14, tzinfo=EST),
    updated_at=datetime(2023, 9, 6, 19, 26, 14, tzinfo=EST),
)
p9.save()

p10 = Post(
    user=user3,
    content="""
I love espressos!!!
""",
    created_at=datetime(2023, 9, 17, 18, 0, 30, tzinfo=EST),
    updated_at=datetime(2023, 9, 17, 18, 0, 30, tzinfo=EST),
)

p10.save()

p11 = Post(
    user=user1,
    content="""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi feugiat ultricies
metus at dignissim. Aliquam tincidunt, elit at scelerisque lacinia, mi libero
ornare libero, sit amet dictum libero nunc suscipit tellus. Phasellus hendrerit,
elit et blandit ullamcorper, tellus est tincidunt sem, quis laoreet erat felis
nec turpis. 
""",
    created_at=datetime(2023, 6, 6, 1, 14, 15, tzinfo=EST),
    updated_at=datetime(2023, 6, 6, 1, 14, 15, tzinfo=EST),
)
p11.save()

p12 = Post(
    user=user1,
    content="""Ut sed tellus sed lorem congue mollis.""",
    created_at=datetime(2023, 6, 12, 0, 28, 40, tzinfo=EST),
    updated_at=datetime(2023, 6, 12, 0, 28, 40, tzinfo=EST),
)
p12.save()

p13 = Post(
    user=user1,
    content="""
Interdum et malesuada fames ac ante ipsum primis in faucibus. Etiam mollis
tortor elit, tincidunt venenatis neque viverra scelerisque
""",
    created_at=datetime(2023, 6, 16, 2, 16, 26, tzinfo=EST),
    updated_at=datetime(2023, 6, 16, 2, 16, 26, tzinfo=EST),
)
p13.save()

p14 = Post(
    user=user2,
    content="""
Etiam tempor sem eget tortor fermentum blandit. Nullam neque risus, convallis
a quam sit amet, hendrerit sollicitudin magna.
""",
    created_at=datetime(2023, 6, 1, 14, 2, 50, tzinfo=EST),
    updated_at=datetime(2023, 6, 1, 14, 2, 50, tzinfo=EST),
)
p14.save()

p15 = Post(
    user=user2,
    content="""
Mauris venenatis ipsum quis libero hendrerit, nec molestie enim consectetur.
Suspendisse et risus eget dui pretium tincidunt.
""",
    created_at=datetime(2023, 6, 7, 3, 13, 42, tzinfo=EST),
    updated_at=datetime(2023, 6, 7, 3, 13, 42, tzinfo=EST),
)
p15.save()

p16 = Post(
    user=user2,
    content="""
Etiam condimentum nunc neque, id finibus magna dapibus sed.
""",
    created_at=datetime(2023, 6, 20, 21, 10, 3, tzinfo=EST),
    updated_at=datetime(2023, 6, 20, 21, 10, 3, tzinfo=EST),
)
p16.save()

p17 = Post(
    user=user2,
    content="""
Sed nec maximus urna
""",
    created_at=datetime(2023, 6, 3, 16, 25, 50, tzinfo=EST),
    updated_at=datetime(2023, 6, 3, 16, 25, 50, tzinfo=EST),
)
p17.save()

p18 = Post(
    user=user3,
    content="""
Aenean sit amet tellus nec ex consectetur maximus.
""",
    created_at=datetime(2023, 6, 6, 7, 20, 20, tzinfo=EST),
    updated_at=datetime(2023, 6, 6, 7, 20, 20, tzinfo=EST),
)
p18.save()

p19 = Post(
    user=user3,
    content="""
Dianzi laggiu lascia storia eccolo riposi pel all. Consunta oh piramide no
dovresti lucidita proseguo tremante.
""",
    created_at=datetime(2023, 6, 6, 16, 26, 14, tzinfo=EST),
    updated_at=datetime(2023, 6, 6, 16, 26, 14, tzinfo=EST),
)
p19.save()

p20 = Post(
    user=user3,
    content="""
I love espressos!!!
""",
    created_at=datetime(2023, 6, 17, 18, 0, 30, tzinfo=EST),
    updated_at=datetime(2023, 6, 17, 18, 0, 30, tzinfo=EST),
)

p20.save()

p21 = Post(
    user=user3,
    content="""
Dianzi laggiu lascia storia eccolo riposi pel all. Consunta oh piramide no
dovresti lucidita proseguo tremante.
""",
    created_at=datetime(2023, 4, 6, 16, 26, 14, tzinfo=EST),
    updated_at=datetime(2023, 4, 6, 16, 26, 14, tzinfo=EST),
)
p21.save()

# Create a follower relationship
follower = Following(user=user1, follows=user2)
follower.save()

follower = Following(user=user1, follows=user3)
follower.save()

follower = Following(user=user1, follows=user4)
follower.save()

follower = Following(user=user2, follows=user4)
follower.save()