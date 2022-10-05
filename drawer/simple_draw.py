import cv2

def add_text(image_rbg, text):
    
    org = (0, 950)
    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 5
    color = (255,255,255)
    thickness = 10
    lineType = cv2.LINE_AA

    # adjust according to text length
    if len(text) < 10:
        fontScale = 5
        org = (200, 950)
    elif len(text) < 20:
        fontScale = 3
        org = (100, 950)
    elif len(text) < 30:
        fontScale = 2
        org = (5, 950)
    elif len(text) < 40:
        fontScale = 2
        org = (5, 950)
    else:
        fontScale = 2
        org = (5, 950)

    # covert to correct format for cv2.putText
    image_bgr = cv2.cvtColor(image_rbg, cv2.COLOR_RGB2BGR)

    image_drawn = cv2.putText(image_bgr, text, org, fontFace, fontScale, 
                 color, thickness, lineType, False)

    # to RGB
    image_drawn = image_drawn[:, :, [2, 1, 0]]
    return image_drawn