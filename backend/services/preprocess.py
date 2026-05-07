import cv2

def preprocess_image(path):

    image = cv2.imread(path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    thresh = cv2.threshold(
        gray,
        150,
        255,
        cv2.THRESH_BINARY
    )[1]

    processed_path = "processed/processed.png"

    cv2.imwrite(processed_path, thresh)

    return processed_path