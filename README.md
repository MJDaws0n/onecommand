# OneCommand

## How to use
Open the program and type your 1st command in. After that hit enter and enter your second command. Repeat that as many times as you like (well up to 1000 times). Then after you have entered all your desired commands type ]go[ to generate your command.

## Command not running
This is because you will have to use a button or place a block next to the command block and a redstone block above, then run the command. This is becasue the block above the commandblock is required to be powered.

## Supported versions
Although I have not tested in all version I know that it works in the latest version ans suppose that it works all the way down to minecraft 1.13

## Does it work for minecraft bedrock
Currently this program will only generate commands for minecraft java edition. Im not even sure where I would start for minecraft bedrock edition. Mainly becasue they don't have falling blocks.

## Fire burning out to fast
If you are having the issue of the fire burning out to fast, then it will be becasue your pressing the button to fast. If you need to press it fast then you can try lowering the number in the `age=[15]` section, right at the end of the command. If that still does not work replace the `fire[age=15]` to `lava[level=6]`. This will most likly make minecarts apear arround the command block. To kill all the minecarts then get a repeating command block and set it to always active. In the command put `kill @e[type=item,name=Minecart]`. Note this will kill all and any dropped Minecarts.

## Program crashing
Download and install python from [the offical site](https://python.org/download/) then download the soure code and unzip it. Then run CommandCreator.py. This will run the code directly through python

## Can I remake this
Sure. I would prefer credit, and also only like you to remake it if you change some things, but sure.
