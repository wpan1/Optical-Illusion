###############################################################################
# COMP10001 Project 2  
# Author - William Pan 694945  
# Date - 11/05/2014   
#
# Skeleton code for COMP10001 Proj 2 S1/2014
# Provided by Andrew Turpin and Tim Baldwin
# Date: 17/4/2014
###############################################################################

import Image


TEST_REPORT = "testReport.html"
CAFE_FILE = "cafe.png"
THREE_IN_ONE_FILE = "3in1.png"


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)


###############################################################################
def draw_square(image, (x, y), r, colour):
    """
    Draw a square with top left at (x,y) and side length r
    Assumes top-left of image is (0,0)
    Only draws the portion of the square that is in the image.
    INPUTS:
      image - an Image object
      x, y  - coordinates of top left corner 
      r     - side length
      colour - [R,G,B] list
    
    Sets max_x, max_y, x and y as variables outside the while loop
    This makes sure that max_x and max_y are not changed, when x/y is changed
    
    Function iterates over x values (x_val) and y values (y_val) to draw
    seperate lines horizontally. If x or y values are found to be outside the
    width/length of image. The starting points or ending points are set to
    either 0 (start of image) or width/height (end of image).
    
    Due to range function not including the last value, height and width does
    not need to be changed.
    
    No else is needed as all inputs of x,y,max_y and max_x are accounted for.
    
    RETURNS: nothing
    """

    assert not image == None
    width, height = image.size
    pixels = image.load()
    
    max_x = x + r
    max_y = y + r
    x = x
    y = y
    
    while True:
        try:
            for x_val in range(x,max_x):
                for y_val in range(y,max_y):
                    pixels[x_val,y_val] = colour
            break
        except IndexError:
            if x < 0:
                x = 0
            elif max_x > width:
                max_x = width
            elif y < 0:
                y = 0
            elif max_y > height:
                max_y = height

    return(image)


###############################################################################
def draw_line(image, (sx,sy), (dx,dy), (ex,ey), colour):
    """
    Draw line beginning at (x,y) on slope (deltax,deltay) until 
    the line hits (ex,ey) into image.  
    Only the part of line that is in image is drawn.
    Note that ex or ey can be None (not both), in which case the other 
    is used as the end.
    Assumes top-left of image is (0,0)
    INPUTS:
      image - an Image object
      (sx,sy) - coordinate of start of line
      (dx,dy) - change in x and y for each pixel
              - (0,+1) horizontal right
              - (0,-1) horizontal left etc
      (ex,ey) - End is x or y get to these points. One can be None,
                in which case the other is used as the terminating condition.
      colour  - [R,G,B] list
    
    Function draws lines using brute force. Ignores errors and keeps adding
    dx/dy to sx and sy until sx==ex or sy==ey.
    
    pixels[sx,sy] = colour is used before sx==ex or sy==ey to ensure that
    one pixel can be drawn.
    
    RETURNS: nothing
    """

    assert not image == None
    width,height = image.size
    pixels = image.load()
    

    while True:
        try:
            pixels[sx,sy] = colour
            if sx == ex or sy == ey:
                break
            sx += dx
            sy += dy

        except IndexError:
            if sx == ex or sy == ey:
                break
            sx += dx
            sy += dy

    return image


###############################################################################
def set_colour(image, colour):
    """
    Set all pixels in `image` to `colour`
    
    INPUTS:
      image - an Image object
      colour - [R,G,B] list for background
    
    RETURNS: Nothing
    IN-PLACE MODIFICATION: sets all pixels in `image` to `colour`
    """
    
    width, height = image.size
    pixels = image.load()
    for x in range(0,width):
        for y in range(0,height):
            pixels[x,y] = colour


