## Deployment 

The YAML file `docker.yaml` is a GitHub Actions workflow that automates the process of building a Docker image and deploying it to Google Cloud Run. Here's a detailed explanation of each step:

<ol>
 <li><code><b>Workflow Name</b></code>: The <code>name: Build and Deploy to Google Cloud Run</code> line names the workflow.

```yaml
name: Build and Deploy to Google Cloud Run
```
 </li>
 <li><code><b>Trigger</b></code>:The <code>on: push: branches: [ main ] </code>lines specify that this workflow should be triggered when changes are pushed to the <code>main</code> branch.

```yaml
on:
  push:
    branches: [ main ]
```
 <li><code><b>Checkout Code</b></code>: This step uses the <code>actions/checkout@v4 </code>action to clone the code from the GitHub repository into the runner's workspace. This makes the code available for the subsequent steps in the workflow.</li>

```bash
- name: Checkout code
  uses: actions/checkout@v4
```
  <li><code><b>Authenticate to Google Cloud</b></code>: This step uses the <code>google-github-actions/auth@v2</code>action to authenticate to Google Cloud. It uses a service account key stored in the <code>GCP_SA_KEY</code> secret. This secret is set in the GitHub repository's settings.</li>

```bash
- name: Authenticate to Google Cloud
  uses: google-github-actions/auth@v2
  with:
    credentials_json: ${{ secrets.GCP_SA_KEY }}
```
 <li><code><b>Set up Cloud SDK</b></code>: This step uses the <code>google-github-actions/setup-gcloud@v2 </code>action to set up the Google Cloud SDK in the runner's environment. It configures the SDK with the project ID stored in the <code>GCP_PROJECT_ID</code> secret.</li>

  <li><code><b>Build Docker Image</b></code>: The <code>run: | gcloud auth configure-docker</code> and<code>docker build --target production -t gcr.io/mldjango/mysite:latest ./mysite </code>lines build the Docker image using the Dockerfile in the mysite directory and tag it with the specified name.

```bash
- name: Build Docker image
  run: |
    gcloud auth configure-docker
    docker build --target production -t  gcr.io/mldjango/mysite:latest ./mysite
```

 <li><code><b>Push Docker Image</b></code>: This step runs a shell command to push the Docker image to the Google Container Registry (GCR). The image is pushed to the <code>mldjango</code> project in GCR, with the tag <code>mysite:latest</code>.</li>

```bash
- name: Push Docker image
  run: |
    docker push gcr.io/mldjango/mysite:latest
```
  <li><code><b>Deploy to Cloud Run</b></code>: This step runs a shell command to deploy the application to Google Cloud Run. It deploys the Docker image from GCR to a Cloud Run service named mysite in the asia-south1 region. The --allow-unauthenticated flag allows the service to be accessed without authentication.</li>

```bash
- name: Deploy to Cloud Run
  run: |
     gcloud run deploy mysite --image gcr.io/mldjango/mysite:latest --region asia-south1 --platform managed --allow-unauthenticated
```
This deployment process ensures that every push to the <code>main</code>branch triggers a new deployment of the application to Google Cloud Run.


## Dockerfile

The Dockerfile is a multi-stage build Dockerfile. Here's a step-by-step explanation:

1. **Use an official Python runtime as a parent image**: The `FROM python:3.11.5 as builder` line specifies the base image for the Docker image. In this case, it's using the official Python image version 3.11.5 and naming this stage as `builder`.

2. **Set environment variables**: The `ENV PYTHONDONTWRITEBYTECODE 1` and `ENV PYTHONUNBUFFERED 1` lines set environment variables in the Docker image. `PYTHONDONTWRITEBYTECODE` prevents Python from writing `.pyc` files, and `PYTHONUNBUFFERED` ensures that Python's output is sent straight to the terminal without being first buffered, which is useful for logging.

3. **Set work directory**: The `WORKDIR /app` line sets the working directory in the Docker image to `/app`.

4. **Install dependencies**: The `COPY requirements.txt /app/` and `RUN pip install --no-cache-dir -r requirements.txt` lines copy the `requirements.txt` file from your project to the Docker image and install the Python dependencies listed in it.

5. **Copy the current directory contents into the container at /app**: The `COPY . /app/` line copies the entire contents of your project directory into the `/app` directory in the Docker image.

6. **Collect static files**: The `RUN python manage.py collectstatic --noinput` line runs the `collectstatic` management command of your Django application. This collects all the static files from your application into a single location that can be served easily.

7. **Start a new stage and copy over the necessary files**: The `FROM python:3.11.5 as production` line starts a new stage of the build and names it `production`. This is where the production-ready Docker image is built.

8. **Copy from builder**: The `COPY --from=builder /app /app` line copies the `/app` directory from the `builder` stage into the `production` stage. This includes the application code and the collected static files.

9. **Install dependencies in the production image as well**: The `COPY requirements.txt /app/` and `RUN pip install --no-cache-dir -r requirements.txt` lines are repeated in the `production` stage to ensure that the Python dependencies are installed in the production image as well.

10. **Make port 8000 available to the world outside this container**: The `EXPOSE 8080` line informs Docker that the application listens on the specified network ports at runtime. In this case, it's port 8080.

11. **Run gunicorn when the container launches**: The `CMD exec gunicorn --bind :$PORT --worker-class gevent mysite.wsgi:application` line specifies the command to run when the Docker container is started. In this case, it's running the Gunicorn server with the Django application.

This Dockerfile is a standard way to containerize a Python web application for deployment. It ensures that the application and its dependencies are isolated in a Docker container, which can be easily deployed to any environment that supports Docker.