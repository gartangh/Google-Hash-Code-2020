from slide import Slide

def make_slideshow_sorted(slides):
        return bucketSort(slides)

# sort slides on amount of tags
def qsort(inlist):
    if inlist == []: 
        return []
    else:
        pivot = len(inlist[0].tags)
        lesser = qsort([x for x in inlist[1:] if len(x.tags) < pivot])
        greater = qsort([x for x in inlist[1:] if len(x.tags) >= pivot])
        return lesser + [pivot] + greater

def bucketSort(slides): 
    arr = [] 

    # find max amount of tags
    slot_num = 0
    for s in slides:
        n_tags = len(s.tags)
        if slot_num < n_tags:
            slot_num = n_tags
    
    for i in range(slot_num): 
        arr.append([]) 
          
    # Put array elements in different buckets  
    for s in slides:
        arr[len(s.tags)-1].append(s) 

    x = []
    # concatenate the result 
    #k = 0
    for i in range(slot_num): 
        if len(arr[i]) > 1:
            arr[i] = Slide.make_slideshow(arr[i])

        for j in range(len(arr[i])): 
            x.append(arr[i][j])
            #k += 1

    slideshow = x
    return slideshow