###############################################################################
def draw_cafe(width, height, radius, offset, bg_colour, fg_colour):
    """
    Return an Image representing 
    a Cafe Wall Illusion using squares of side length radius
    in colour fg_colour on a bg_colour background.
    
    INPUTS:
      width, height - image size in pixels
      radius - side length of squares in pixels
      offset - proportion of square to offset in each odd row
               between 0 and 1
      bg_colour - [R,G,B] list for background
      fg_colour - [R,G,B] list for foreground
    
    1.
    Line starts with fg_colour square. fg_colour square is continuously added
    until square is either cut off or outside image.
    
    2. 
    Line starts with offset. fg_colour sqare is then drawn with a difference
    of int(offset*radius) added to the start. Draw_square stops when square is
    either cut or outside image.
    
    3.
    Straight (one pixel) lines are drawn for y value of 0 += radius. 
    
    
    RETURNS: Image object
    """

    image = Image.new('RGB', (width, height))
    assert not image == None
    set_colour(image, bg_colour)
    
    
    #Refer to 1 above
    row = 0      
    while row <= height:
        i = 0
        while i < width:
            draw_square(image, (i, row), radius, fg_colour)
            i += radius+radius
        row += radius + radius

        
    #Refer to 2 above        
    row = radius       
    while row <= height:
        i = 0
        while i < width:
            draw_square(image, (i+int(offset*radius), row), radius, fg_colour)
            i += radius + radius
        row += radius + radius
    
    
    #Refer to 3 above    
    j = 0
    while j <= height:
        draw_line(image, (0,0+j), (1,0), (width,None), fg_colour)
        j += radius
    
              
    return image

###############################################################################
def copy(image,(sx,sy),(ex,ey),(dx,dy)):
    """
    INPUTS:
      image - an Image object
      (sx,sy) - coordinates of starting point of to be copied image
      (ex,ey) - end coordinates of to be copied image
      (dx,dy) - change in x and y for each pixel
              - (0,+1) horizontal right
              - (0,-1) horizontal left etc
    
    Image in the space of sx to ex and sy to ey is copied and moved a distance
    of dx and dy, in the horizontal and vertical directions respectively.
    
    This is useful in drawing the 3in1 to copy squares.
    
    RETURNS:Nothing
    """
    
    assert not image == None
    width,height = image.size
    pixels = image.load()
        
    for k in range(sx,ex):
        for j in range(sy,ey):
            colour = pixels[k,j]
            pixels[k+dy,j+dx] = colour
    
    return image
            
            
###############################################################################            
def invert(image,(sx,sy),(ex,ey)): 
    """
    INPUTS:
      image - an Image object
      (sx,sy) - coordinates of starting point of to be inverted image
      (ex,ey) - end coordinates of to be inverted image
    
    Image in the space of sx to ex and sy to ey is flipped/inverted.
    
    This is useful in drawing the 3in1 to copy squares.
    
    RETURNS:Nothing
    """
    
    assert not image == None
    width,height = image.size
    pixels = image.load() 

    for y in range(sy,ey/2+sy/2):
        for x in range(sx,ex):
            colorsource = pixels[x,y]
            colourtarget = pixels[x,ey+sy-y-1]
            pixels[x,y] = colourtarget
            pixels[x,ey+sy-y-1] = colorsource 
            
    return image


