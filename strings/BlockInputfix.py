from mcpi.minecraft import Minecraft
mc = Minecraft.create()
blockType = ()
pos = mc.player.getTilePos()

x = pos.x
y = pos.y
z = pos.z

try:
    blockType = int(input("Enter a block type: "))
    mc.setBlock(x, y, z, blockType)
except:
    mc.postToChat("you did not enter a number! Enter a number next time.")
  
