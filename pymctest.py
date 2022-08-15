from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

mc.postToChat("I am watching you!")

while True:
    x, y, z = mc.player.getTilePos()
    mc.postToChat("you are located to X:" + str(x) + ", Y:" + str(y) + ", Z:" + str(z))
    time.sleep(1)
    
    