###############################################################################
def draw_three_in_one(radius, fg_colour, bg_colour):
    """
    Draw 3 nested squares of side length 3*radius, 
    4*radius and 5*radius in `fg_colour` on a background
    of 9 tiled frames in `bg_colour`, where each frame is 
    4 nested squares that are diagonaly shaded alternately.
    
    INPUTS:
      radius - width of an individual frame part == 
               1/3 sidelength of inner square
      fg_colour - colour of 3 inner squares
      bg_colour - colour of background frames
    RETURNS: 
      Image of size 24*radius x 24*radius with RGB values
    
    1. 
    The first third of image (1/3*width and 1/3*height) is shaded vertically 
    with bg_colour. The width between each line is radius/10. The width and height
    of the square is determined to be radius*8. First draw_line function shades 
    with increasing x values (right side of image), second draw_line function
    shades with increading y values (left side of image).
    
    2.
    Invert function used to flip the square in the nested squares of 3*radius,
    4*radius and 5*radius. Image is then copied to respective areas.
    
    3.
    The rest of the sqaures are copied again. Right after inverting once again.
    This time the whole square is inverted.
    
    4.
    fg_colour squares without fill are drawn using the draw_line function. Use of
    iterations to decide the starting points and size of squares.
    
    RETURNS: Image object
    """

    image = Image.new('RGB', (3*radius*8, 3*radius*8))
    assert not image == None
    set_colour(image, WHITE)

    width = 8*radius*3
    height = 8*radius*3

    #Refer to 1 above
    column = radius/10
    while column < 8*radius:
        draw_line(image, (column,0), (1,1), (8*radius,radius*8-column), bg_colour)
        draw_line(image, (0,column), (1,1), (8*radius-column,radius*8), bg_colour)
        column += 2*radius/10
    
    #Refer to 2 above    
    invert(image,(radius,radius),(radius*7,radius*7))
    invert(image,(radius*2,radius*2),(radius*6,radius*6))
    invert(image,(radius*3,radius*3),(radius*5,radius*5))
    invert(image,(0,0),(8*radius,8*radius))
    
    copy(image,(0,0),(8*radius,8*radius),(8*radius,0))
    copy(image,(0,0),(8*radius,8*radius),(0,8*radius))
    copy(image,(0,0),(8*radius,8*radius),(8*radius*2,8*radius))
    copy(image,(0,0),(8*radius,8*radius),(8*radius,8*radius*2))
    
    
    #Refer to 3 above 
    invert(image,(0,0),(radius*8,radius*8))
    
    copy(image,(0,0),(8*radius,8*radius),(8*radius*2,0)) 
    copy(image,(0,0),(8*radius,8*radius),(0,8*radius*2))
    copy(image,(0,0),(8*radius,8*radius),(8*radius*2,8*radius*2))
    copy(image,(0,0),(8*radius,8*radius),(8*radius,8*radius))
    
    
    #Refer to 4 above 
    for i in [0,1,2]:
        draw_line(image, (8.5*radius+radius*i,8.5*radius+radius*i), (1,0),
                  (8*radius*2-0.5*radius-radius*i,None), fg_colour)
        draw_line(image, (8.5*radius+radius*i,15.5*radius-radius*i), (1,0),
                  (8*radius*2-0.5*radius-radius*i,None), fg_colour)
    
    for i in [0,1,2]:
        draw_line(image, (8.5*radius+radius*i,8.5*radius+radius*i), (0,1),
                  (None,8*radius*2-0.5*radius-radius*i), fg_colour)
        draw_line(image, (15.5*radius-radius*i,8.5*radius+radius*i), (0,1),
                  (None,8*radius*2-0.5*radius-radius*i), fg_colour)
        
    return image 


###############################################################################
def images_equal(im1, im2):
    """
    Compare the pixel values of two images, returning
    True if they are the same, False otherwise
    INPUTS:
       im1, im2 - both Image objects
    RETURNS:
       True if pixel values of `im1` and `im2` are the same
       False otherwise
    """

    if not im1.size == im2.size:
        return False

    width,height = im1.size

    p1 = im1.load()
    p2 = im2.load()
    for x in range(0,width):
        for y in range(0,height):
            if not p1[x,y] == p2[x,y]:
                return False
    return True


###############################################################################       
def test_all(output_file, testlist):
    """
    Run all tests provided in `testlist` and print a HTML section 
    for each (which is an h2 heading and a table showing the 
    desired and obtained images).
    
    INPUTS:
      output_file - an open file object (NOT a filename)
      testlist - a list of dictionaries, where each dictionary contains
                'name'  - printed as heading and used 
                          without spaces as the image filenames
             'function' - name of function to call as string
                          This function should not return anything.
               'params' - List of parameters (in the correct order)
                          as strings for passing to the funciton.
                          The parameter "canvas" is available as an
                          empty image that is the same size as...
               'result' - An Image object that is the expected result
                          of calling funciton(params)
    RETURNS: Nothing.

    IN-PLACE MODIFICATION: 
      Outputs HTML to `output_file` that includes for each element of 
      `testlist`, `tc`:
         A h2 heading that is tc['name'] and Passed or Failed
         The desired image (tc['result'])
         The obtained image (canvas after tc['function'](tc['params']) is run)
    """
    
    assert not output_file == None
    for tc in testlist:
        result_image = tc['result']
        canvas = Image.new('RGB', result_image.size)

        cmd = "{0}({1})".format(tc['function'], ",".join([str(p) for p in tc['params']]))
        print(cmd)
        answer = eval(cmd)
        if answer == None:
            answer = canvas

        wanted_filename = "{0}-wanted.png".format(tc['name']).replace(" ", "")
        got_filename    = "{0}-got.png".format(tc['name']).replace(" ", "")
        answer.save(got_filename)
        result_image.save(wanted_filename)

        pass_fail = "Passed" if images_equal(answer, result_image) else "Failed"
        output_file.write("<h2>{0} - {1}</h2>".format(tc['name'], pass_fail))
        output_file.write("<table><tr>\n")
        output_file.write("<td><img src={0} width=200></td>\n".format(wanted_filename))
        output_file.write("<td><img src={0} width=200></td></tr>\n".format(got_filename))
        output_file.write("<tr><td>Wanted</td><td>Got</td></tr>\n")
        output_file.write("</table>\n")



