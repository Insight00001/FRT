import cv2

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
        
        img_canny = cv2.Canny(img, 100,200)
        img_canny = self.resize_img(img_canny)
        cv2.imshow("Canny",img_canny)
        cv2.imwrite("Josh_canny.jpg",img_canny)
        cv2.waitKey(0)
      
        return img_canny
    def 
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

run.canny_edge("josh.jpg")

