
import tensorflow as tf
from django.views.decorators.csrf import csrf_exempt
import os
from PIL import Image
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
import hashlib
import re
import requests as req
import PIL
import numpy as np
import shutil
import PIL.Image


# Create your views here.


def index(request):
    return render(request, 'illusion/index.html')


from . import utils
from . import style_transfer_tester
#import time


"""main"""
def run_test(content_img, transfer_img,style_model):
    tf.reset_default_graph()

    # load content image
    #start_time = time.time()
    content_image = utils.load_image(content_img)

    # open session
    soft_config = tf.ConfigProto(allow_soft_placement=True)
    soft_config.gpu_options.allow_growth = True # to deal with large image
    sess = tf.Session(config=soft_config)

    # build the graph
    transformer = style_transfer_tester.StyleTransferTester(session=sess,                                                                                   # 체크ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
                                                            model_path=style_model,
                                                            content_image=content_image,
                                                            )
    # execute the graph

    output_image = transformer.test()                                                                                                                      # 체크ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    del transformer

    # save result
    utils.save_image(output_image, transfer_img)
    #end_time = time.time()
    # report execution time
    shape = content_image.shape #(batch, width, height, channel)
    #print('Execution time for a %d x %d image : %f msec' % (shape[0], shape[1], 1000.*float(end_time - start_time)/60))
    print('Transfer finished for a %d x %d image.' % (shape[0], shape[1])


#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ^




def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error:Creating directory.' + directory)



@csrf_exempt
def preview(request, style_id, url):
    if style_id is None:
        return HttpResponseBadRequest()
    if url is None:
        return HttpResponseBadRequest()

    """
    STEP 0   : Preview 찾기
    STEP 1-1 : content_img 찾기
               or
         1-2 : content_img 다운로드
    STEP 2   : preview 생성
    STEP 3   : 이미지 return
    """
    # if re.search("photos", url) is None:
    #     url = re.sub("/filter/", "/photos /", url)
    # else :
    #     url = re.sub("/photos/", "/photos /", url)
    if re.search("photos", url) is not None:
        url = re.sub("/photos/", "/photos /", url)
    else:
        return HttpResponseBadRequest()

    url = url.split(" ")
    url[1] = re.sub("/", "%2F", url[1])
    url = "".join(url)


    a=request.GET.get('alt')
    b=request.GET.get('token')

    url = url+"?alt={alt}&token={token}".format(alt=a, token=b)


    filename_md5 = hashlib.md5(url.encode('utf-8')).hexdigest().upper() # url을 md5로 축약 -> 파일명으로 사용
    directory = 'preview/{}'.format(filename_md5)
    preview_content_img = 'preview/{}/{}.jpg'.format(filename_md5, filename_md5) # 미리보기 할 컨텐츠 이미지
    preview_img = 'preview/{}/{}_{}.jpg'.format(filename_md5, filename_md5,style_id) # 이미지 축소 후 transfer 된 이미지
    style_model = 'models/{}.ckpt'.format(style_id) # 모델링 돌릴 스타일의 모델


    #preview_img가 있는지 확인하고 있으면 리턴
    # STEP 0
    if os.path.exists(preview_img):
    # STEP 3
        try:
            with open(preview_img, "rb") as f:
                return HttpResponse(f.read(), content_type="image/jpg")
        except IOError:
            red = Image.new('RGBA', (1, 1), (255, 0, 0, 0))
            response = HttpResponse(content_type="image/jpeg")
            red.save(response, "JPEG")
            return response


    # preview_img가 없으면, preview_content_img가 있는지 확인하고
    # 있으면 모델링을 돌리고 해당 이미지를 리턴
    # STEP 1-1
    elif os.path.exists(preview_content_img):
    # STEP 2
        run_test(preview_content_img, preview_img, style_model)
    #     subprocess.call(
    #         ['python', 'illusion/run_test.py', '--content', preview_content_img, '--style_model',
    #          style_model, '--output', preview_img]) # 쉘로 명령어 입력해서 style transfer 진행
    # STEP 3
        try:
            with open(preview_img, "rb") as f: # transfer 된 결과물을 열어서 리턴
                return HttpResponse(f.read(), content_type="image/jpg")
        except IOError:
            red = Image.new('RGBA', (1, 1), (255, 0, 0, 0))
            response = HttpResponse(content_type="image/jpeg")
            red.save(response, "JPEG")
            return response

    # preview_content_img가 없으면 url을 통해서 이미지다운받고 모델링 돌리고 해당 이미지 리턴
    # STEP 1-2
    else:
        # 폴더생성
        resp = req.get(url, stream=True)
        if not resp:
            return HttpResponseBadRequest()
        createFolder(directory)




        # Open the url image, set stream to True, this will return the stream content.


        # Open a local file with wb ( write binary ) permission.
        local_file = open(preview_content_img, 'wb')
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        resp.raw.decode_content = True
        # Copy the response stream raw data to local image file.
        shutil.copyfileobj(resp.raw, local_file)
        del resp
        local_file.close()



        #resize
        image = Image.open(preview_content_img)
        factor = float(512) / np.max(image.size)
        size = np.array(image.size) * factor
        size = size.astype(int)
        image = image.resize(size, PIL.Image.LANCZOS)
        image.save(preview_content_img)

    # STEP 2
        run_test(preview_content_img, preview_img, style_model)
    #     subprocess.call(
    #         ['python', 'illusion/run_test.py', '--content', preview_content_img, '--style_model',
    #          style_model, '--output', preview_img]) # 쉘로 명령어 입력해서 style transfer 진행
    # STEP 3
        try:
            with open(preview_img, "rb") as f: # transfer 된 결과물을 열어서 리턴
                return HttpResponse(f.read(), content_type="image/jpg")
        except IOError:
            red = Image.new('RGBA', (1, 1), (255, 0, 0, 0))
            response = HttpResponse(content_type="image/jpeg")
            red.save(response, "JPEG")
            return response


# 스타일 선택 페이지에서 "확인" 버튼 누르면 실행되는 최종함수

@csrf_exempt
def transfer(request, style_id, url):
    if style_id is None:
        return HttpResponseBadRequest()
    if url is None:
        return HttpResponseBadRequest()
    """
    STEP 0   : Transfer 찾기
    STEP 1-1 : content_img 찾기
               or
         1-2 : content_img 다운로드
    STEP 2   : transfer 생성
    STEP 3   : 이미지 return
    """


    if re.search("photos", url) is not None:
        url = re.sub("/photos/", "/photos /", url)
    else:
        return HttpResponseBadRequest()
    # if re.search("photos", url) is None:
    #     url = re.sub("/filter/", "/photos /", url)
    # else :
    #     url = re.sub("/photos/", "/photos /", url)

    url = url.split(" ")
    url[1] = re.sub("/", "%2F", url[1])
    url = "".join(url)

    a=request.GET.get('alt')
    b=request.GET.get('token')

    url = url+"?alt={alt}&token={token}".format(alt=a, token=b)

    filename_md5 = hashlib.md5(url.encode('utf-8')).hexdigest().upper()  # url을 md5로 축약 -> 파일명으로 사용
    directory = 'transfer/{}'.format(filename_md5)
    content_img = 'transfer/{}/{}.jpg'.format(filename_md5, filename_md5) # transfer 할 컨텐츠 이미지
    transfer_img = 'transfer/{}/{}_{}.jpg'.format(filename_md5, filename_md5,style_id) # transfer 된 이미지
    style_model = 'models/{}.ckpt'.format(style_id) # 모델링 돌릴 스타일의 모델

    # transfer_img가 있는지 확인하고 있으면 리턴
    # STEP 0
    if os.path.exists(transfer_img):
    # STEP 3
        try:
            with open(transfer_img, "rb") as f:
                return HttpResponse(f.read(), content_type="image/jpg")
        except IOError:
            red = Image.new('RGBA', (1, 1), (255, 0, 0, 0))
            response = HttpResponse(content_type="image/jpeg")
            red.save(response, "JPEG")
            return response

    # transfer_img가 없으면, content_img가 있는지 확인하고 있으면 모델링을 돌리고 해당 이미지를 리턴
    # STEP 1-1
    elif os.path.exists(content_img):
    # STEP 2
        run_test(content_img, transfer_img,style_model)
    #     subprocess.call(
    #         ['python', 'illusion/run_test.py', '--content', content_img, '--style_model',
    #          style_model, '--output', transfer_img]) # 쉘로 명령어 입력해서 style transfer 진행
    # STEP 3
        try:
            with open(transfer_img, "rb") as f: # transfer 된 결과물을 열어서 리턴
                return HttpResponse(f.read(), content_type="image/jpg")
        except IOError:
            red = Image.new('RGBA', (1, 1), (255, 0, 0, 0))
            response = HttpResponse(content_type="image/jpeg")
            red.save(response, "JPEG")
            return response


    # content_img가 없으면 url을 통해서 다운받고 모델링 돌리고 해당 이미지 리턴
    # STEP 1-2
    else:
        # 폴더생성
        resp = req.get(url, stream=True)
        if not resp:
            return HttpResponseBadRequest()
        createFolder(directory)


        # Open the url image, set stream to True, this will return the stream content.

        # Open a local file with wb ( write binary ) permission.
        local_file = open(content_img, 'wb')
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        resp.raw.decode_content = True
        # Copy the response stream raw data to local image file.
        shutil.copyfileobj(resp.raw, local_file)
        del resp
        local_file.close()

    # STEP 2
        run_test(content_img, transfer_img, style_model)
    #     subprocess.call(
    #         ['python', 'illusion/run_test.py', '--content', content_img, '--style_model',
    #          style_model, '--output', transfer_img]) # 쉘로 명령어 입력해서 style transfer 진행
    # STEP 3
        try:
            with open(transfer_img, "rb") as f: # transfer 된 결과물을 열어서 리턴
                return HttpResponse(f.read(), content_type="image/jpg")
        except IOError:
            red = Image.new('RGBA', (1, 1), (255, 0, 0, 0))
            response = HttpResponse(content_type="image/jpeg")
            red.save(response, "JPEG")
            return response
