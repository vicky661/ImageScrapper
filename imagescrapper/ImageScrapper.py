import time

class ImageScrapper:

    def createURL(self,keyWord):
        keyWord = keyWord.split()
        keyWord = '+'.join(keyWord)
        url = "https://www.google.co.in/search?q=" + keyWord + "&source=lnms&tbm=isch"
        return url
        # print (url)
        # add the directory for your image here

    # contains the link for Large original images, type of  image
    def getimageUrlList(self, url, wd, sleep_between_interactions, max_links=4):
        def scroll_to_end(wd):
            wd.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(sleep_between_interactions)

        wd.get(url)

        image_urls = []

        scroll_to_end(wd)
        thumbnail_results = wd.find_elements_by_css_selector('img.Q4LuWd')

        for img in thumbnail_results:
            try:
                if len(image_urls) < max_links:
                    img.click()
                    time.sleep(0.5)
                    actual_img = wd.find_element_by_css_selector('img.n3VNCb')
                    if actual_img.get_attribute('src'):
                        image_urls.append(img.get_attribute('src'))
                else:
                    break
            except Exception:
                continue
        return image_urls