import math
from ultralytics import YOLO
import cv2

cap = cv2.VideoCapture(0)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width, frame_height))

model = YOLO("../YOLO-Weights/yolov8n.pt")
class_names = [
    "person",
    "apple",
    "banana",
    "water bottle",
    "carrot",
    "tomato",
    "potato",
    "onion",
    "lettuce",
    "cucumber",
    "grape",
    "orange",
    "lemon",
    "lime",
    "watermelon",
    "peach",
    "strawberry",
    "blueberry",
    "raspberry",
    "mango",
    "pear",
    "cherry",
    "bell pepper",
    "broccoli",
    "spinach",
    "mushroom",
    "corn",
    "peas",
    "pumpkin",
    "sweet potato",
    "zucchini",
    "garlic",
    "ginger",
    "kiwi",
    "pineapple",
    "nectarine"
]

while True:
    success, img =cap.read()
    # out.write(img)
    results=model(img,stream=True)
    for r in results:
        boxes=r.boxes
        for box in boxes:
            x1,y1,x2,y2=box.xyxy[0]
            x1,y1,x2,y2=int(x1),int(y1),int(x2),int(y2)
            print(x1,y1,x2,y2)
            cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)  
            conf=math.ceil((box.conf[0]*100))/100
            cls=int(box.cls[0])
            print("//")
            print(cls)
            class_name= class_names[cls] 
            label=f'{class_name} {conf}'
            t_size=cv2.getTextSize(label,0,fontScale=1,thickness=2)[0]
            print(t_size)
            c2=x1+t_size[0],y1 - t_size[1] - 3
            cv2.rectangle(img,(x1,y1),c2,[255,0,255],-1,cv2.LINE_AA)    #filled

            cv2.putText(img,label,(x1,y1-2),0, 1,[255,255,255], thickness=1,lineType=cv2.LINE_AA)
    out.write(img)
    cv2.imshow("Image",img)
    if cv2.waitKey(1) ==ord("q"):
        break
out.release()