# Neurify

Welcome to the MySite Django-Project. This project integrates three main components: the IrisApp, the Movie Recommendation System, and a welcome deck. 

## Getting Started

To get started with this project, you'll need to set up a local development environment, clone the repository, and install the required dependencies. Here's a step-by-step guide:

1. **Set up a Python environment**: This project requires Python 3.11.5. If you don't have this version of Python installed, you can download it from the [official Python website](https://www.python.org/downloads/). Once you have Python installed, it's recommended to create a virtual environment for the project. This can be done using the following commands:

```bash
python3 -m venv env
source env/bin/activate
```

2. **Clone the repository**: You can clone the repository using the following command:

```bash
git clone https://github.com/username/mysite.git
```

Replace <code>username</code> with your GitHub username and <code>mysite</code> with the name of your repository.

3. **Install the dependencies**: Navigate to the project directory and install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

4. **Run the server locally**: You can start the Django server locally using the following command:

```bash
python manage.py runserver
```

Now, you can access the application in your web browser at <code>http://localhost:8000</code>.

Detailed instructions for setting up the project can be found in the [Deployment.md](deployment.md) file.

## Components

This project consists of three main components:

1. **mysite**: This is the main Django project that integrates multiple smaller applications. More details about the structure and configuration of this project can be found in the [Architecture.md](Architecture.md) file.

2. **IrisApp**: This is a simple web application for predicting the species of an Iris flower based on its sepal and petal dimensions. 

3. **Movie Recommendation System**: This is a simple web application for recommending popular books.

## Integration

To integrate <code>mysite</code>with <code>irisapp</code> and <code>book_recommender</code>, you would need to modify the <code>urls.py</code> and <code>settings.py</code>files in the mysite project. Add <code>irisapp</code> and <code>book_recommender</code> to the <code>INSTALLED_APPS</code> list in <code>settings.py</code>and include the URLs of <code>irisapp</code> and <code>book_recommender</code> in the project's URL configuration in <code>urls.py</code>.

## Usage

With these changes, when a user visits <code>https://mysite-olvdmbamqa-el.a.run.app//iris</code>, they will be directed to the irisapp application, and when they visit <code>https://mysite-olvdmbamqa-el.a.run.app/movie</code>, they will be directed to the book_recommender application.


## Further Reading

For more detailed information about the architecture of the project and the deployment process, please refer to the [Architecture.md](Architecture.md) and [Deployment.md](deployment.md) files, respectively.