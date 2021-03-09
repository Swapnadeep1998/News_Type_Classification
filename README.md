# News_Type_Classification

## Steps To Run The App

>> 1. Clone the repo & cd into it

`git clone https://github.com/Swapnadeep1998/News_Type_Classification.git`

`cd News_Type_classification/`

>> 2. Build the Docker image

`sudo docker build -t news_classification .`

>> 3. Run the image as a container

`sudo docker run -p 8000:8000 news_classification`

>> 4. Open the SWAGGER UI in browser

http://0.0.0.0:8000/docs
