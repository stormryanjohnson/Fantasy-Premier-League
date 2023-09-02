# Fantasy-Premier-League-Prediction-Service
## Overview

Fantasy Premier League (FPL) is a popular online fantasy football game with over 10 million active participants on a yearly basis. Users assemble virtual teams of real-life footballers and earn points based on their performances in actual Premier League matches. One crucial aspect of the game is player pricing, which gets set at the start of every season based on a footballer’s performance from the previous seasons. 

The FPL Price Prediction Service aims to help FPL managers gain insight into player prices before the start of the upcoming season. The Service uses information and statistics on footballers’ previous season in order to predict what their prices will be upon the official launch of the game. These predictions enable FPL managers to gain an edge in the game while planning their team selection for the upcoming season.

## Architecture and Dataflow

Below is a schematic of the basic architecture of this product. The illustration displays the end-to-end flow of data for the entire project - from the ingesting of footballer data from the FPL API to the input-output utility of the Prediction Service.
![FPL app.png](https://neat-second-89c.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F710c82c4-e98f-48ce-8b8d-21fbaf39d6e1%2FFPL_app.png?table=block&id=4848968f-8ca4-465f-a93e-d9cd98268f77&spaceId=31d99ce6-2ebb-4508-b1ae-bcae928c747e&width=2000&userId=&cache=v2)
The architecture consists of the following steps:
1. At the end of each Premier League season, the football player data for the season is transferred from the FPL API to a public [GitHub repository](https://github.com/vaastav/Fantasy-Premier-League).
2. The player data is transferred and used to locally develop the ML model with the assistance of [mlflow](https://mlflow.org/) for experiment monitoring and hyper-parameter tuning. An app is designed to serve the ML model through a local endpoint.
3. The app is containerised by creating a Dockerfile.
4. The app, model, Dockerfile and workflow details are pushed to a GitHub repository.
5. The CI/CD workflow is orchestrated through GitHub Actions, which ensures that whenever the deployment repository is updated, the changes will immediately begin integrating into the deployed endpoint hosted on Heroku. 
6. A basic frontend web interface was created with HTML to collect the input JSON data through an Heroku endpoint. Upon imputing the relevant fields, a POST request is sent via the Flask API.
7. Feature processing occurs in the backend, and the model produces an associated prediction of a player price which is returned in the form of an output JSON.

## Prediction Service Deployment
[FPL deployment](https://fplplayerpricepredictor-35659dcd2f3b.herokuapp.com/)

## Conclusion and Impact
- Designed and deployed a scalable machine learning model as a real-time predictions service with an average latency of 30 ms.
- Implemented a CI/CD workflow to ensure immediate model integration and deployment upon updates to the GitHub repository.

