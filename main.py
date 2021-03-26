import pyqrcode, png, time, image
from PIL import Image, ImageDraw
from switch import Switch


#pip install pillow 
#pip install switch
#pip install PyQRCode 


def create(name:str, url : str, farbe1:str, farbe2: str):
  if farbe1.lowcase() == farbe2.lowcase():
   print("err")
  with Switch(farbe1) as case:
    if case.match(r'rot|Rot'):
      farbe1 = 255,0,0
    if case.match(r'grün|Grün'):
      farbe1 = 124,252,0
    if case.match(r'blau|Blau'):
      farbe1 = 30,144,255
    if case.default:
      print("err")
      
  with Switch(farbe2) as case:
    if case.match(r'rot|Rot'):
      farbe2 = 255,0,0
    if case.match(r'grün|Grün'):
      farbe2 = 124,252,0
    if case.match(r'blau|Blau'):
      farbe2 = 30,144,255
    if case.default:
      print("err")
  url = pyqrcode.create(eingabe, error='H')
  url.png("qrcodes/" + name + ".png", module_color=(farbe1), background=(farbe2), scale=(10))
  print("Der QRCode wird erstellt......")
  print("Der QRCode wurde in dem Ordner >> qrcodes << erstellt \r\n" +
      "Wenn da kein Ordner namens >> qrcodes << vorhanden ist \r\n" +
      "bitte erstelle ihn sonst kommt ein Error!")

  myImage = Image.open("qrcodes/" + name + ".png");
  myImage.show();

  time.sleep(10)

print("Gib bitte den Namen für den QRcode an!")
name = input("name>>")

print("Gib bitte einen Link an der zu einem QRCode umgewandelt werden soll!")
eingabe = input("url>>")

print("Jetzt farbe 1! Mögliche eingaben = grün, blau, rot")
farbe1 = input("farbe1>>")

print("Jetzt farbe 2!")
farbe2 = input("farbe2>>")


create(name, eingabe, farbe1, farbe2)