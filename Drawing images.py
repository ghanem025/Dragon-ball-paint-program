#graphics.py
# Dragonball themed paint program
#paint program includes many tools such as pencil,marker,eraser,spray,bucket,etc...
#paint program also allowss user to us both filled and in filled shapes






from pygame import*
from math import*
from glob import*

from random import*
res=(1440,720)
screen=display.set_mode(res)
running=True



font.init()
sayianfont= font.Font("Saiyan-Sans.ttf",30)
def fonts(name,mx,my,text):
    txt=name(text,True,(230,120,0))
    screen.blit(txt,(mx,my))
             
quotes=["you whats up"]
Background = image.load("images/background.png")## adds the background
screen.blit(Background,(0,0))
pencilRect = Rect(20,60,75,75)# this creates an imaginary box for your tool/stamp
eraseRect= Rect(20,140,75,75)
sprayRect = Rect(20,220,75,75)
bucketRect= Rect (20,300,75,75)
markerRect= Rect(20,380,75,75)
clearRect= Rect(20,460,75,75)
shaperect= Rect(140,60,75,75)
rectfillrect= Rect(140,140,75,75)
ellipserect= Rect (140,220,75,75)
ellipsefillrect= Rect (140,300,75,75)
box= Rect (1040,300,250,200)


white= Rect (230,5,850,550)# this adds the canvas
gokuRect= Rect (600,565,150,130)
vegetaRect= Rect(800,565,150,130)
friezarect= Rect(500,565,150,130)
vegitorect= Rect ((950,565,150,130))
colorpalette= Rect(20,560,150,140)
blackrect= Rect((350,565,150,130))
bardockrect= Rect ((200,565,150,130))
gogetarect= Rect(1100,565,150,132)
zamausrect= Rect(1250,565,150,131)
##shaperect= Rect
Goku= image.load("images/goku.png")# this represents the stamp
vegeta= image.load("images/vegeta.png")
gokuicon=image.load("images/gokuicon.png")# this represents the icons for the stams
vegetaicon = image.load("images/vegetaicon.png")
pencilicon=image.load("images/pencil.png")
colorpicker=image.load("images/colorpalette.png")
erasericon=image.load("images/eraser.png")
sprayicon=image.load("images/spray.png")
bucketicon=image.load("images/bucket.png")
markericon=image.load("images/marker.png")
##dragonball=image.load("images/dragonball.png")
frieza=image.load("images/frieza.png")
friezaicon=image.load("images/friezaicon.png")
picvegito=image.load("images/vegito.png")
vegitoicon=image.load("images/vegitoicon.png")
blackgokuicon=image.load("images/blackgokuicon.png")
blackgoku=image.load("images/blackgoku.png")
picbardock=image.load("images/bardock.png")
bardockicon=image.load("images/bardockicon.png")
toolz=image.load("images/toolztext.png")
gogeta=image.load("images/gogeta.png")
gogetaicon=image.load("images/gogetaicon.png")
roshi=image.load("images/roshi.png")
ellipseicon=image.load("images/ellipseicon.png")
ellipsefillicon=image.load("images/ellipsefillicon.png")
clearicon=image.load("images/clear.png")
rectangleicon=image.load("images/rectangleicon.png")
rectanglefill=image.load("images/rectanglefill.png")
zamauspic=image.load("images/zamaus.png")
zamausicon=image.load("images/zamausicon.png")

zamaus=0
pencil=0
mx,my=0,0
pos=0
erase=0
picg=0
spray=0#varibale for specified tool
bucket=0
picv=0
marker=0#varibale for specified tool
size=5#varibale for size
ellipsetool=0#varibale for ellipse filled
s=0
rectfill=0
picfrieza=0
c=0#varibale for specified for color
vegito=0#varibale for specified stamp
radius=2
black=0
copy=screen.copy
clear=0
rectangle=0
bardock=0
undo=0
ellipse2=0#varibale for ellipse unfilled
gogetapic=0
redo=0

