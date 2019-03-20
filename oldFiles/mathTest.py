import mathClass

velocity00 = mathClass.Vec2D(10, 10)
# print(velocity00.getX())
velocity01 = mathClass.Vec2D(2, 2)

velocity00.addVec(velocity01)
# print(velocity00.getX())


playerPosition = mathClass.Vec2D(13, 13)
playerCollider = mathClass.Collider((3, 3), False, playerPosition)


# for x in range (1, 5):
#     playerCollider.update()
#     print(playerCollider.position.getX())

boxTestPosition = mathClass.Vec2D(13, 13)
boxTestCollider = mathClass.Collider((6,6), True, boxTestPosition)



colliderList = []
colliderList.append(playerCollider)
colliderList.append(boxTestCollider)

world = mathClass.worldSpace(9.8)


print("PLAYER Y PRIOR POS \n")
print(playerCollider.position.getY())
print("\n")
    
print("BOX Y PRIOR POS \n")
print(boxTestCollider.position.getY())


world.update(colliderList)
print("\n")
print("PLAYER Y END POS \n")
print(playerCollider.position.getY())
print("\n")
print("BOX Y POS")
print(boxTestCollider.position.getY())