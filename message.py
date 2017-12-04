Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> from mcpi.minecraft import Minecraft
>>> mc = Minecraft.create()
>>> mc.postToChat("Hello Minecraft World")
>>> 
input("What is your name?")
What is your name?
============= RESTART: /home/pi/Minecraft_Python_Repo/Message.py =============
>>> input("what is your name?")
what is your name?
>>> craig
''
>>> craig
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    craig
NameError: name 'craig' is not defined
>>> 'craig'
'craig'
>>> name = input("What is your name?")
What is your name?
>>> 'craig'
'craig'
>>> 
