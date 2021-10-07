#Brandon Camacho
#Minecraft Code Example

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

mc.postToChat('hello')
coordinates = mc.player.getTilePos()
mc.postToChat(coordinates)