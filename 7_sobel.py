import cv2 as cv
import numpy as np

def my_sobel( img, sobel_1, sobel_2, ksize=3 ):
    #print( f"my_sobel( {sobel_1}, {sobel_2} )")

    img2 = img.copy()
    x_order_1, y_order_1 = sobel_1
    if ( x_order_1 > 0 ) or ( y_order_1 > 0 ):
        img2 = np.abs( cv.Sobel( img, cv.CV_64F, x_order_1, y_order_1, ksize=3 ) ) 
    
    img3 = img.copy()
    x_order_2, y_order_2 = sobel_2
    if ( x_order_2 > 0 ) or ( y_order_2 > 0 ):
        img3 = np.abs( cv.Sobel( img, cv.CV_64F, x_order_2, y_order_2, ksize=3 ) ) 

    return img2 * img3

def main():
    img = cv.imread( "images/window.jpg", cv.IMREAD_GRAYSCALE )
    set_1 = my_sobel( img, ( 1,0 ), ( 0,0 ) )
    set_2 = my_sobel( img, ( 0,1 ), ( 0,0 ) )
    set_3 = my_sobel( img, ( 2,0 ), ( 0,0 ) )
    set_4 = my_sobel( img, ( 0,2 ), ( 0,0 ) )
    set_5 = my_sobel( img, ( 1,1 ), ( 0,0 ) )
    set_6 = my_sobel( img, ( 1,0 ), ( 0,1 ) )
    set_7 = my_sobel( img, ( 0,2 ), ( 2,0 ) )
    set_8 = my_sobel( img, ( 1,0 ), ( 2,0 ) )
    set_9 = my_sobel( img, ( 0,0 ), ( 0,0 ) )
    cv.imshow( "img1", set_1 )
    cv.imshow( "img2", set_2 )
    cv.imshow( "img3", set_3 )
    cv.imshow( "img4", set_4 )
    cv.imshow( "img5", set_5 )
    cv.imshow( "img6", set_6 )
    cv.imshow( "img7", set_7 )
    cv.imshow( "img8", set_8 )
    cv.imshow( "img9", set_9 )
    
    cv.waitKey( 0 )

main()