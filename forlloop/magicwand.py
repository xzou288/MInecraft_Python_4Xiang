from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time
x = 0
y = 1
z = 0
hits = mc.events.pollBlockHits()
Block = 103

for hit in hits:
x, y, z = hit.pos.x, hit.pos.y, hit.pos.z
mc.setBlockPos(x, y, z)
