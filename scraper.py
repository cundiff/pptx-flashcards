from pptx import Presentation

pA = Presentation('/Users/ian/Downloads/Study_Images__Set_A_.pptx')
pB = Presentation('/Users/ian/Downloads/Study_Images__Set_B_.pptx')
pC = Presentation('/Users/ian/Downloads/Study_Images__Set_C_.pptx')
pD = Presentation('/Users/ian/Downloads/Study_Images__Set_D_.pptx')
pE = Presentation('/Users/ian/Downloads/Study_Images__Set_E_.pptx')
pF = Presentation('/Users/ian/Downloads/Study_Images__Set_F_.pptx')
pG = Presentation('/Users/ian/Downloads/Study_Images__Set_G_.pptx')

for slide in pA.slides:
    print("Slide "+"index"+" notes: "+slide.notes_slide.notes_text_frame.text)
