# Project Setup

To set up and run this project, follow these steps:

## Prerequisites

Before running the project, make sure you have the following packages installed:

* pandas
* requests
* functools
* json
* mistralai

You can install these packages using pip:
```
pip install pandas requests functools json mistralai
```
## <img src="https://media.theresanaiforthat.com/icons/mistral-ai.svg?height=207" width="20" height="20"> Mistral API Key

This project uses the Mistral.ai Large model. To use the model, you need to provide an API key, which you can obtain from the Mistral AI console at `https://console.mistral.ai`. Once you have the API key, you can add it to your code as follows:
```python
import mistralai
api_key = "YOUR_API_KEY"
```
Replace `YOUR_API_KEY` with your actual API key.

## Running the Server

To start the FastAPI server, run the following command in your terminal:
```css
uvicorn FastAPI:app --reload
```
This command starts the server and enables automatic reloading of the server whenever changes are made to the code.

Once the server is running, you can access the API documentation by navigating to <http://localhost:8000> in your web browser.

## Project Overview

The remainder of the project can be found in the `Mistral Function Calling.ipynb` Jupyter notebook. This notebook provides an example of how to use Mistral AI to call Python functions based on textual conversations. It includes step-by-step instructions and code examples.

That's it! You have successfully set up and run the project.
