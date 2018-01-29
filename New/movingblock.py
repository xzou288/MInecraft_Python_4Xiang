from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

def calculateMove():
    """ Changes the x and z variable blah blah blah blah blah blah """
    melons = 103
    global melons
    currentHeight =  mc.getHeight(x, z) -1

    forwardHeight = mc.getHeight(x + a, z)
    rightheight = mc.getHeight(x, z + 1)
    backwardHeight = mc.Height(x - 1,z)
    leftHeight = mc.getHeight(x, z - 1)
    if forwardheight - cirrentHeight < 3:
        x += 1
    
