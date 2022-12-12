def classPhotos(redShirtHeights, blueShirtHeights):
    back_row = None
    front_row = None

    if sum(blueShirtHeights) > sum(redShirtHeights):
        back_row = sorted(blueShirtHeights)
        front_row = sorted(redShirtHeights)
    elif sum(blueShirtHeights) < sum(redShirtHeights):
        back_row = sorted(redShirtHeights)
        front_row = sorted(blueShirtHeights)
    else:
        return False

    for student in range(len(back_row)):
        if back_row[student] <= front_row[student]:
            return False
    return True


redShirtHeights = [5, 8, 1, 3, 4]
blueShirtHeights = [6, 9, 2, 4, 5]
print(classPhotos(redShirtHeights, blueShirtHeights))
