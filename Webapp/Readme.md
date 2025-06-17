### Why Docker?

I used Docker to containerize my web application by creating a Docker image, which was then deployed to the EKS cluster. This ensured consistency across environments and streamlined the deployment process. I implemented a multi-stage Dockerfile—where the first stage installs all required dependencies, and the second stage uses a distroless image. This approach significantly reduces the image size and enhances security by minimizing the container’s attack surface, as it includes only the essential binaries.

### Brief Description of Project Files

- Dockerfile -> Contains the main set of instructions executed sequentially to build the Docker image. It incorporates the core Python application along with its dependencies.
- gandalf.py -> The main application code written in Python, utilizing Flask as the web server due to its lightweight and minimal setup requirements.
- requirements.txt -> Specifies all the Python libraries and dependencies needed for the application to run properly.

### Commands used for set-up

#### Containerization application with docker 
```
Docker build -t <ECR Repo Name>:latest .
```

#### For pushing the created image to ECR
```
Docker push <ECR Repo Name>
```
