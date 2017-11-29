"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Jack Cook.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    #circle_and_rectangle()
    lines()

def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    window = rg.RoseWindow(800, 400)
    centerpoint1 = rg.Point (400, 300)
    centerpoint2 = rg.Point (600, 100)
    radius1 = 100
    radius2 = 50
    circle1= rg.Circle(centerpoint1,radius1)
    circle1.fill_color = 'blue'
    circle2= rg.Circle(centerpoint2,radius2)
    circle1.attach_to(window)
    circle2.attach_to(window)
    window.render()
    window.close_on_mouse_click()


    # ------------------------------------------------------------------
    #
    # Done: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    window=rg.RoseWindow(800,600)
    x1=200
    y1=200
    centerpoint1=(x1, y1)
    radius=100
    x2=300
    y2=300
    x3=500
    y3=400
    cornerpoint1=(x2,y2)
    cornerpoint2=(x3,y3)
    centerpoint2=(x3-x2,y3-y2)
    circle=rg.Circle(centerpoint1,radius)
    circle.fill_color='blue'
    rectangle=rg.Rectangle(cornerpoint1,cornerpoint2)
    circle.attach_to(window)
    rectangle.attach_to(window)

    print(circle.outline_thickness)
    print(circle.fill_color)
    print(centerpoint1)
    print(x1)
    print(y1)

    print(rectangle.outline_thickness)
    print(centerpoint2)
    print(x3-x2)
    print(y3-y2)

    window.render()
    window.close_on_mouse_click()

    # ------------------------------------------------------------------
    # TODO: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    window=rg.RoseWindow(800,600)
    x1=0
    y1=0
    x2=400
    y2=300
    x3=200
    y3=0
    x4=600
    y4=300
    start1=(x1,y1)
    start2=(x3,y3)
    end1=(x2,y2)
    end2=(x4,y4)
    line1=rg.Line(start1,end1)
    line2=rg.Line(start2,end2)
    line1.attach_to(window)
    line2.attach_to(window)
    print(line1.get_midpoint())
    print(x2-x1)
    print(y2-y1)
    print(line2.get_midpoint())
    print(x4-x3)
    print(y4-y3)

    window.render()
    window.close_on_mouse_click()

    line1=rg.Line()
    # ------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
