from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

heights = [100, 0]
count = 0

while count < 60:
    pos = mc.player.getTilePos()

    if pos.y < heights[0]:
        y < 100
    elif pos.y > heights[1]:
        y > 0

    count += 1
    time.sleep(1)

mc.postToChat("Lowest: ") y > 0
mc.posttoChat("Highest: ") y < 100 
