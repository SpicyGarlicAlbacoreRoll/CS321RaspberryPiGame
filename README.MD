Welcome! This is the group project repo for our CS321 Operating Systems course,

The intent of the project is to make a simple game for the Raspberry Pi that takes GPIO pins for input.

The actual content of this game is yet to be determined, but we hope to make it an
interesting experience.

Given the very specific nature of this game's inputs, we can't confirm that this will work for any particular setup
besides our own.


GENERAL CODE STRUCTURE AND LOGIC:

-"testFile.py" is the file that calls most of the code

-Pygame handles the actual drawing of images and listening for inputs

-The gameObject class and its subclasses are in development, and track useful gameobject info
    -Current subclasses: Player
    -Pending subclasses: Environment, Pickups

-Each gameObject has a collider which determines collisions based on position relative to 
    every other gameobject collider.