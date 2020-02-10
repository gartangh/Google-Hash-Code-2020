from slide import Slide
from numpy import random


def to_slide_random(photos):
    # array containing slides
    slides = []

    # go through all horizontal pictures
    i = 0
    print("Sorting horizontal pictures...")
    while i < len(photos):
        if photos[i].orientation is 'H':
            # horizontal pictures are the same as a slide
            slides.append(Slide(photos[i]))
            photos.pop(i)
            # one index back so you end up in the next place
            i-=1
        i+=1

    # find matches for vertical pictures
    print("Matching vertical pictures to slides...")
    while len(photos)>2:
        print(len(photos), end="\r", flush=True)
        # look for a random combination of pictures
        photo = photos[0]
        other = random.randint(1, len(photos)-1)

        if other is not 0:
            # if 0 not usefull
            slides.append(Slide(photo,photos[other]))
            photos.pop(other)
            photos.pop(0)  
    # print number of unused pictures
    print(len(photos))
    return slides