###############################################################################
# Test cases
###############################################################################
#draw_line((-2,-2), (+1,+1), (20,20), RED)
#to test if draw_line works outside image parameters
res1 = Image.new('RGB', (5, 5))
res1.putdata([
        RED  ,BLACK,BLACK,BLACK,BLACK, 
        BLACK,RED  ,BLACK,BLACK,BLACK, 
        BLACK,BLACK,  RED,BLACK,BLACK, 
        BLACK,BLACK,BLACK,  RED,BLACK, 
        BLACK,BLACK,BLACK,BLACK,  RED 
    ])
#draw_line((2,1), (0,0), (None,1), RED)
#to test if draw_line can draw one pixel
res2 = Image.new('RGB', (5, 3))
res2.putdata([
        BLACK,BLACK,BLACK,BLACK,BLACK, 
        BLACK,BLACK, RED ,BLACK,BLACK, 
        BLACK,BLACK,BLACK,BLACK,BLACK 
    ])
#draw_line((6,5), (-1,-1), (-1,2), RED)
#to test if draw_line can draw in reverse
res3 = Image.new('RGB', (5, 5))
res3.putdata([
        BLACK, RED ,BLACK,BLACK,BLACK, 
        BLACK,BLACK, RED ,BLACK,BLACK, 
        BLACK,BLACK,BLACK, RED ,BLACK, 
        BLACK,BLACK,BLACK,BLACK, RED , 
        BLACK,BLACK,BLACK,BLACK,BLACK
    ])
#draw_square((1,1), 3, RED)
#tests if draw_square works
res4 = Image.new('RGB', (5, 5))
res4.putdata([
        BLACK,BLACK,BLACK,BLACK,BLACK, 
        BLACK, RED , RED , RED ,BLACK, 
        BLACK, RED , RED , RED ,BLACK, 
        BLACK, RED , RED , RED ,BLACK, 
        BLACK,BLACK,BLACK,BLACK,BLACK 
    ])
#draw_square((-1,-1), 5, RED)
#tests if draw_square works outside image parameters
res5 = Image.new('RGB', (5, 5))
res5.putdata([
        RED  , RED , RED , RED ,BLACK, 
        RED  , RED , RED , RED ,BLACK,
        RED  , RED , RED , RED ,BLACK, 
        RED  , RED , RED , RED ,BLACK,
        BLACK,BLACK,BLACK,BLACK,BLACK 
    ])
#draw_line((-2,-2), (+1,+1), (20,20), RED)
#tests if draw_square can fill a whole image, also tests outside parameters
res6 = Image.new('RGB', (5, 5))
res6.putdata([
        RED , RED , RED , RED , RED , 
        RED , RED , RED , RED , RED ,
        RED , RED , RED , RED , RED , 
        RED , RED , RED , RED , RED ,
        RED , RED , RED , RED , RED
    ])
#draw_cafe(6, 6, 2, 1, WHITE, BLACK)
#tests draw_cafe with offset 1
res7 = Image.new('RGB', (6, 6))
res7.putdata([
        BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,
        BLACK,BLACK,WHITE,WHITE,BLACK,BLACK,
        BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,
        WHITE,WHITE,BLACK,BLACK,WHITE,WHITE,
        BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,
        BLACK,BLACK,WHITE,WHITE,BLACK,BLACK,
    ])
#draw_cafe(10, 10, 2, 0.5, WHITE, BLACK)
#basic test of draw_cafe on a larger scale
res8 = Image.new('RGB', (10, 10))
res8.putdata([
        BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK, 
        BLACK,BLACK,WHITE,WHITE,BLACK,BLACK,WHITE,WHITE,BLACK,BLACK,
        BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK, 
        WHITE,BLACK,BLACK,WHITE,WHITE,BLACK,BLACK,WHITE,WHITE,BLACK, 
        BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK, 
        BLACK,BLACK,WHITE,WHITE,BLACK,BLACK,WHITE,WHITE,BLACK,BLACK,
        BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK, 
        WHITE,BLACK,BLACK,WHITE,WHITE,BLACK,BLACK,WHITE,WHITE,BLACK,
        BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,
        BLACK,BLACK,WHITE,WHITE,BLACK,BLACK,WHITE,WHITE,BLACK,BLACK,             
    ])
