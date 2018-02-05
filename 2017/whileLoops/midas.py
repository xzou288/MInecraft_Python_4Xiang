from mcpi.minecraft import Minecraft
mc = Minecraft.create()

air = 0
water = 9

while True:
    pos = mc.player.getPos()
    mc.setBlock(pos.x, pos.y, pos.z, 41)
    