draw.rect(screen,(255,255,255),white)# draws a white rectangle for the canvas
running=True
while running:
    keypresses=False
    for e in event.get():
        print(e)
        if e.type==QUIT:
            running=False
        if e.type == KEYDOWN:
            if e.key == K_BACKSPACE:
                if len(ans)>0:
                         ans = ans[:1]
            elif e.key == K_KP_ENTER or e.key == K_RETURN:##################################
                    ans=""
            elif e.key < 265:
                ans+= e.unicode


        if e.type==MOUSEBUTTONDOWN:
            pic=screen.copy()
            if e.button == 4:
                size+=1# increases size 
            elif e.button ==5:
                size-=1#decreases size
            if size==0:
                size+=1 # this allows for the size to never reach zero
        if e.type==MOUSEBUTTONDOWN and white.collidepoint(mx,my):
            image.save(screen.subsurface(white),"dragonball.png")#copys whatever you have on canvas and creates a png file
            copy=screen.copy()
            if e.button==1:
                rmx=e.pos# gives postion of rmx
                rmy=e.pos
                rmx=mx
                rmy=my
             
                





    #-----------
    mb=mouse.get_pressed()
    omx,omy= mx,my
    mx,my=mouse.get_pos()

    fonts(sayianfont.render,1080,350,"welcome to the best ")
    fonts(sayianfont.render,1080,400,"dragonball paint ever.")
    fonts(sayianfont.render,1080,450,"you have your tools on the left")
    fonts(sayianfont.render,1080,500,"and stamps on the bottom enjoy")

    if e.type==MOUSEBUTTONDOWN and white.collidepoint(mx,my):
        copy=screen.copy


    if colorpalette.collidepoint(mx,my) and mb[0]==1:
        c=screen.get_at((mx,my))# takes the colocr of the pixel the cursor is hovering over



    if mb[1]==1:
        s+=0

    if white.collidepoint(mx,my) and mb[0]==1:# if the mouse button hits the canvas than...
        screen.set_clip(white)
        if clear==1:
            draw.rect(screen,(255,255,255),white)# places a white sheet on top of the canvas giving the illusion of clearing

        if marker==1 and mb[0]==1:
            draw.line(screen,(c),(omx,omy),(mx,my),size)

        if pencil==1 and mb[0]==1:# if a tool is choosen it is turned into one
            draw.circle(screen,(c),(mx,my),size)
        if erase==1 and mb[0]==1:
            draw.circle(screen,(255,255,255),(mx,my),size)# drawing a white circle gives the illusion of erasing
        if spray==1 and mb[0]==1:
            sprayx=(randint(mx-size,mx+size)) #))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
            sprayy=(randint(my-size,my+size))
            if hypot(mx-sprayx,my-sprayy)<size:
                draw.circle(screen,(c),(sprayx,sprayy) ,1)
                time.wait(5)
        if picg==1 and mb[0]==1:
            screen.blit(pic,(0,0))# stops the picture from dragging by creating a still image
            screen.blit(Goku,(mx-175,my-172))# adds the picture of your current image
        if bucket==1 and mb[0]==1:
            draw.rect(screen,(c),white)
        if picv==1 and mb[0]==1:
            screen.blit(pic,(0,0))
            screen.blit(vegeta,(mx-150,my-150))
        if picfrieza==1 and mb[0]==1:
            screen.blit(pic,(0,0))
            screen.blit(frieza,(mx-150,my-150))
        if vegito==1 and mb[0]==1:
            screen.blit(pic,(0,0))
            screen.blit(picvegito,(mx-150,my-150))
        if rectangle==1 and mb[0]==1:
            ##screen.set_clip(white)
            ##screen.blit(copy,(0,0))
            screen.blit(pic,(0,0))
            draw.rect(screen,(c),(rmx,rmy,mx-rmx,my-rmy),2)# adds the shape making them subtract coordinates(mx-rmx,my-rmy) lets the usere drag the shape into whatever size he,she wants
        if black==1 and mb[0]==1:
            screen.blit(pic,(0,0))
            screen.blit(blackgoku,(mx-150,my-150))
        if bardock==1 and mb[0]==1:
            screen.blit(pic,(0,0))
            screen.blit(picbardock,(mx-150,my-150))
        if gogetapic==1 and mb[0]==1:
            screen.blit(pic,(0,0))
            screen.blit(gogeta,(mx-150,my-150))
        if zamaus==1 and mb[0]==1:
            screen.blit(pic,(0,0))
            screen.blit(zamauspic,(mx-150,my-150))
        
            
        if undo==1 and mb[0]==1:
            screen.set_clip(white)
        if rectfill==1 and mb[0]==1:
            ##screen.set_clip(white)
            ##screen.blit(copy,(0,0))
            screen.blit(pic,(0,0))
            draw.rect(screen,(c),(rmx,rmy,mx-rmx,my-rmy))
    ##if radius>width:
        if ellipsetool==1 and mb[0]==1:
            ##width=(mx-x,1)
            ##radius=(my-y,1)
            screen.blit(pic,(0,0))
            ellipsefill= Rect (rmx,rmy,mx-rmx,my-rmy)
            ellipsefill.normalize()#dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
            draw.ellipse(screen,(c),ellipsefill,0)
        if ellipse2==1 and mb[0]==1:
            screen.blit(pic,(0,0))
            ellipse= Rect (rmx,rmy,mx-rmx,my-rmy)
            ellipse.normalize()
            if ellipse.width<radius*2 or ellipse.height<radius*2:# this checks if the radius of the ellipse is greater than the width or eight of the ellipse if its not you draw an infilled ellipse
                draw.ellipse(screen,(c),ellipse)
            else:
                draw.ellipse(screen,(c),ellipse,radius)







                
        

