from slide import Slide


def to_slide_greedy(photos):
    # define target nuber of tags per slide
    number_pics = len(photos)
    number_tags = 0
    for photo in photos:
        number_tags += len(photo.tags)

    # array containing slides
    slides = []

    # only vertical should remain
    slides, photos = get_horizontal(slides, photos)

    # sort photos by number of tags
    photos = bucketSort(photos)

    while len(photos)>1:
        photo = photos[len(photos)-1]
        photos.pop(len(photos)-1)
        
        max_tags = len(photo.tags)
        other = len(photos)-2

        for i in range(len(photos)-100, len(photos)-1):
            if i>=0:
                num_tags = calc_tags(photo, photos[i])
                if num_tags > max_tags:
                    max_tags = num_tags
                    other = i

        slides.append(Slide(photo, photos[other]))
        photos.pop(other)

    return slides

def get_horizontal(slides, photos):
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
    
    return slides, photos

def bucketSort(photos): 
    arr = [] 

    # find max amount of tags
    slot_num = 0
    for s in photos:
    	n_tags = len(s.tags)
    	if slot_num < n_tags:
    		slot_num = n_tags
    
    for i in range(slot_num): 
        arr.append([]) 
          
    # Put array elements in different buckets  
    for s in photos:
        arr[len(s.tags)-1].append(s) 
    
    x = []
    # concatenate the result 
    k = 0
    for i in range(slot_num): 
        for j in range(len(arr[i])): 
            x.append(arr[i][j])
            k += 1
    return x 



def calc_tags(photo1, photo2):
    combined_tags = list(set().union(photo1.tags, photo2.tags))
    return len(combined_tags)