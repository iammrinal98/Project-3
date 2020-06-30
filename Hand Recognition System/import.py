import cv2 
import numpy as np 
  
cap = cv2.VideoCapture(0) 
hand_cascade = cv2.CascadeClassifier('hand.xml')