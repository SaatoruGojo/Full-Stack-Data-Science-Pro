from selenium import webdriver
from selenium.webdriver.chrome.service import Service  
from webdriver_manager.chrome import ChromeDriverManager  
from selenium.webdriver.common.by import By  
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import urllib.parse
from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/scrape',methods=['POST'])
def scrape():
    query = request.form['product_name']

    # Encode the product name for URL (replace spaces, special characters, etc.)
    encoded_query = urllib.parse.quote(query)

    # Build the Flipkart search URL with the encoded product name
    base_url = "https://www.flipkart.com/search?q=" + encoded_query

    # Initialize a Chrome WebDriver using the webdriver manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Navigate to the Flipkart search page for the specified product
    driver.get(base_url)
    driver.implicitly_wait(10)

    # Initialize an empty list to store scraped reviews
    all_reviews = []

    visited_names = set()  # Set to store visited names
    index = 0  # Initialize an index counter

    while index<10:
         # Get the product links on each iteration to avoid StaleElementReferenceException
        product_links = driver.find_elements(By.XPATH, "//a[@class='_1fQZEK']")
        
        # Get the product URL
        product_url = product_links[index].get_attribute("href")

        # Open the product page
        driver.get(product_url)

        # Explicitly wait for the reviews container to be present (adjust the timeout as needed)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='_16PBlm']")))

        # Scrape reviews
        product_com = driver.find_elements(By.XPATH, "//div[@class='_16PBlm']")


        # Initialize a counter to keep track of the number of reviews for the current product
        review_counter = 0

        # Loop through each review container in the product page
        for product_coms in product_com:
            # Extract elements for name, rating, header, and comment from the review container
            name_elem = product_coms.find_element(By.XPATH, ".//p[@class='_2sc7ZR _2V5EHH']")
            rating_elem = product_coms.find_element(By.XPATH, ".//div[@class='_3LWZlK _1BLPMq']")
            header_elem = product_coms.find_element(By.XPATH, ".//p[@class='_2-N8zT']")
            comment_elem = product_coms.find_element(By.XPATH, ".//div[@class='']")

            # Extract text content from the elements
            name = name_elem.text
            rating = rating_elem.text
            comment_header = header_elem.text
            comment = comment_elem.text
            # Remove "READ MORE" and strip extra spaces from the comment
            comment = comment.split("READ MORE")[0].strip()

            # Check if the name is not in the visited names set
            if name not in visited_names:
                    # Create a dictionary for each review
                mydict = {
                    'name': name,
                    'rating': rating,
                    'comment_header': comment_header,
                    'comment': comment
                }
                print(mydict)

                    # Append the dictionary to the list
                all_reviews.append(mydict)

                    # Add the name to the visited names set
                visited_names.add(name)

                review_counter += 1

                    # Break out of the loop if maximum reviews (5) reached
                if review_counter >= 5:
                    break
        
        # Navigate back to the previous page using the browser's back button
        driver.back()
        # Increment the index to move on to the next product in the search results
        index += 1
    return render_template('result.html', data=all_reviews,query = query)



if __name__ == '__main__':
    app.run(debug=True,host = '0.0.0.0')
