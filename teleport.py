from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 10
y = 120
z = 26

mc.player.setTilePos(x, y, z)
