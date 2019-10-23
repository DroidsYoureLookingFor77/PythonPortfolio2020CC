#couldn't convert string to float with the word two

# Geometry Homework
#9/19

#Kaden Marden
#Connor Crowe
#Anthony Peraza
#Demetrius Whites

def triangle():
    print("Area of a triangle:\n")
    base_tri = input("Base of triangle:\n")
    height = input("Height of triangle:\n")
    area = 0.5*float(base_tri)*float(height)
    tri_shape = str.format("""

                |\ 
                | \ 
                |  \ 
                |   \ 
                |    \ 
                |     \ 
     {0:5}      |      \ 
                |       \ 
                |        \ 
                |         \ 
                |__________\ 
                         {1}
    Area of this triangle is: {2}
    """, height, base_tri, area)

    print(tri_shape)

def sq_perimeter():
    print("Perimeter of square:\n")
    length = input("Length of square:\n")
    heightsq = input("Height of square:\n")
    perimeter_of_square = float(length)*2+float(heightsq)*2
    print(perimeter_of_square)
    square_shape = str.format("""
                 ________
                l        l
                l        l {0}
                l        l
                l        l
                1________1
                  {1}
    Perimeter of this square is: {2}
    """, heightsq, length, perimeter_of_square)

    print(square_shape)

def sq_area():
    print("Area of square")
    print("Area in square feet:\n")
    length = float(input("Length of square:\n"))
    heightsq = float(input("Height of square:\n"))
    area_of_square = length * heightsq
    square_shape = str.format("""
                 ________
                l        l
                l        l {0}
                l        l
                l        l
                1________1
                  {1}
    Area of this square is: {2}
    """, heightsq, length, area_of_square)

    print(square_shape)

def circle():
    print("Circumference of a Circle")
    radius = input("Radius of circle:\n")
    circumferance = 2*3.14*float(radius)
    print(circumferance)
    print("Circumference of Circle")
    circ_shape= str.format("""
               , - ~ ~ ~ - ,
            ,                , 
          ,                    ,
         ,                      ,
         ,                      ,
         ,            -------------,{0}
         ,                      ,
         ,                      ,
          ,                    ,
            ,                 ,  
               - , _ _ _  , -
    Circumference of this circle is: {1:.2f}""", radius, circumferance)

    print(circ_shape)

def cube ():
    print("Volume of a cube:\n")
    side = input("Side of Cube:")
    volume = float(side)*float(side)*float(side)
    volume_square = str.format ("""

               _______________________                         
             /                       /l
            /                       / l
           /                       /  l
          /                       /   l
         /_______________________/    l    
         l                       1    l
         l                       l    l
         l                       l    l    
         l                       l    1
         l                       l    l
         l                       l   /
         l                       l  /
         l                       l /
         l_______________________l/
                            {0}
    Volume of this cube is: {1}
    """, side, volume)

    print(volume_square)

def prgrmEnd():
    question = input("""
Are you sure you want to quit?

1. Yes
2. No
""")
    if question == "1":
        exit()
    elif question == "2":
        return
    

#Menu System for Geometry Homework

print("""

1. Area of a Triangle
2. Perimeter of a Square
3. Area of a Square
4. Circumference of a Circle
5. Volume of a Cube
6. Close Program

""")

def menu():
    while True:
        choice = input("Pick an option from the menu: ")
        if choice == "1":
            triangle()
        elif choice == "2":
            sq_perimeter()
        elif choice == "3":
            sq_area()
        elif choice == "4":
            circle()
        elif choice == "5":
            cube()
        elif choice == "6":
            prgrmEnd()
        else:
            print("Sorry, that's not an acceptable input. Please try again.")
            return

menu()
