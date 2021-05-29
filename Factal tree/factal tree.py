import turtle as tl 

def draw_smalltree(tree_length,tree_angle):
    '''
         Fractal tree function
    '''
    if tree_length >= 3:
        tl.forward(tree_length) #Forward painting
        tl.right(tree_angle)  #turn right
        draw_smalltree(tree_length - 10,tree_angle)#Draw a branch until the branch length is less than 3

        tl.left(2 * tree_angle)  # 
        draw_smalltree(tree_length -10,tree_angle) #Until the branch length is less than 3

        tl.rt(tree_angle) #Turn to the positive direction, then go back to the previous level
        if tree_length <= 30:  #The branch length is less than 30, can be used as leaves, the leaves are green
            tl.pencolor('green')
        if tree_length > 30:
            tl.pencolor('brown')  #The trunk part is brown
        tl.backward(tree_length)  #Back to draw, back to the previous level



def main():
    tl.penup()
    #tl.pencolor('green')
    tl.left(90)  #Because the tree is upwards, turn the direction to the left first
    tl.backward(250) #Put the starting point to the bottom
    tl.pendown()
    tree_length = 100  #I set the longest trunk to 100
    tree_angle = 20  #Branch bifurcation angle, I set it as 20
    draw_smalltree(tree_length,tree_angle)
    tl.exitonclick()  #Click to close the drawing window

if __name__ == '__main__':
    main()
