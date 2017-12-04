Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import time
>>> from mcpi.minecraft import Minecraft
>>> mc = Minecraft.create()
>>> 
>>> pos1 =mc.player.getTilePos()
>>> x1 = pos1.x
>>> y1 = pos1.x
>>> z1 = pos1.z
>>> y1 = pos1.y
>>> time.sleep(10)

pos2.
>>> pos.2 = mc.player.getTilePos()
SyntaxError: invalid syntax
>>> pos2 = mc.player.getTilePos()
>>> x2 = pos2.x
>>> y2 = pos2.y
>>> z2 = pos3.z
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    z2 = pos3.z
NameError: name 'pos3' is not defined
>>> z2 = pos2.z
>>> xDistance = x2 - x1
>>> yDistance = y2 - y1
>>> zDistance = z2 - z1
>>> mc.postToChat("results")
>>> mc.postToCha("The player has moved + xDistance + yDistance + zDistance")
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    mc.postToCha("The player has moved + xDistance + yDistance + zDistance")
AttributeError: 'Minecraft' object has no attribute 'postToCha'
>>> mc.postToChat("The player has moved + xDistance + yDistance + zDistance")
>>> 
