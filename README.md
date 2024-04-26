# Engineering Entrance Chatbot for Pulchowk Campus (EDUGUIDEBOT)

## Introduction:
In the ever-evolving landscape of education, aspiring engineering students often encounter challenges in navigating the complexities of entrance exams, application processes, and associated fees. To address these issues, this project proposes the development of an intelligent Engineering Entrance Chatbot. Leveraging advanced technologies such as Natural Language Processing (NLP) and machine learning, the chatbot aims to provide tailored guidance and information to streamline the journey of prospective engineering students.

## Problem Statement:
Engineering aspirants frequently face confusion and uncertainty regarding the application process, exam fees, eligibility criteria, and other essential details. The lack of a centralized and intelligent system to assist students in their queries contributes to the challenge of obtaining accurate and up-to-date information. This project aims to bridge this gap by creating a user-friendly chatbot capable of comprehending and addressing the diverse needs of individuals aspiring to pursue engineering studies.

## Objectives:
The objective of this project is to develop a chatbot using text processing and other AI and ML techniques in Python to assist engineering entrance exam aspirants. The chatbot aims to provide information about the application process, exam fees, requirements, and other relevant details to help students navigate the complexities of engineering entrance exams and studies.

## Features:
1. **Natural Language Processing (NLP):**
    - Implement a robust NLP module to understand and process user queries. 
    - Use techniques like tokenization, part-of-speech tagging, and named entity recognition to extract relevant information from user inputs.

2. **Information Retrieval:**
    - Integrate a comprehensive knowledge base about engineering entrance exams, application procedures, fees, eligibility criteria, and other related details. 
    - Utilize algorithms for efficient information retrieval based on user queries.

3. **Intent Recognition:**
    - Train the chatbot to recognize user intents accurately. 
    - Identify common queries related to application procedures, fee structures, eligibility criteria, and other topics relevant to engineering entrance exams.

## Preliminary Literature Review:
Previous studies and developments in the field of chatbots and AI-assisted education reveal the potential for intelligent systems to provide personalized guidance and support to students. NLP techniques, combined with machine learning algorithms, have shown promise in creating conversational agents capable of understanding and responding to user queries effectively. However, there is a gap in the literature regarding the specific application of such technologies to address the challenges faced by engineering entrance exam aspirants.

## Technology Stack:
- **Programming Language:** Python
- **NLP Library:** 
    - chatterbot==1.0.8
    - chatterbot-corpus==1.2.0
    - pyyaml==3.13
    - spacy==3.0.6
- **Web Framework:** Django for deployment

## Proposed Methodology:
1. **Requirement Gathering and Data Collection:**
    - Gather comprehensive data on engineering entrance exams, application procedures, fees, and other relevant information.

2. **Model Training:**
    - Train NLP models for intent recognition and information extraction. 
    - Utilize machine learning models to improve accuracy over time.

3. **Integration:**
    - Integrate the developed models with the chatbot framework, ensuring seamless communication and data flow.

4. **Testing:**
    - Conduct thorough testing to identify and address any issues related to intent recognition, information retrieval, and user interactions.

5. **User Feedback and Improvement:**
    - Collect user feedback to identify areas of improvement and refine the chatbot's capabilities over time.

## Expected Outcome:
The successful implementation of the Engineering Entrance Chatbot is expected to result in a user-friendly, intelligent system that significantly simplifies the application process for engineering aspirants. The chatbot's ability to provide accurate, real-time information, personalized guidance, and multilingual support is anticipated to enhance the overall experience of students navigating the complexities of engineering entrance exams, leading to increased confidence and informed decision-making.


#### Getting Started:

1. **Activate Virtual Environment:**
   - Navigate to the project directory: `cd chatapp/`
   - Activate the virtual environment for Python:
     ```
     # For Windows
     venv\Scripts\activate
     # For Unix or MacOS
     source venv/bin/activate
     ```

2. **Install Dependencies:**
   - Use pip to install the required packages listed in `requirements.txt`:
     ```
     pip install -r requirements.txt
     ```

3. **Run Migrations:**
   - Ensure your database schema is up-to-date by running migrations:
     ```
     python manage.py migrate
     ```

#### Usage:

- Once the virtual environment is activated, dependencies are installed, and migrations are applied, you can start using the EDUGUIDEBOT application.

- To run the development server, execute the following command:

```
python manage.py runserver
```

- Access the application by navigating to `http://localhost:8000/` in your web browser.

#### Additional Notes:

- Make sure to keep your virtual environment activated whenever you're working on the project to ensure compatibility with the installed dependencies.
- If you encounter any issues during setup or usage, refer to the project's documentation or seek assistance from the project team.


## Conclusion:
By developing a sophisticated chatbot with text processing and AI/ML capabilities, this project aims to provide a user-friendly solution for engineering entrance exam aspirants, helping them navigate the complexities of the application process, fees, and other related queries.
