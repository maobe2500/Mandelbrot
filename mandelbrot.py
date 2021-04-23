from PIL import Image, ImageDraw
import colorsys
import numpy as np 
Width = 200
Height = 200
Max_iter = 30

#Skalar ett värde från ett intervall till ett annat
def scale(value, old_min, old_max, new_min, new_max):
    old_range = (old_max - old_min)
    new_range = (new_max - new_min)
    new_value = (((value - old_min) * new_range) / old_range) + new_min
    return new_value

#Kollar om punkten (x, y) finns i mandelbrotmängden
#Om punktens absolutvärde blir över två ger den tillbaka antalet iterationer tills det hände
def mandelbrot(x, y, max_iter): 

    z = 0
    c = complex(x, y)
    for i in range(max_iter):
        z = z**2 + c
        if (abs(z) > 2):
            return i
    return max_iter

def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

def calc_color(iter):
    c = scale(iter, 0, Max_iter, 0, 1)
    angle = c * 10
    if (c == 1):
        return 0
    else:
        #rgb_tuple = hsv2rgb(angle, 90, 100)
        rgb_tuple = (round(255*c)*10, 0, 0)
        return (255,255,255)



pixels = Image.new("RGB", (Width, Height))
image = ImageDraw.Draw(pixels, "RGB")

for row_index in range(Width):
    for col_index in range(Height):

        scaled_x_val = scale(row_index, 0, Width, -2, 2)
        scaled_y_val = scale(col_index, 0, Height, -2, 2)
        iter = mandelbrot(scaled_x_val, scaled_y_val, Max_iter)
        rgb_tuple = calc_color(iter)
        image.point((row_index, col_index), fill=rgb_tuple)

    




pixels.save("Fractal.png")