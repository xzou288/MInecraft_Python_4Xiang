from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = 10
y = 11
z = 12
answer = input("Yes")
gift = mc.getBlock(x, y, z)
if gift != 57:
mc.setBlocks(pos.x + 1, pos.y + 1, pos.z + 1, pos.x - 1, pos.y - 1, pos.z - 1) = blockType(0)
else:
    mc.postToChat("Place an offering on the pedestal.")
if answer:
    mc.setBlock(pos.x + 1, pos.y + 1, pos.z + 1) = blockType(57)

elif blockType >= 57:
     mc.setBlocks(pos.x + 1, pos.y + 1, pos.z + 1, pos.x - 1, pos.y - 1, pos.z - 1) = blockType(10)
