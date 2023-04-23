# Containerize a YouTube to MP3 Converter with Docker
This is a small web-based application built with Flask to convert YouTube videos to MP3. The project is designed to demonstrate the concept of containerization with Docker. The application is containerized with Docker and pushed to Docker Hub.

# Prerequisites
Before getting started, ensure that you have the following installed on your system:

* Docker
* Python 3

# Getting Started
1. Clone the repository:

```
git clone https://github.com/yassinelkhantach/containerize-flask-youtube-converter-app-with-docker.git

```

2. Change into the project directory:

```
cd containerize-flask-youtube-converter-app-with-docker
```

3. Build the Docker image:

```
docker build -t yassinelk23/convert-my-tube .
```

4. Run the Docker container:

```
docker run -p 5000:5000 yassinelk23/convert-my-tube
```

5. Open a web browser and navigate to http://localhost:5000

6. Enter the URL of the YouTube video you wish to convert to MP3 and click the "Search" button.

7. If the URL is valid, the application will display the video's title and thumbnail. Click the "Download MP3" button to download the MP3 file.

# Contributing
Contributions are welcome! Fork the project and submit a pull request with your changes.
