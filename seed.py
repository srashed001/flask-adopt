from models import db, Pet
from app import app 

db.drop_all()
db.create_all()


Pet.query.delete()

fluffy = Pet(name='Fluffy', species="dog", photo_url='https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Bulldog_adult_male.jpg/220px-Bulldog_adult_male.jpg', age=2, notes="needs a good home", available=True )
blue = Pet(name='Blue', species="dog", photo_url='http://cdn.shopify.com/s/files/1/0284/2391/3547/articles/American-Pitbull-Puppies-6.JPG_c4357295-9ee4-45f8-9718-e36c98022c46_1200x1200.jpg?v=1603063314', age=1, notes="very friendly", available=True )
jamie = Pet(name='Jamie', species="cat", photo_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCC4squwzXz2nJjoLg54HZI__bsl39JUc6NQ&usqp=CAU', age=1, notes="super smart", available=False )
oreo = Pet(name='Oreo', species="dog", photo_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvxmZRtFqxW08By7jk6_Dnn05wLdRP58P5gA&usqp=CAU', age=3, notes="very calm", available=True)


db.session.add_all([fluffy, blue, jamie, oreo])
db.session.commit()