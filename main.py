import cv2
import numpy as np

def hex_to_bgr(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (4, 2, 0))

colors = {
    'land zone': '#4d71db',   
    'drop zone': '#d1956c',
    'bucket': '#d15b60',     
    'white_circle': '#c0c3c7'
}

img = cv2.imread('assets.png')
if img is None:
    raise ValueError("Gambar tidak ditemukan. Pastikan path 'input.jpg' benar.")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
output = img.copy()

def detect_color_shape(mask, label=None, draw_cross=False, color_bgr=(255,255,255)):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        min_area = 2000 if label == 'land zone' else 300
        if area < min_area:
            continue
        approx = cv2.approxPolyDP(cnt, 0.04 * cv2.arcLength(cnt, True), True)
        (x, y, w, h) = cv2.boundingRect(approx)
        center = (x + w//2, y + h//2)

        if len(approx) >= 8:
            cv2.circle(output, center, w//2, color_bgr, 2)
            if draw_cross:
                cv2.line(output, (center[0]-5, center[1]), (center[0]+5, center[1]), color_bgr, 2)
                cv2.line(output, (center[0], center[1]-5), (center[0], center[1]+5), color_bgr, 2)
            if label:
                cv2.putText(output, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color_bgr, 2)
        elif 4 <= len(approx) <= 6: 
            cv2.rectangle(output, (x, y), (x+w, y+h), color_bgr, 2)
            if label:
                cv2.putText(output, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color_bgr, 2)

for label, hex_color in colors.items():
    bgr = np.uint8([[hex_to_bgr(hex_color)]])
    hsv_color = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)[0][0]
    
    lower = np.array([max(0, hsv_color[0]-10), 50, 50])
    upper = np.array([min(179, hsv_color[0]+10), 255, 255])
    
    if label == 'land zone':
        lower = np.array([hsv_color[0]-5, 100, 100])
        upper = np.array([hsv_color[0]+5, 255, 255])
    
    mask = cv2.inRange(hsv, lower, upper)
    
    if label == 'land zone':
        detect_color_shape(mask, label='land zone',draw_cross=True, color_bgr=(0, 255, 0))
    elif label == 'drop zone':
        detect_color_shape(mask, label='drop zone',draw_cross=True, color_bgr=(0, 255, 0))
    elif label == 'bucket':
        detect_color_shape(mask, label='bucket', draw_cross=True, color_bgr=(0, 255, 0))
    elif label == 'white_circle':
        lower = np.array([0, 0, 180])
        upper = np.array([180, 50, 255])
        mask = cv2.inRange(hsv, lower, upper)
        detect_color_shape(mask, draw_cross=True, color_bgr=(0, 0, 255))

cv2.imshow("Detected Zones", output)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("output_detected.jpg", output)
