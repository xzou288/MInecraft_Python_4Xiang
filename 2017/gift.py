from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -16
y = 4
z = -17
gift = mc.getBlock(x, y, z)
diamond = 57
sapling = 6

if gift == diamond:
    mc.postToChat("thanks for the diamond")
elif gift == sapling:
    mc.postToChat("I guess tree sapling is as good as diamonds")
else:
    mc.postToChat("Bring gift to " + str(x) + "," + str(y) + "," + str(z))