#draw_cafe(10, 10, 2, 0, WHITE, BLACK)
#tests draw_cafe with offset 0, on a large scale
res9 = Image.new('RGB', (10, 10))
res9.putdata([
        BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK, 
        BLACK,BLACK,WHITE,WHITE,BLACK,BLACK,WHITE,WHITE,BLACK,BLACK,
        BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK, 
        BLACK,BLACK,WHITE,WHITE,BLACK,BLACK,WHITE,WHITE,BLACK,BLACK, 
        BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK, 
        BLACK,BLACK,WHITE,WHITE,BLACK,BLACK,WHITE,WHITE,BLACK,BLACK,
        BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK, 
        BLACK,BLACK,WHITE,WHITE,BLACK,BLACK,WHITE,WHITE,BLACK,BLACK,
        BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,
        BLACK,BLACK,WHITE,WHITE,BLACK,BLACK,WHITE,WHITE,BLACK,BLACK,             
    ])


"""
Note: No testing is done for 3in1 as it is difficult to replicate
manually
Note: canvas is defined in the test harness to be the same 
size as result with a BLACK background
"""
test_cases = [
    {'name':'Test 1', 
     'function':'draw_line', 
     'params':['canvas','(-2,-2)', '(+1,+1)', '(20,20)', 'RED'], 
     'result': res1
    },
    {'name':'Test 2', 
     'function':'draw_line', 
     'params':['canvas','(2,1)', '(0,0)', '(None,1)', 'RED'], 
     'result': res2
    },
    {'name':'Test 3', 
     'function':'draw_line', 
     'params':['canvas','(6,5)', '(-1,-1)', '(-1,-2)', 'RED'], 
     'result': res3
    },
    {'name':'Test 4', 
     'function':'draw_square', 
     'params':['canvas','(1,1)', '3', 'RED'], 
     'result': res4
    },
    {'name':'Test 5', 
     'function':'draw_square', 
     'params':['canvas','(-1,-1)', '5', 'RED'], 
     'result': res5
    },
    {'name':'Test 6', 
     'function':'draw_square', 
     'params':['canvas','(-1,-1)', '10', 'RED'], 
     'result': res6
    },
    {'name':'Test 7', 
     'function':'draw_cafe', 
     'params':['6', '6', '2', '1', 'WHITE', 'BLACK'], 
     'result': res7
    },
    {'name':'Test 8', 
     'function':'draw_cafe', 
     'params':['10','10','2','0.5','WHITE','BLACK'], 
     'result': res8
    },  
    {'name':'Test 9', 
     'function':'draw_cafe', 
     'params':['10','10','2','0','WHITE','BLACK'], 
     'result': res9
    }  
        
]


###############################################################################
def main():
    """
    Main function to generate www page
    """
    
    #saves cafe and three in one, with predetermined inputs
    radius   = 50
    image = draw_cafe(int(10.5*radius), 10*radius, radius, 0.66, WHITE, BLACK)
    image.save(CAFE_FILE)

    radius = 20
    image = draw_three_in_one(radius, RED, BLACK)
    image.save(THREE_IN_ONE_FILE)

    f = open(TEST_REPORT, 'w')
    assert not f == None
    
    f.write('<html>\n')
    f.write('<head>\n')
    f.write('<title>William Pan 694945</title>')
    f.write('</head>\n')  
    f.write('<body>\n')
    f.write('<h1><u>William Pan 694945</u></h1>')
    f.write('<table>\n')
    f.write('<table><tr>\n')
    f.write('<td><img src={0}></td>\n'.format(CAFE_FILE))
    f.write('<td><img src={0}></td></tr>\n'.format(THREE_IN_ONE_FILE))
    f.write('<tr><td>Cafe</td><td>Three in one</td></tr>\n')
    f.write('</table>')                      
    f.write('<h1><u>Test Cases</u></h1>')    
    
    #saves and draws test cases    
    test_all(f, test_cases)
    
    f.write('</body>\n')
    f.write('</html>')
    f.close()
    
    #test for infinite loops, or errors
    print "done"

main()
