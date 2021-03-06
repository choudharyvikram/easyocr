# import the necessary packages
from easyocr import Reader
import cv2


def cleanup_text(text):
    # strip out non-ASCII text so we can draw the text on the image
    # using OpenCV
    return "".join([c if ord(c) < 128 else "" for c in text]).strip()


def ocr_image(image_path, langs='en', gpu=-1):
    # break the input languages into a comma separated list
    langs = langs.split(",")
    print("[INFO] OCR'ing with the following languages: {}".format(langs))
    # load the input image from disk
    image = cv2.imread(image_path)
    # OCR the input image using EasyOCR
    print("[INFO] OCR'ing input image...")
    reader = Reader(langs, gpu=gpu > 0)
    results = reader.readtext(image)

    all_text = ''
    # loop over the results
    for (bbox, text, prob) in results:
        # display the OCR'd text and associated probability
        print("[INFO] {:.4f}: {}".format(prob, text))
        # unpack the bounding box
        (tl, tr, br, bl) = bbox
        tl = (int(tl[0]), int(tl[1]))
        tr = (int(tr[0]), int(tr[1]))
        br = (int(br[0]), int(br[1]))
        bl = (int(bl[0]), int(bl[1]))
        # cleanup the text and draw the box surrounding the text along
        # with the OCR'd text itself
        text = cleanup_text(text)
        cv2.rectangle(image, tl, br, (0, 255, 0), 2)
        cv2.putText(image, text, (tl[0], tl[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        all_text += ' ' + text

    # resize image for UI purpose
    h, w, _ = image.shape

    # image = cv2.resize(image, (700, 700))
    return image, all_text