##        if rectangle==1 and mb[3]==1:
##            draw.rect(screen,(c),(mx,my,size,size))



    draw.rect(screen,(0,255,0),pencilRect,2)#adds a rectangle for the user to select the tools
    draw.rect(screen,(255,0,0),eraseRect,2)
##    draw.rect(screen,(255,0,255),gokuRect,2)
    draw.rect(screen,(255,45,100),sprayRect,2)
    draw.rect(screen,(0,0,255),bucketRect,2)
    draw.rect(screen,(0,255,0),rectfillrect,2)

    draw.rect(screen,(255,0,100),markerRect,2)
    draw.rect(screen,(255,111,111),clearRect,2)
    draw.rect(screen,(255,100,50),shaperect,2)
    draw.rect(screen,(50,100,200),ellipserect,2)
    draw.rect(screen,(50,100,250),ellipsefillrect,2)
    
    draw.rect(screen,(c),(1203,10,75,75))

    screen.blit(gokuicon,(650,565))#adds icons for tools and stamps allows for change of postion to the icons
    screen.blit(colorpicker,(20,560))
    screen.blit(pencilicon,(-40,45))
    screen.blit(erasericon,(30,140))
    screen.blit(sprayicon,(20,220))
    screen.blit(vegetaicon,(800,565))
    screen.blit(bucketicon,(20,300))
    screen.blit(markericon,(40,380))
    screen.blit(friezaicon,(500,565))
    screen.blit(vegitoicon,(950,565))
    screen.blit(blackgokuicon,(350,565))
    screen.blit(bardockicon,(200,565))
    screen.blit(toolz,(20,10))
    screen.blit(gogetaicon,(1100,565))
    screen.blit(roshi,(1300,250))
    screen.blit(ellipseicon,(140,300))
    screen.blit(ellipsefillicon,(140,225))
    screen.blit(clearicon,(20,460))
    screen.blit(rectangleicon,(140,65))
    screen.blit(rectanglefill,(155,155))
    screen.blit(zamausicon,(1250,565))
    

    

    if pencilRect.collidepoint(mx,my) and mb[0]==1:# checks if the mouse hits the box, if it does it activates the tool
       
        
        draw.rect(screen,(255,0,0),pencilRect,2)# this highlights the rectangle whnever its clicked
        pencil=1# ones the tool is selected as one it means it is active
        erase=0# every time you use a certain tool all the other tools become 0 so they don't interfer with the selected tool
        spray=0
        bucket=0
        picg=0
        picv=0
        marker=0
        clear=0
        picfrieza=0
        vegito=0
        rectangle=0
        black=0
        bardock=0
        ellipsetool=0
        ellipse2=0
        zamaus=0
        gogetapic=0

    if eraseRect.collidepoint(mx,my) and mb[0]==1:
 
        draw.rect(screen,(255,0,255),eraseRect,2)
        erase=1
        pencil=0
        spray=0
        bucket=0
        picg=0
        picv=0
        marker=0
        clear=0
        picfrieza=0
        vegito=0
        rectangle=0
        black=0
        bardock=0
        ellipsetool=0
        rectfill=0
        ellipse2=0
        zamaus=0
        gogetapic=0

    if gokuRect.collidepoint(mx,my) and mb[0]==1:
        picg=1
        spray=0
        pencil=0
        erase=0
        picv=0
        marker=0
        clear=0
        bucket=0
        picfrieza=0
        vegito=0
        rectangle=0
        black=0
        bardock=0
        ellipsetool=0
        rectfill=0
        ellipse2=0
        gogetapic=0
        zamaus=0

    if sprayRect.collidepoint(mx,my) and mb[0]==1:
        
        spray=1
        pencil=0
        erase=0
        bucket=0
        picg=0
        picv=0
        marker=0
        clear=0
        picfrieza=0
        vegito=0
        rectangle=0
        black=0
        bardock=0
        ellipsetool=0
        rectfill=0
        ellipse2=0
        gogetapic=0
        zamaus=0

    if bucketRect.collidepoint(mx,my) and mb[0]==1:
      

        
        draw.rect(screen,(0,111,200),bucketRect,2)
        bucket=1
        spray=0
        pencil=0
        erase=0
        picg=0
        picv=0
        marke=0
        clear=0
        picfrieza=0
        vegito=0
        rectangle=0
        black=0
        bardock=0
        ellipsetool=0
        ellipse2=0
        gogetapic=0
        zamaus=0

    if vegetaRect.collidepoint(mx,my) and mb[0]==1:
        picv=1
        spray=0
        pencil=0
        erase=0
        bucket=0
        picg=0
        clear=0
        picfrieza=0
        vegito=0
        rectangle=0
        black=0
        bardock=0
        ellipsetool=0
        rectfill=0
        ellipse2=0
        zamaus=0


    if markerRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(150,255,50),markerRect,2)
        marker=1
        spray=0
        pencil=0
        bucket=0
        erase=0
        picg=0
        picv=0
        clear=0
        picfrieza=0
        vegito=0
        rectangle=0
        black=0
        bardock=0
        ellipsetool=0
        rectfill=0
        ellipse2=0
        zamaus=0
        gogetapic=0

    if clearRect.collidepoint(mx,my) and mb[0]==1:
        
        draw.rect(screen,(0,111,200),clearRect,2)
        clear=1
        spray=0
        pencil=0
        erase=0
        bucket=0
        picg=0
        picv=0
        marker=0
        picfrieza=0
        vegito=0
        rectangle=0
        black=0
        bardock=0
        ellipsetool=0
        rectfill=0
        ellipse2=0
        zamaus=0
        gogetapic=0

    if shaperect.collidepoint(mx,my) and mb[0]==1:
        clear=0
        spray=0
        pencil=0
        erase=0
        bucket=0
        picg=0
        picv=0
        marker=0
        rectangle=1
        picfrieza=0
        vegito=0
        black=0
        bardock=0
        ellipsetool=0
        rectfill=0
        ellipse2=0
        zamaus=0
        gogetapic=0

    if friezarect.collidepoint(mx,my) and mb[0]==1:
        clear=0
        spray=0
        pencil=0
        erase=0
        bucket=0
        picg=0
        picv=0
        marker=0
        rectangle=0
        picfrieza=1
        vegito=0
        black=0
        bardock=0
        ellipsetool=0
        rectfill=0
        ellipse2=0
        zamaus=0
        gogetapic=0
    if vegitorect.collidepoint(mx,my) and mb[0]==1:
        clear=0
        spray=0
        pencil=0
        erase=0
        bucket=0
        picg=0
        picv=0
        marker=0
        rectangle=0
        picfrieza=0
        vegito=1
        black=0
        bardock=0
        ellipsetool=0
        rectfill=0
        gogetapic=0
        ellipse2=0
        zamaus=0
    if blackrect.collidepoint(mx,my) and mb[0]==1:
        clear=0
        spray=0
        pencil=0
        erase=0
        bucket=0
        picg=0
        picv=0
        marker=0
        rectangle=0
        picfrieza=0
        vegito=0
        black=1
        bardock=0
        ellipsetool=0
        rectfill=0
        ellipse2=0
        gogetapic=0
        zamaus=0
        
    if bardockrect.collidepoint(mx,my) and mb[0]==1:
        clear=0
        spray=0
        pencil=0
        erase=0
        bucket=0
        picg=0
        picv=0
        marker=0
        rectangle=0
        picfrieza=0
        vegito=0
        black=0
        bardock=1
        rectfill=0
        ellipsetool=0
        ellipse2=0
        zamaus=0
        gogetapic=0
    ##if undorect.collidepoint(mx,my) and mb[0]==1:
        ##clear=0

    if rectfillrect.collidepoint(mx,my) and mb[0]==1:
        clear=0
        spray=0
        pencil=0
        erase=0
        bucket=0
        picg=0
        picv=0
        marker=0
        rectangle=0
        picfrieza=0
        vegito=0
        black=0
        bardock=0
        rectfill=1
        ellipsetool=0
        ellipse2=0
        zamaus=0
        gogetapic=0
    if ellipserect.collidepoint(mx,my) and mb[0]==1:
        clear=0
        spray=0
        pencil=0
        erase=0
        bucket=0
        picg=0
        picv=0
        marker=0
        rectangle=0
        picfrieza=0
        vegito=0
        black=0
        bardock=0
        rectfill=0
        ellipsetool=1
        ellipse2=0
        gogetapic=0
        zamaus=0
    if ellipserect.collidepoint(mx,my) and mb[0]==1:
        clear=0
        spray=0
        pencil=0
        erase=0
        bucket=0
        picg=0
        picv=0
        marker=0
        rectangle=0
        picfrieza=0
        vegito=0
        black=0
        bardock=0
        rectfill=0
        ellipsetool=1
        ellipse2=0
        gogetapic=0
        zamaus=0
    if ellipsefillrect.collidepoint(mx,my) and mb[0]==1:
        clear=0
        spray=0
        pencil=0
        erase=0
        bucket=0
        picg=0
        picv=0
        marker=0
        rectangle=0
        picfrieza=0
        vegito=0
        black=0
        bardock=0
        rectfill=0
        ellipsetool=0
        ellipse2=1
        gogetapic=0
        zamaus=0
    if gogetarect.collidepoint(mx,my) and mb[0]==1:
        clear=0
        spray=0
        pencil=0
        erase=0
        bucket=0
        picg=0
        picv=0
        marker=0
        rectangle=0
        picfrieza=0
        vegito=0
        black=0
        bardock=0
        rectfill=0
        ellipse2=0
        gogetapic=1
        ellipsetool=0
        zamaus=0
    if zamausrect.collidepoint(mx,my) and mb[0]==1:
        clear=0
        spray=0
        pencil=0
        erase=0
        bucket=0
        picg=0
        picv=0
        marker=0
        rectangle=0
        picfrieza=0
        vegito=0
        black=0
        bardock=0
        rectfill=0
        ellipse2=0
        gogetapic=0
        ellipsetool=0
        zamaus=1


        



    display.flip()
quit()
