#!/usr/bin/env python

import torch
import os
from pdf2image import convert_from_path
from PIL import Image
from transformers import LayoutLMv2FeatureExtractor
import pytesseract
from pdf2image import convert_from_path


def append_images(file_name:str):
    pil_image_lst = []
    pil_image_lst = convert_from_path(file_name)
    x,y = pil_image_lst[0].size
    tot_y = len(pil_image_lst) * y
    offset = 0
    merged_image = Image.new('RGB',(x, tot_y))
    min_list_len = min(2,len(pil_image_lst))
    for i in range(0, min_list_len):
        merged_image.paste(pil_image_lst[i],(0,offset))
        offset += y
    return merged_image


def extract_text_from_pdf(path_to_pdf: str) -> str:
    if not os.path.exists(path_to_pdf):
        raise Exception("File doesn't exist")
    
    ocr_text = ''
    images = convert_from_path(path_to_pdf)
    for i in range(0,1): #range(len(images)):    
        page_content = pytesseract.image_to_string(images[i])
        page_content = '***PDF Page {}***\n'.format(i+1) + page_content
        ocr_text = ocr_text + ' ' + page_content
    return ocr_text
    # feature_extractor = LayoutLMv2FeatureExtractor()
    # # get a batch of document images
    # img = append_images(path_to_pdf)  # "/home/ryang/repos/docvqa/bp/0001.pdf"
    # image = img.convert("RGB")

    # # resize every image to 224x224 + apply tesseract to get words + normalized boxes
    # encoding = feature_extractor(image)
    # return(','.join(str(item) for innerlist in encoding.words for item in innerlist))