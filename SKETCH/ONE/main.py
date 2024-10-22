from sketchpy import canvas
obj = canvas.sketch_from_image('ONE/muni.jpg')
obj.draw(threshold=60)