# Introduction to Docker

Docker is a powerful tool for automating the deployment of applications inside lightweight, portable containers. These containers can run on any machine that has Docker installed, providing consistency across development, testing, and production environments. This tutorial will offer basic instructions on how to use Docker.

# Description of this demo
This demo showcases a guessing number website, where the frontend displays an interactive user interface, and the backend validates the number entered by the user. Users will attempt to guess a number between 1 and 100.

# Instructions
1. Download Docker
2. Clone this repo
3. docker compose up --build
4. Enter your IP address in browser


# Key Docker Concepts:

1. **Dockerfile:**

   - A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image.
   - It serves as the blueprint for creating Docker images.
   - Dockerfile includes instructions to build an image layer by layer.

2. **docker run:**

   - Docker run is the command used to create and start containers based on a Docker image.
   - It can be customized with various options such as port mappings, volume mounts, environment variables, and more.

3. **docker pull:**

   - Docker pull is the command used to download Docker images from a registry.
   - If an image is not available locally, Docker pull fetches it from the registry specified and stores it on the local system.

4. **docker push:**

   - Docker push is the command used to push Docker images to a registry.
   - It allows users to share their custom-built images with others or deploy them to production environments.

5. **docker build:**
   - Docker build is the command used to build a Docker image from a Dockerfile.
   - It reads the instructions from the Dockerfile and executes them in order to create the image.

## Advantages of Docker:

- **Portability:** Docker containers can run on any machine with Docker installed, providing consistency across different environments.
- **Isolation:** Containers isolate applications from each other and the underlying system, ensuring that they run independently without interfering with one another.
- **Efficiency:** Docker containers are lightweight and share the host system's kernel, resulting in fast startup times and efficient resource utilization.
- **Scalability:** Docker's container-based architecture makes it easy to scale applications up or down based on demand.

## Getting Started:

1. Install Docker on your system from the [official Docker website](https://www.docker.com/get-started).
2. Explore [Docker Hub](https://hub.docker.com/) to discover pre-built images and repositories shared by the community.
3. Experiment with Docker commands like `docker run`, `docker build`, `docker pull`, and `docker push` to familiarize yourself with Docker's workflow.
4. Checkout Docker Docs (https://docs.docker.com/manuals/) for comprehensive information.
