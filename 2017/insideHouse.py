from mcpi.minecraft import Minecraft
mc = Minecraft.create()

buildX = 1
buildY = 2
buildZ = 3
width = 10
height = 5
length = 6

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

inside = buildX < x < buildX + width and 1
