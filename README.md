## Demonstration of ML Model deployment on Kubernetes platform

-  Model Training
-  Building the Model locally
-  API Deployment with FastAPI
-  Dockerization
-  Kubernetes Deployment

### Setup Environment and install dependencies
``` bash
python3 -m venv .mlops-kubernetes  (. to keep venv in hidden   environment)
.\.mlops-kubernetes\Scripts\Activate.ps1   
pip install -r requirements.txt
```
### Training the model
``` bash
python model_train.py
```
### Building FastAPI Application for user interaction
``` bash
uvicorn main:app --reload   ( model pkl is placed in software application)
``` 
`Uvicorn running on http://127.0.0.1:8000`
`this will print {"message":"Diabetes Prediction API is live"} `

### Test the model with user input (Model Evaluation)
- http://127.0.0.1:8000/docs  under POST section, Try it out, expand application/json drop down to access input features. Give values and click on Execute

### Dockerization and deploy in local machine

- Create Dockerfile
- validate Dockerfile (if it throws error in windows, in start search  Docker Desktop, wait till docker engine starts)
``` bash
docker ps
docker build -t diabetes-randomforest-model-demo .
# test the docker image by running
docker images # to see whether docker image is created
docker run -p 8000:8000 diabetes-randomforest-model-demo
# if linux click on the http link otherwise on windows in the browser http://localhost:8000/ : This shows the message as {"message":"Diabetes Prediction API is live"}  and test the same way as local deployment http://localhost:8000/docs
```

### Deployment on Kubernetes 
- create cluster using kind command
``` bash
kind create cluster --name=demo-mlops  # creates single node cluster
# For windows follow this
# Invoke-WebRequest "https://kind.sigs.k8s.io/dl/v0.24.0/kind-windows-amd64" -OutFile "kind.exe"
# Move-Item .\kind.exe "C:\Windows\System32\kind.exe"

# tag  docker image and then push to docker hub
docker images # shows REPOSITORY TAG IMAGE ID CREATED SIZE (we need IMAGE ID for demo image )
docker tag 2e18780fe029 jayk8s/diabetes-randomforest-model-demo:v1
docker login -u username
docker push  jayk8s/diabetes-randomforest-model-demo:v1 # (if fails login to docker hub with same username and create a repo jayk8s/diabetes-randomforest-model-demo)  this will create pod and service
kubectl apply -f deploy.yml


# to know the status
kubectl get pods -w  # containers will be created
kubectl get svc  # run this command after api service is in running status , to view api-service name cluser ip 
kubectl port-forward svc/diabetes-api-service 1111:80  --address=0.0.0.0
localhost:1111/docs
```
