from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def melon():
    """ returns the value of hte melon block """
    return 103

block = melon()
pos = mc.player.getTilePos()
mc.setBlock(pos.x, pos.y, pos.z, block)
