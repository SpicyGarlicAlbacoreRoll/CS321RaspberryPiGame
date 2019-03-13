import mathClass

velocity00 = mathClass.Vec2D(10, 10)
# print(velocity00.getX())
velocity01 = mathClass.Vec2D(2, 2)

velocity00.addVec(velocity01)
# print(velocity00.getX())


playerPosition = mathClass.Vec2D(14, 14)
playerCollider = mathClass.Collider((2, 2), False, playerPosition)


# for x in range (1, 5):
#     playerCollider.update()
#     print(playerCollider.position.getX())

boxTestPosition = mathClass.Vec2D(13, 13)
boxTestCollider = mathClass.Collider((5,5), True, boxTestPosition)



colliderList = []
colliderList.append(playerCollider)
colliderList.append(boxTestCollider)

world = mathClass.worldSpace(9.8)


print("PLAYER X PRIOR POS \n")
print(playerCollider.position.getX())
print("\n")
    
print("BOX X PRIOR POS \n")
print(boxTestCollider.position.getX())


world.update(colliderList)
print("\n")
print("PLAYER X END POS \n")
print(playerCollider.position.getX())
print("\n")
print("BOX X POS")
print(boxTestCollider.position.getX())