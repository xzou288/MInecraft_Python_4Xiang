Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> from mcpi.minecraft import Minecraft
>>> mc = Minecraft.create()
>>> message = "Blah blah blah"
>>> mc.postToChat(message)
>>> firstName = "Alex"
>>> lastName = "Kary"
>>> print(firstName + lastName)
Alex Kary
>>> print(firstName + " " + lastName)
Alex Kary
>>> print(firstName, lastName)
Alex Kary
>>> print(firstName, lastName)
Alex Kary
>>> print("His name is " + firstName + " " + lastName)
His name is Alex Kary
>>> print("My not-soo-secret golden apple stash: " + str(myGoldenApples))
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print("My not-soo-secret golden apple stash: " + str(myGoldenApples))
NameError: name 'myGoldenApples' is not defined
>>> myGoldenApples = 1
>>> print ("My not so-secret golden apple stash: " + str(myGoldenApples))
My not so-secret golden apple stash: 1
>>> print(str(19) + str(84))
1984
>>> print("The year is " + str(19) + str(84))
The year is 1984
>>> message = input("dab: ")
dab: mc.postToChat(;oish;ihar)
>>> mc.postToChat(;ldrg;lsg)
SyntaxError: invalid syntax
>>> cansOftunaPerCat = 4
>>> cats = input("How many cats do you have? ")
How many cats do you have? cats = int(cats)
>>> dailyTunaEaten = cats * cansOfTunaPerCat
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    dailyTunaEaten = cats * cansOfTunaPerCat
NameError: name 'cansOfTunaPerCat' is not defined
>>> cansOfTunaPerCat = 4
>>> dailyTunaEaten = cats * cansOfTunePerCat
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    dailyTunaEaten = cats * cansOfTunePerCat
NameError: name 'cansOfTunePerCat' is not defined
>>> dailyTunaEaten = cats * cansOfTunaPerCat
>>> 
