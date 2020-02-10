from slide import Slide


def to_slide(photos):
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
    while len(photos) > 1:
        print(len(photos), end="\r", flush=True)
        # look for an "ok" combination of pictures
        photo = photos[0]
        max_tags = len(photo.tags)
        other = 0

        for i in range(1, len(photos)):
            num_tags = calc_tags(photo, photos[i])
            if num_tags > max_tags:
                max_tags = num_tags
                other = i

        if other is not 0:
            # if 0 not useful
            slides.append(Slide(photo, photos[other]))
            photos.pop(other)
            photos.pop(0)  
    # print number of unused pictures
    print(len(photos))
    return slides


def calc_tags(photo1, photo2):
    combined_tags = list(set().union(photo1.tags, photo2.tags))
    return len(combined_tags)
