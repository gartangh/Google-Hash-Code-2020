# imports
from photo import Photo
from slide import Slide
# from to_slide import to_slide
from to_slide_greedy import to_slide_greedy
# from to_slide_random import to_slide_random
from to_slideshow_sorted import make_slideshow_sorted

# main
if __name__ == '__main__':
	# initialization
	file_names = ['a_example', 'b_lovely_landscapes', 'c_memorable_moments', 'd_pet_pictures', 'e_shiny_selfies']
	file_index = 3
	photos = []

	print('Reading Photos ...')
	with open('in/{}.txt'.format(file_names[file_index])) as file_in:
		for i in range(int(file_in.readline().split()[0])):
			line = file_in.readline().split()
			tags = line[-int(line[1]):]
			photos.append(Photo(i, line[0], tags))
	print('Photos read')

	all_tags = []
	for photo in photos:
		all_tags.extend(photo.tags)
	print(len(all_tags), len(set(all_tags)))

	print('to_slide ...')
	slides = to_slide_greedy(photos)
	print('to_slide')

	print('Making slideshow ...')
	#slideshow = Slide.make_slideshow(slides)
	slideshow = make_slideshow_sorted(slides)
	print('Slideshow made')

	print('Writing output ...')
	with open('out/{}.txt'.format(file_names[file_index]), 'w') as file_out:
		file_out.write(f'{len(slideshow)}\n')
		for slide in slideshow:
			file_out.write(str(slide))

	print('Output written')
