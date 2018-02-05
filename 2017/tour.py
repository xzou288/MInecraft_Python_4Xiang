from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x = 10
y = 28
z = 30

mc.player.setTilePos(10, 28, 30)

time.sleep(10)

x = 20
y = 30
z = 80

mc.player.setTilePos(30, 40, 20)
