# News_Type_Classification

## Steps To Run The App

'Clone the repo & cd into it'

>> 1. git clone https://github.com/Swapnadeep1998/News_Type_Classification.git

>> 2. cd News_Type_classification/

"Build the Docker image"

>> 3. sudo docker build -t news_classification .

"Run the image as a container"

>> 4. sudo docker run -p 8000:8000 news_classification

"Open the SWAGGER UI in browser"

>> 5. http://0.0.0.0:8000/docs
