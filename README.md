# Elec5616-ass2

## How to run buffer demo:
There is no need to compile savegame.c without a stack-protector for the buffer demo:
`gcc savegame.c -o savegame`

Then to run the buffer demo run:
`python$ver$ buffer_demo.py | ./savegame`

to find the location of the secret function

`gcc -g -fno-stack-protector savegame.c -o savegame`
`gdb ./savegame`
`break main`
`run`
`info address secret_function`
