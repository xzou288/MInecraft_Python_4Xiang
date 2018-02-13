from mcpi.minecraft import Minecraft
mc = Minecraft.create()

oneDimensionslRainbowList = [0, 1, 2, 3, 4, 5]

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

for color in oneDimensionslRainbowList:
    mc.setBlock(x, y, z, 35, color)
    y += 1 z
