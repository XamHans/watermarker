# Watermarker Setup Guide

## Prerequisites

Before you can run a Watermarker, you need to have Python installed on your computer.

### Installing Python

1. **Download Python**:
   Visit the official Python website to download Python. Use this link to download the version appropriate for your operating system: [Python Download](https://www.python.org/downloads/).

   - For Windows users, make sure to check the box that says "Add Python 3.x to PATH" at the beginning of the installation.

2. **Verify Python Installation**:
   To check if Python installed correctly, open your command line interface (CLI) — Command Prompt for Windows, Terminal for macOS and Linux — and enter the following command:
   ```
   python --version
   ```
   This should display the Python version number. If you see an error, Python may not be installed correctly.

## Setting Up Your Watermarker

Once Python is installed, you can set up your Watermarker by following these steps:

1. **Download Your Watermarker**:
   Obtain the files for your Watermarker. This might be from a download as zip file or git clone

2. **Navigate to Your Application Directory**:
   Open your command line interface and change the directory to where your Watermarker files are located. You can do this by typing:

   ```
   cd path_to_your_application
   ```

   Replace `path_to_your_application` with the path to your Watermarker files.

3. **Install Required Libraries**:
   Your Watermarker might require specific Python libraries to run correctly. These dependencies are usually listed in a file named `requirements.txt`. Install them using the following command:
   ```
   pip install -r requirements.txt
   ```

## Running the Watermarker

To run the application, you need to execute it through the command line:

1. **Launch the Application**:
   In your CLI where your application directory is active, run the following command:

   ```
   streamlit run main.py
   ```

2. **Access the Application**:
   Once the application starts, Streamlit will provide you with a local URL, usually something like `http://localhost:8501`. Open this URL in your web browser to view your application.

# Enjoy your Watermarker!

## Need Help?

If you encounter any issues contact me at

Johannes Hayer
https://jhayer.tech/
https://www.linkedin.com/in/johannes-hayer-b8253a294/
