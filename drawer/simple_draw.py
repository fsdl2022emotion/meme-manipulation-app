import cv2

def add_text(image_rbg, text):
    width = image_rbg.shape[1]
    height = image_rbg.shape[0]

    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    color = (255,255,255)
    thickness = 15
    lineType = cv2.LINE_AA

    # adjust according to text length
    if len(text) < 10:
        fontScale = 5
        org = (int(width/2 - 200), int(height/10*9 + 100))
    elif len(text) < 20:
        fontScale = 3
        org = (int(width/2 - 300), int(height/10*9 + 100))
    else:
        fontScale = 2
        org = (int(width/2 - 400), int(height/10*9 + 100))


    # covert to correct format for cv2.putText
    image_bgr = cv2.cvtColor(image_rbg, cv2.COLOR_RGB2BGR)

    image_drawn = cv2.putText(image_bgr, text, org, fontFace, fontScale, 
                 color, thickness, lineType, False)

    # to RGB
    image_drawn = image_drawn[:, :, [2, 1, 0]]
    return image_drawn