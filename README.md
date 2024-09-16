# BGU-Student-Complaint-Generator
## Service Deployed Link
([https://bgu-complaint-generator-1.onrender.com](https://bgu-complaint-generator-1.onrender.com))

## Overview 

The BGU Student Complaint Generator is a project designed to test and integrate various technological tools. The application uses a combination of Google’s LLM, Gemma2, Flask, HTML, CSS, and Firebase to create a functional and interactive web-based complaint generator. Docker is used to containerize the application for consistent development and deployment.


## Technologies Used
- **Google LLM (Gemma2)**: Utilized through the Groq module for generating realistic complaints.
- **Flask**: Serves as the backend server to handle requests and responses.
- **HTML & CSS**: Employed for creating a visually appealing user interface that functions well on both desktop and mobile devices.
- **Firebase**: Used as the database service to store and manage user data and interactions.
- **Docker**: Used to containerize the application, ensuring consistent environments across different stages of development and deployment.

## Features
- **User Session Management**: Upon visiting the site, a cookie with a unique UUID is saved on the user's computer.
- **Conversation Storage**: All interactions between the user and the model are stored in Firebase.
- **Unique User Data**: Each user’s data is kept under a unique ID in Firebase’s users collection, corresponding to their UUID.
- **Responsive Design**: CSS ensures that the site is functional and visually appealing on both desktop and mobile devices.

## Installation 
### Option 1
1. Clone the repository.
2. Install the required dependencies using the requirements.txt file.
3. Create `.env` file for the GROQ_API_KEY token and get your own groq api key.
4. Create a `firebase_auth.json` file for the firebase authantication.
5. Run the `main.py` file.
### Option 2 
1. Clone the repository.
2. Create `.env` file for the GROQ_API_KEY token and get your own groq api key.
3. Create a `firebase_auth.json` file for the firebase authantication.
4. Use `docker-compose.yml` and `Dockerfile` to create an image and run it using docker.

 
## Usage

1. **Initial Visit**:
   - When a new user first visits the website, a cookie with a unique UUID is saved on their computer. Simultaneously, a new entry is created in the Firebase database to track the user.
   ![image](https://github.com/user-attachments/assets/4799086e-5fe3-47ba-a6ea-58f8897499d5)
   ![image](https://github.com/user-attachments/assets/72fd42da-ea76-4104-a4ac-96df193be4fb)
   ![image](https://github.com/user-attachments/assets/1df05d36-a8c2-4f0e-b8da-0973623dc098)


   

2. **Submitting a Complaint**:
   - The user can enter and submit a new complaint through the web interface.
   - Upon submission, the complaint is sent to Google’s LLM (Gemma2) via the Groq module.
   - The LLM generates a new, made-up complaint in response, which is then saved back to the Firebase database along with all previous messages exchanged between the user and the model.
![image](https://github.com/user-attachments/assets/b16704f7-f513-4391-9fab-0440820d6edc)
![image](https://github.com/user-attachments/assets/425fa103-66e6-459e-9215-3badfc4bc6ab)



3. **Returning to the Website**:
   - When the user returns to the website, their conversation history is loaded from Firebase and restored to the model.
   - This allows the model to remember and continue the conversation from where it left off, providing a seamless user experience.







