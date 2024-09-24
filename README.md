
# Home Price Prediction ML App

## 1. Overview
This is a Flask-based machine learning application that predicts home prices based on features like square footage, number of bedrooms, and number of bathrooms. The app allows users to input these details via a simple UI and receive a predicted home price. The backend uses a pre-trained machine learning model for predictions. The app is containerized using Docker and deployed on Google Cloud with auto-scaling enabled.


## 2. Tech Stack

**Backend:** Flask (Python)

**Frontend:** HTML, CSS, jQuery

**Machine Learning:** scikit-learn, joblib

**Deployment:** Docker, Google Cloud (Container Registry, Instance Groups, Auto-scaling)


## 3. Requirements


- Python 3.8+ installed on your local machine.
- Docker installed for containerization.
- Google Cloud SDK installed and configured (gcloud auth login).

To run this project, the following dependencies are required. These are listed in the [requirements.txt]() file​ 

- Flask==3.0.3
- scikit-learn==1.5.1
- pandas==2.2.3
- joblib==1.4.2
- gunicorn==23.0.0

#### Install the dependencies using pip

```pip install -r requirements.txt```


## 4. Setup Instructions

### Local Development Setup

#### Clone the repository:

```git clone <repository-url>
cd <project-folder>
```

#### Set up a virtual environment:

```python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

#### Install dependencies:
```
pip install -r requirements.txt
```

#### Run the Flask app locally:
```
flask run
```

#### Access the app at: ```http://127.0.0.1:8000```

## 5. Building the Docker Image

### Build the Docker image:
```
docker build -t my-ml-app .
```
### Run the Docker container locally:
```
docker run -p 8000:8000 my-ml-app
```



    

## 6. Google Cloud Deployment

### Pushing the Docker Image to Google Cloud
#### Authenticate to Google Cloud:
```
gcloud auth configure-docker

```

#### Tag your Docker image for Google Container Registry:
```
docker tag my-ml-app gcr.io/<your-project-id>/my-ml-app:latest
```

#### Push the image to Google Cloud:

``` 
docker push gcr.io/<your-project-id>/my-ml-app:latest
```



## API Reference

#### Post Query

```http
  POST /predict
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `square_footage`      | `int` | **Required**. Id of item to fetch |
| `bedrooms`      | `int` | **Required**. Id of item to fetch |
| `bathrooms`      | `int` | **Required**. Id of item to fetch |




