#Brandon Camacho
#Minecraft Demo_GetPosition

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
coordinates = mc.player.getTilePos()
mc.postToChat(coordinates)