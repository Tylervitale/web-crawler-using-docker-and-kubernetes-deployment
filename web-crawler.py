import requests
from bs4 import BeautifulSoup
import boto3


def web_crawler(url):
    # Make a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract the data you're interested in (e.g. the text of all <p> tags)
    data = [p.text for p in soup.find_all("p") if "winner" in p.text]

    # Store the data in a file or database
    with open("data.txt", "w") as f:
        for item in data:
            f.write(item + "\n")


def store_data_in_s3(data):
    # Create an S3 client
    s3 = boto3.client("s3")

    # Upload the data to the S3 bucket
    s3.put_object(Bucket="my-bucket", Key="data.txt", Body=data)


def process_data():
    with open("data.txt", "r") as f:
        data = f.read()
        store_data_in_s3(data)


def main():
    # Start the web crawler by passing in a URL
    web_crawler("https://www.aarweb.org/AARMBR/About-AAR-/Award-Programs-/Awards/Journalism-Award-Winners-and-Sample"
                "-Articles.aspx")
    process_data()


if __name__ == '__main__':
    main()
