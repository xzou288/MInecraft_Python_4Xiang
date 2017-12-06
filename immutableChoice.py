from mcpi.minecraft import Minecraft
mc = Minecraft.create()
Name = "Y"
answer = input("Do you want blocks to be immutable? Y/N: ")
if answer == Name:
    mc.setting("world_immutable", True)
    mc.postToChat("World is immutable")
else:
    mc.setting("world_immutable", False)
    mc.postToChat("World isn't immutable")
    
