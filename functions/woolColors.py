from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def getWoolState(color):
    """ Take color as a string and returns the wool block state for that color """
    if color == "pink":
        blockState = 6

    elif color == "blue":
        blockState = 11

colorString = input("Enter a block color: ")
state = getWoolState(colorString)

pos = mc.player.getTilePos()
mc.setBlock(pos.x, pos.y, pos.z, 35, state)
