from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

pos = mc.player.getTilePos()
floorX = pos.x - 2
floorY = pos.y - 1
floorZ = pos.z - 2
width = 20
length = 20
block = 22
mc.setBlocks(floorX, floorY, floorZ,
             floorX + width, floorY, floorZ + length, block)

while floorX <= pos.x <= floorX + width and floorZ <= pos.z <= floorZ + length:
    if block == 22:
        block = 35
    else: block = 22

    mc.setBlocks(floorX, floorY, floorZ,
                 floorX + width, floorY, floorZ + length, block)
    pos = mc.player.getTilePos()
    time.sleep(0.5)
