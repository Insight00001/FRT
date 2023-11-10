import cv2
import numpy as np

# read image from file
class Operations:
    def resize_img(self,img):
        scale = 10
        width = int(img.shape[1]*scale/100)
        height= int(img.shape[0]*scale/100)
        dim = (width,height)
        self.img= cv2.resize(img,dim,interpolation = cv2.INTER_AREA)
        return self.img
    def gray_image(self,img):
        gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        return gray_img
    def blur_image(self,img):
        img_blur = cv2.GaussianBlur(img,(3,3),3)
        return img_blur
   
    def img_shape(self,img):
        img_height = img.shape[0]
        img_width = img.shape[1]
        #channels = img.shape[2]
        print(img_height,img_width)
    def split_img(self,img):
        #b,g,r = cv2.split(img)
        img = cv2.imread(img)
        b= img[:,:,0]
        return b
    def make_boder(self,img):
        img = cv2.imread("josh.jpg")
        img = self.resize_img(img)
        img_boder = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=(255,0,0))
        cv2.imshow("Img",img_boder)
        cv2.waitKey(0)
        return img_boder
    def rotate_img(self,img):
        img = cv2.imread(img)
        img = self.resize_img(img)
        width,height = img.shape[:2]
        center = (width/2,height/2)
        angle90= 90
        angle180 = 180
        angle270 = 270
        scale = 1.0
        rotated = cv2.getRotationMatrix2D(center,angle270,scale)
        rotated90 = cv2.warpAffine(img,rotated,(height,width))

        cv2.imshow("Rotated Image",rotated90)
        cv2.waitKey(0)
        return rotated90
    def canny_edge(self,img):
        img = cv2.imread("josh.jpg")
        img = self.resize_img(img)
        img_canny = cv2.Canny(img, 100,200)
        print(len(img_canny))
      
        cv2.imshow("Canny",img_canny)
      
        cv2.waitKey(0)
      
        return img_canny
    def img_canny_vid(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret,img = cap.read()
            if not ret:
                break
            # convert BGR to HSV
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            #define range of red color in HSV
            lower_red =np.array((30,150,50))
            upper_red = np.array((255,255,150))
            # create a red HSV colour boundary and    
            # threshold HSV image   
            mask = cv2.inRange(hsv,lower_red,upper_red)
            res = cv2.bitwise_and(img,img,mask=mask)
            edges = cv2.Canny(img,100,200)
            cv2.imshow("Me",edges)
            if cv2.waitKey(0)&0XFF==ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
    
    def bilateral_filter(self):
        img = cv2.imread("josh.jpg")
        img= self.resize_img(img)
        blur = cv2.bilateralFilter(img,9,95,95)
 
        
        cv2.imshow("Blur",blur)
        cv2.waitKey(0)
    def boxfilter(self):
        img = cv2.imread("josh.jpg")
        img = self.resize_img(img)
        img_1 = cv2.boxFilter(img,0,(5,5),img,(-1,-1),False,cv2.BORDER_DEFAULT)
        cv2.imshow("BoxFilter",img_1)
        cv2.waitKey(0)

    def filter2d(self):
        img= cv2.imread("josh.jpg")
        img = self.resize_img(img)
        kernel = np.ones((5,5),np.float32)/25
        img_1 = cv2.filter2D(img,-1,kernel)

        cv2.imshow("Filter 2D",img_1)
        cv2.waitKey(0)

    def threshold(self):
        img = cv2.imread("josh.jpg")
        img = self.resize_img(img)
        retval,thres = cv2.threshold(img,62,255, cv2.THRESH_BINARY)
        cv2.imshow("Threshold",thres)
        cv2.waitKey(0)
    def getContour(self):
        img = cv2.imread("josh_bg.png")
        #img = self.resize_img(img)
        img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        ret,thes = cv2.threshold(img_gray,127,255,0)

        contour,hierachy = cv2.findContours(thes,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        cnt = contour[3]

        cv2.drawContours(img,contour,-1,(0,255,0),5)

        cv2.imshow("Img",img)
        cv2.waitKey(0)

    def adaptive_thresh(self):
        pass
    def read_image(self,name):
        img=cv2.imread(name,1)
        img= self.resize_img(img)
        img_sh=self.img_shape(img)
        img_pixel = img[100,100]
        img = self.gray_image(img)
        self.canny_edge(img)
        self.make_boder(img)
     
        
        
        cv2.imshow("My Image",img)
        cv2.waitKey(0)
        return img

    cv2.destroyAllWindows()


run = Operations()

run.getContour()

