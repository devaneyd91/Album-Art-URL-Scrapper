from selenium import webdriver
from selenium.webdriver.common.by import By
import time


PATH = r"D:\Code\drivers\chromedriver-win64(117)\chromedriver-win64\chromedriver.exe"


def accept_google_cookies(wd):
    try:
        # Locate the "Accept all" button by class name
        accept_button = wd.find_element(By.CLASS_NAME, "lssxud")

        # Click the "Accept all" button
        accept_button.click()
        print("Clicked the 'Accept all' button.")
    except Exception as e:
        print("Could not find or click the 'Accept all' button:", str(e))


loop = 1


def get_images_from_web(wd, loop):

    if loop == 1:
        search = 'https://www.listchallenges.com/1001-albums-you-must-hear-before-you-die-every'
        loop += 1
        wd.get(search)
    elif loop >= 2 and loop <= 28:
        search = 'https://www.listchallenges.com/1001-albums-you-must-hear-before-you-die-every/list/' + \
            str(loop)
        loop += 1
        wd.get(search)

    # Find all divs with class 'item-image-wrapper'
    image_wrappers = wd.find_elements(By.CLASS_NAME, 'item-image-wrapper')

    image_data = []
    count = 0
    pages = 1

    for image_wrapper in image_wrappers:

        # Find the img element within each 'item-image-wrapper' div
        image = image_wrapper.find_element(By.TAG_NAME, 'img')

        # Get the source (src) attribute of the img tag
        if image.get_attribute('src') and 'http' in image.get_attribute('src'):
            time.sleep(delay)
            url = image.get_attribute('src')

        # Get the alt attribute text of the img tag
        album_name = image.get_attribute('alt')
        count += 1
        #add_to_database(album_name, url)

        if count == 40 and pages < 28:
            count = 0
            get_images_from_web(wd, loop)

        elif count == 40 and pages == 28:
            break

        # Append the src and alt_text to the image_data list
        image_data.append({'src': url, 'alt_text': album_name})

    return image_data


if __name__ == "__main__":
    # Initialize the webdriver 
    wd = webdriver.Chrome(PATH)

    # Set an optional delay
    delay = 5

    # Get image data from the web page
    image_data = get_images_from_web(wd, loop)

    # Print the image data
    for i, data in enumerate(image_data, start=1):
        print(
            f"Image {i} - Source: {data['src']}, Alt Text: {data['alt_text']}")

    # Close the webdriver
    wd.quit()
