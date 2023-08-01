'''
320 x int(W_View_size / 1.333)
640 x int(W_View_size / 1.777
320 x 240
640 x 480
800 x 600
1280 x 300
'''
import cv2

class Camera():
  def __init__(self,cameraNum   : int,
                    cameraWidth : int,
                    cameraHieght: int,
                    cameraFPS   : int):
    
    self.cap = cv2.VideoCapture(cameraNum)

    if not self.cap.isOpened():
      raise ValueError("Failed to open the camera. Check if the cameraNum is correct.")
    self.cameraWidth  = cameraWidth
    self.cameraHieght = cameraHieght
    self.camerFPS     = cameraFPS
    self.old_time = self.clock()
    print("Camera setup")

  @staticmethod
  def draw_str(dst, target, str):
    x, y = target
    cv2.putText(dst, str, (x+1, y+1), cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 0), thickness = 2, lineType=cv2.LINE_AA)
    cv2.putText(dst, str, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.0, (255, 255, 255), lineType=cv2.LINE_AA)
  @staticmethod
  def clock():
    return cv2.getTickCount() / cv2.getTickFrequency()
   
  def get_image(self):
    sucess, image = self.cap.read()
    if not sucess:      #error
      raise ValueError("do not get image")
    return image
  
  def set_image(self):
    self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,  self.cameraWidth)
    self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.cameraHieght)
    self.cap.set(cv2.CAP_PROP_FPS, self.camerFPS)

  def show_info(self, mode : int):
    image = self.get_image()
    Frame_time = 1000 / ((self.clock() - self.old_time) * 1000.)
    self.old_time = self.clock()

    if mode == 1:
        self.draw_str(image, (5, 20), str(self.cameraWidth) + " x " + str(self.cameraHieght) + ' = FPS %.1f ' % (Frame_time))
        cv2.imshow('Video Test', image)
    else:
        print(" " + str(self.cameraWidth) + " x " + str(self.cameraHieght) + " = FPS %.1f " % (Frame_time))
 

if __name__ == "__main__":
  camera1 = Camera(0, 1280, 300, 60)

  camera1.set_image()
  while True:
    mode = 1
    camera1.show_info(mode)
    key = 0xFF & cv2.waitKey(1)
    if key == 27:  # ESC  Key
      break
    elif key == ord(' '):  # spacebar Key
      if mode == 0:
        mode = 1
      else:
        mode = 0 