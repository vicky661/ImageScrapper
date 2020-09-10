
from flask_cors import cross_origin
from imagescrapperservice.ImageScrapperService import ImageScrapperService
from flask import Flask, render_template, request
from selenium import webdriver

app = Flask(__name__)

@app.route('/', methods = ['GET'])  # route for redirecting to the home page
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/showImages',methods = ['POST']) # route to show the images on a webpage
@cross_origin()
def show_images():
    if request.method == 'POST':
        print("entered post")
        keyWord = request.form['keyword']
    else:
        print("did not enter post")
    print('printing = ' + keyWord)

    image_name = keyWord.split()
    image_name = '+'.join(image_name)

    DRIVER_PATH = 'chromedriver.exe'

    service = ImageScrapperService()  # instantiating the object of class ImageScrapperService
    # (imageURLList, header, keyWord, fileLoc)
    with webdriver.Chrome(executable_path=DRIVER_PATH) as wd:
        image_urls = service.downloadImages(keyWord, wd)

    try:
        if(len(image_urls)>0): # if there are images present, show them on a wen UI
            print(image_urls[0])
            return render_template('showImage.html', urls=image_urls)
        else:
            return "Please try with a different string" # show this error message if no images are present in the static folder
    except Exception as e:
        print('no Images found ', e)
        return "Please try with a different string"

if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=5000, debug = True) # port to run on local machine
    #app.run(debug=True) # to run on cloud
    app.run(debug = True)