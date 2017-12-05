from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 10
y = 11
z = 12
melon = 103
block = mc.getBlock(x, y, z)

noMelon = not a melon 

noMelon = 12
mc.postToChat("You will need to get some food: " + str(noMelon))

