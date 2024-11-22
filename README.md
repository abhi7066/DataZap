# DockBridge
###### A robust and versatile data migration solution designed to seamlessly transfer data between various platforms, including Azure, AWS, Snowflake, and SQL Server.

## Installation Guide
##### Follow these steps to set up DockBridge on your local machine:


<b>1. Clone the Repository</b>
>Clone the repository to your local system:
```bash
git clone https://github.com/abhi7066/darkalchemy-vscode-theme.git  
```
<b>2. Open the Project</b>
>Open the project folder in your preferred IDE (e.g., VSCode, IntelliJ).

<b>3. Configure the Environment</b>
>Add the required environment variables in the .env file. Ensure that the necessary credentials and configuration settings for the data sources (Azure, AWS, Snowflake, SQL Server) are properly set.

<b>4. Build the Docker Image</b>
>Build the Docker image by running the following command in the terminal:
```bash
docker build . -t <dockerImageName>:<Tag(optional)>  
```

<b>5. Run the Docker Container</b>
>Start the Docker container with the following command:
```bash
docker run <--rm(optional)> <dockerImageName>:<Tag(optional)>
```
