#Brandon Camacho
#Minecraft Demo_PlaceBlock

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    pos = mc.player.getPos()
    mc.setBlock(pos.x, pos.y - 1, pos.z,  11)