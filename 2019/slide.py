from numpy import random

class Slide:
	"""A slide"""

	def __init__(self, photo1, photo2=None):
		self.photo1 = photo1
		self.photo2 = photo2

		self.tags = photo1.tags

		if photo2 is not None:
			self.tags.extend(photo2.tags)
			self.tags = list(set(self.tags))

	def __str__(self):
		return f'{self.photo1.id}\n' if self.photo2 is None else f'{self.photo1.id} {self.photo2.id}\n'

	@staticmethod
	def get_score(slide1, slide2):
		score1 = len(set(slide1.tags) & set(slide2.tags))
		score2 = len(set(slide1.tags)) - len(set(slide1.tags) & set(slide2.tags))
		score3 = len(set(slide2.tags)) - len(set(slide1.tags) & set(slide2.tags))
		return min(score1, score2, score3)

	@staticmethod
	def make_slideshow(slides):
		slideshow = []
		slide0 = slides.pop()
		slideshow.append(slide0)

		while len(slides) > 2:
			max_score = 0
			next_slide_index = 0

			for i1, s1 in enumerate(slides):
				score = Slide.get_score(slide0, s1)
				if score > max_score:
					max_score = score
					next_slide_index = i1

			slideshow.append(slides.pop(next_slide_index))
			slide0 = slideshow[-1]

		slideshow.append(slides.pop(0))

		return slideshow
