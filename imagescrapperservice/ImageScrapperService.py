from imagescrapper.ImageScrapper import ImageScrapper

class ImageScrapperService:

    imgScrapper = ImageScrapper
    keyWord = ""
    fileLoc = ""
    image_name = ""
    header = ""

    def downloadImages(self,keyWord, web_driver):
        imgScrapper = ImageScrapper()
        url = imgScrapper.createURL(keyWord)

        imageURLList = imgScrapper.getimageUrlList(url,web_driver,0.5)
        
        return imageURLList