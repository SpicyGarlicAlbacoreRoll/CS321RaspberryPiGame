import mathClass

velocity00 = mathClass.Vec2D(10, 10)
# print(velocity00.getX())
velocity01 = mathClass.Vec2D(2, 2)

velocity00.addVec(velocity01)
# print(velocity00.getX())


playerPosition = mathClass.Vec2D(5, 5)
playerCollider = mathClass.Collider((2, 2), False, playerPosition)


for x in range (1, 5):
    playerCollider.update()
    print(playerCollider.position.getX())