from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

score = 0

pos = mc.player.getPos()
blockAbove = mc.getBlock(pos.x, pos.y + 2, pos.z)

count = 0
while count < 200:
    print(count)
    count += 1
    blockAbove == 8
    time.sleep(1)
pos = mc.player.getPos()
blockAbove = mc.getBlock(pos.x, pos.y + 2, pos.z)
score = score + 1
mc.postToChat("Current score: " + str(score))

mc.postToChat("Final score: " + str(score))

if score > 6:
    finalPos = mc.player.getTilePos()
    mc.setBlocks(finalPos.x -5, finalPos.y + 10, finalPos.z - 5,
                 finalPos.x +5, finalPos.y + 10, finalPos.z + 5 , 38)
    
