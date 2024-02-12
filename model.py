from tensorflow.keras.models import load_model
import cv2




def convImg(impath,res=96):
    img = cv2.imread(impath)
    converted = cv2.cvtColor(cv2.resize(img,(res,res)),cv2.COLOR_BGR2GRAY)
    return converted

convImg("image.jpeg")
cv2.waitKey(0)
cv2.des