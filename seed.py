from model import Pet, db
from app import app


db.drop_all()
db.create_all()




seven = Pet(name = '7', species = 'dog', photo_url = 'https://i.pinimg.com/originals/f2/c0/95/f2c0953dce811407addafd4db154185d.jpg', age = 2, notes = "Kind friendly and loveable", available = True )
daemon = Pet(name = "Daemon" , species = "dog", photo_url = "https://dogtime.com/wp-content/uploads/sites/12/gallery/labradoodle-dog-breed-pictures/side-1.jpg", age = 1, notes = "Siper friendly, protective, active", available = True)
thirteen = Pet(name = "13", species = "cat", photo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbs9zDZJW0IOjcqIQImPm4PRdKcjn9blwyIA&usqp=CAU", age = 4,  available = False )
blue = Pet(name = "blue", species = "porcupine", photo_url = "", age = 6, notes = "Dangerous!!!! PLEASE EXPRIENCED REQUIRED" , available = True )
twist = Pet(name = "twist" , species = "cat" , photo_url = "https://img1.wsimg.com/isteam/ip/8ab7d45d-02bb-4554-99d0-4e4ce06f0d39/cat.jpg/:/cr=t:0%25,l:0%25,w:100%25,h:100%25" , age = 11, notes = "Playful" )
grayson = Pet(name = "grayson", species = "porcupine", photo_url = "https://blog.allpetsmedical.com/wp-content/uploads/2018/10/monkey-2139295_960_720.jpg", age = 2, available = False )

db.session.add_all([seven, daemon, thirteen, blue, twist, grayson])
db.session.commit()