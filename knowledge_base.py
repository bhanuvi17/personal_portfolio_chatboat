knowledge_base = {
    "personal_info": {
        "name": "Bhanuprakash",
        "full_name": "Bhanuprakash",
        "location": "Bengaluru, India",
        "email": "bhanuprakash1722004@gmail.com",
        "phone": "+91 8971351314",
        "linkedin": "https://www.linkedin.com/in/bhanuvi17/",
        "github": "https://github.com/bhanuvi17",
        "portfolio": "https://bhanu-portfolio.onrender.com/#",
        "introduction": "Hey there! I'm Bhanuprakash, a passionate Computer Science Engineer from Bengaluru, India. I specialize in Python, data analysis, and machine learning. Feel free to ask me about my work and projects!",
        "daily_routine": "My typical day involves coding, learning new technologies, working on projects, and keeping up with the latest in AI and machine learning. I also make time for chess, which is one of my favorite hobbies.",
        "specialization": "I specialize in Python programming, data analysis, and machine learning, with a focus on practical applications like my ENSO prediction system and real estate price prediction tools.",
        "field_of_study": "I am studying Computer Science Engineering, with a focus on programming, data analysis, and machine learning.",
        "sql_experience": "Yes, I have experience with SQL. I've used it for database queries and data analysis in my projects.",
        "favorite_books_movies": "I love machine learning books and science fiction movies. They inspire me to think creatively and solve problems.",
        "advice_for_beginners": "Don’t waste time watching too many videos—learn by coding and trying different approaches! Start with small projects and gradually build your skills.",
        "learning_approach": "To learn new technologies, I take structured online courses, read documentation, and work on hands-on projects. I also follow industry experts and participate in coding communities.",
        "enso_event_prediction": "ENSO (El Niño-Southern Oscillation) Event Prediction is a project where I used LSTM and RNN models to predict El Niño and La Niña events based on historical climate data. The model achieved 86% accuracy."
    },
    "education": {
        "degree": "B.E. in Computer Science & Engineering",
        "institution": "Sambhram Institute of Technology, Bengaluru",
        "cgpa": "8.1",
        "description": "I am pursuing a B.E. in Computer Science & Engineering at Sambhram Institute of Technology, Bengaluru, with a current CGPA of 8.1. I have a strong foundation in programming, AI, and machine learning.",
        "subjects": "Core fundamental CS subjects."
    },
    "skills": {
        "programming": ["Python", "OOP", "VS Code", "Git", "GitHub"],
        "data_analysis": ["NumPy", "Pandas", "SQL", "Tableau", "Matplotlib", "Seaborn", "Jupyter Notebook"],
        "machine_learning": ["Scikit-learn", "Neural Networks", "TensorFlow", "Supervised Learning", "Unsupervised Learning"],
        "description": "I have expertise in:\n* Programming & Tools: Python, OOP, VS Code, Git & GitHub\n* Data Analysis & Visualization: NumPy, Pandas, SQL, Tableau, Matplotlib, Seaborn, Jupyter Notebook\n* Machine Learning & AI: Scikit-learn, Neural Networks, TensorFlow, Supervised & Unsupervised Learning",
        "technologies": "I work with data analysis, ML tools, databases, Power BI, Python frameworks, Flask, and Streamlit."
    },
    "projects": [
        {
            "name": "Predicting ENSO Events Based on Historical Data",
            "technologies": ["LSTM", "RNN", "TensorFlow", "Keras", "Streamlit"],
            "description": "Used LSTM and RNN deep learning models to predict ENSO events. Achieved 86% accuracy after fine-tuning with TensorFlow/Keras. Built a Streamlit-powered dashboard for real-time predictions.",
            "challenge": "My most challenging project so far."
        },
        {
            "name": "Real Estate Price Prediction",
            "technologies": ["Linear Regression", "Flask", "Render"],
            "description": "Developed a linear regression model for forecasting real estate prices. Integrated Flask to create a web-based prediction tool. Deployed on Render for seamless accessibility."
        },
        {
            "name": "Signature Verification System",
            "technologies": ["Python", "OpenCV", "Flask", "Render"],
            "description": "Built an image-processing-based system to verify signatures. Used Python & OpenCV for feature extraction and comparison. Hosted a Flask web app on Render for online authentication.",
            "details": "Yes! I developed a signature verification system using OpenCV and ML techniques."
        }
    ],
    "internships": [
        {
            "company": "Karunadu Technologies",
            "duration": "Oct 2023 – Nov 2023",
            "description": "I interned at Karunadu Technologies (Oct 2023 – Nov 2023), where I worked on machine learning models, data analysis, and real-time data processing under expert mentorship."
        }
    ],
    "certifications": [
        {
            "name": "Machine Learning Specialization",
            "provider": "Deeplearning.AI (Coursera)"
        },
        {
            "name": "Programming with Python",
            "provider": "Internshala"
        },
        {
            "name": "AI for Everyone",
            "provider": "Deeplearning.AI (Coursera)"
        },
        {
            "name": "Data Analysis & Machine Learning Bootcamp",
            "provider": "Udemy"
        }
    ],
    "future_goals": {
        "technical": ["AI", "Deep Learning", "Real-time Data Processing", "AI-powered Applications", "Open-source Contributions"],
        "description": "I aim to advance my expertise in AI, deep learning, and real-time data processing. I'm also interested in developing AI-powered applications and contributing to open-source projects.",
        "career_goals": "I aim to work in AI and data-driven roles."
    },
    "interests": ["Chess", "AI", "ML", "Data Science"],
    "interest_description": "I enjoy playing chess and exploring emerging technologies like AI, ML, and Data Science.",
    "motivation": "The ability to create something meaningful and solve problems motivates me to code.",
    "favorites": {
        "programming_topics": "I enjoy all Python-related topics.",
        "books_movies": "I love machine learning books and science fiction movies."
    },
    "fun_facts": {
        "beard": "I’m 20 and still don’t have a beard!",
        "personality": "I’m a silent person."
    },
    "advice": "Don’t waste time watching too many videos—learn by coding and trying different approaches!",
    
}

# Pattern matching for questions
patterns = {
    r'(?i)who are you|tell me about yourself|introduce yourself': 'personal_info_intro',
    r'(?i)how can i contact you|contact information|contact details|email|reach you': 'contact_info',
    r'(?i)what is your educational background|education|where did you study|university|college|school|degree': 'education_info',
    r'(?i)what are your technical skills|skills|what can you do|technologies|programming languages|tools': 'skills_info',
    r'(?i)tell me about your projects|projects|what have you built|portfolio projects': 'projects_info',
    r'(?i)have you done any internships|work experience|internship|where have you worked': 'internship_info',
    r'(?i)do you have any certifications|certifications|courses|what have you learned|certificates|certifications|what courses|what certifications': 'certification_info',
    r'(?i)what are your future goals|aspirations|career goals|plans|future plans': 'future_goals',
    r'(?i)what are your interests|hobbies|interests|leisure|free time|interested in': 'interests_info',
    r'(?i)hello|hi|hey|greetings': 'greeting',
    r'(?i)bye|goodbye|see you|talk to you later': 'farewell',
    r'(?i)thanks|thank you': 'thanks',
    r'(?i)where are you from|your location|where do you live|which city|which country': 'location_info',
    r'(?i)phone|mobile|contact number|call you': 'phone_info',
    r'(?i)how are you|how are you doing|how do you do': 'how_are_you',
    r'(?i)what are you doing|what are you up to|what are you currently doing|current work': 'current_activity',
    r'(?i)what\'s your full name|full name|your name': 'full_name',
    r'(?i)speciali[sz]e|speciali[sz]ed in|speciali[sz]ation|expert in|expertise': 'specialization',
    r'(?i)daily routine|day look like|everyday|day to day|daily schedule': 'daily_routine',
    r'(?i)what do you do': 'what_do_you_do',
    r'(?i)what programming languages do you know': 'programming_languages',
    r'(?i)what subjects have you studied': 'subjects_studied',
    r'(?i)what technologies and frameworks are you comfortable with': 'technologies_frameworks',
    r'(?i)can you tell me about your signature verification project': 'signature_verification',
    r'(?i)what is your most challenging project': 'most_challenging_project',
    r'(?i)have you developed any machine learning or AI-based projects': 'ml_ai_projects',
    r'(?i)what are your favorite programming topics': 'favorite_programming_topics',
    r'(?i)do you prefer front-end or back-end development': 'prefer_frontend_backend',
    r'(?i)what are your career goals': 'career_goals',
    r'(?i)what motivates you to code': 'motivation',
    r'(?i)what are your favorite books or movies': 'favorite_books_movies',
    r'(?i)if you could build any tech product, what would it be': 'tech_product',
    r'(?i)what is your dream job': 'dream_job',
    r'(?i)what advice would you give to someone starting programming': 'advice',
    r'(?i)can you tell a fun fact about yourself': 'fun_fact',
    r'(?i)what is your field of study|what are you studying|field of study': 'field_of_study',
    r'(?i)what programming languages do you know|which languages do you code in': 'programming_languages',
    r'(?i)do you have experience with sql|sql experience|sql skills': 'sql_experience',
    r'(?i)what kind of books or movies do you enjoy|favorite books or movies|books or movies': 'favorite_books_movies',
    r'(?i)what advice would you give to beginners in programming|advice for beginners|programming advice': 'advice_for_beginners',
    r'(?i)how do you approach learning new technologies|learning new technologies|approach to learning': 'learning_approach',
    r'(?i)what is enso event prediction|enso event prediction|enso prediction': 'enso_event_prediction'
}

# FAQs with potential questions and answers
faqs = [
    {
        "question": "What kind of data analysis tools do you use?",
        "answer": "I use a comprehensive suite of data analysis tools including NumPy and Pandas for data manipulation, Matplotlib and Seaborn for visualization, SQL for database queries, and Tableau for creating interactive dashboards. I've applied these tools across my projects, particularly in my ENSO prediction work."
    },
    {
        "question": "How did you implement your signature verification system?",
        "answer": "For my signature verification system, I used Python with OpenCV for image processing. The system extracts unique features from signatures using contour detection and SIFT algorithms, then performs similarity matching between the test signature and stored authentic signatures. The application is wrapped in a Flask web interface and deployed on Render for easy access."
    },
    {
        "question": "What was your role during your internship at Karunadu Technologies?",
        "answer": "During my internship at Karunadu Technologies, I worked on developing and optimizing machine learning models for data analytics solutions. I was responsible for data preprocessing, model training, and implementation of real-time data processing pipelines. I collaborated with senior data scientists who provided mentorship throughout my internship period from October to November 2023."
    },
    {
        "question": "What machine learning algorithms are you familiar with?",
        "answer": "I'm familiar with a wide range of machine learning algorithms including regression models, classification algorithms (Decision Trees, Random Forests, SVMs), clustering methods (K-means, DBSCAN), and deep learning architectures (CNNs, RNNs, LSTMs). I've applied these in projects like ENSO event prediction, where I used LSTMs and RNNs to achieve 86% prediction accuracy."
    },
    {
        "question": "Tell me about your experience with TensorFlow",
        "answer": "I've used TensorFlow extensively in my deep learning projects, particularly for my ENSO Events prediction model. I implemented custom LSTM and RNN architectures, handled data preprocessing with TensorFlow's data pipeline, and optimized model performance through hyperparameter tuning. I'm comfortable with both the Keras API and lower-level TensorFlow operations."
    },
    {
        "question": "How did you achieve 86% accuracy in your ENSO prediction project?",
        "answer": "In my ENSO prediction project, I achieved 86% accuracy through a combination of careful data preprocessing, feature engineering, and model architecture selection. I used historical climate data spanning several decades, engineered temporal features, and implemented a stacked LSTM-RNN architecture. The model was fine-tuned through extensive hyperparameter optimization using TensorFlow and Keras. I also incorporated domain knowledge about climate patterns to improve the model's performance."
    },
    {
        "question": "What challenges did you face in your real estate price prediction project?",
        "answer": "During my real estate price prediction project, I faced several challenges including handling missing data in property records, addressing multicollinearity among features, and capturing non-linear relationships that impact property values. I overcame these by implementing robust data imputation techniques, using feature selection methods to address collinearity, and exploring various regression models beyond simple linear regression. Deploying the model as a user-friendly Flask application also presented integration challenges that I successfully resolved."
    },
    {
        "question": "Do you have any experience with NLP or computer vision?",
        "answer": "Yes, I have experience in both areas. For computer vision, my signature verification system utilizes OpenCV for feature extraction and image processing. Although it's not highlighted in my main projects, I've also worked with NLP techniques in side projects, implementing text classification and sentiment analysis using libraries like NLTK and spaCy. I'm passionate about both fields and am continuously expanding my knowledge in these areas."
    },
    {
        "question": "What programming languages are you proficient in besides Python?",
        "answer": "While Python is my primary language, I also have working knowledge of SQL for database operations, HTML/CSS for web development, and JavaScript for basic front-end interactivity. My philosophy is to use the right tool for the job, though Python's versatility makes it my go-to language for most tasks in data science and machine learning."
    },
    {
        "question": "How do you approach data preprocessing in your projects?",
        "answer": "I follow a systematic approach to data preprocessing. First, I perform exploratory data analysis to understand data characteristics. Then I handle missing values through appropriate imputation methods, address outliers, and normalize or standardize features as needed. Feature engineering is a critical step where I create new variables that better represent underlying patterns. Finally, I split the data into training, validation, and test sets to ensure robust model evaluation. I use Pandas and NumPy extensively throughout this process."
    },
    {
        "question": "What is your approach to continuous learning in the fast-evolving field of AI?",
        "answer": "To stay current in AI, I follow a multi-faceted approach: I take structured online courses like my Machine Learning Specialization from Deeplearning.AI, read research papers on arXiv, follow leading AI practitioners on platforms like GitHub and Twitter, participate in Kaggle competitions, and implement new techniques in personal projects. I believe hands-on application is essential, so I try to implement new concepts I learn rather than just studying them theoretically."
    },
    {
        "question": "How do you ensure your machine learning models are robust and reliable?",
        "answer": "I ensure model robustness through rigorous validation strategies including k-fold cross-validation, careful feature selection to prevent overfitting, proper handling of data leakage, and testing on holdout datasets. For critical applications, I implement ensemble methods to improve reliability. I also conduct sensitivity analysis to understand how my models respond to variations in input data and monitor performance metrics over time to catch concept drift in production environments."
    },
    {
        "question": "How are you today?",
        "answer": "I'm doing well, thanks for asking! Always ready to chat about my projects, skills, and experience in computer science. How can I help you today?"
    },
    {
        "question": "What are you currently working on?",
        "answer": "I'm currently focused on enhancing my skills in deep learning and exploring new applications for my ENSO prediction model. I'm also working on contributing to open-source projects to build my collaborative development experience."
    },
    {
        "question": "What's your full name?",
        "answer": "My name is Bhanuprakash. I'm a Computer Science Engineer from Bengaluru, India, specializing in Python, data analysis, and machine learning."
    },
    {
        "question": "What is your specialization?",
        "answer": "I specialize in Python programming, data analysis, and machine learning. My expertise is demonstrated in projects like my ENSO prediction system using LSTM/RNN models and my real estate price prediction tool. I'm particularly interested in applying ML techniques to solve real-world problems."
    },
    {
        "question": "What does your daily routine look like?",
        "answer": "My typical day involves coding and working on projects, learning new technologies, keeping up with the latest developments in AI and machine learning, and occasionally playing chess to sharpen my strategic thinking skills."
    }
]

# Keywords for different topics
keywords = {
    "about": "Hey there! I'm Bhanuprakash, a passionate Computer Science Engineer from Bengaluru, India. I specialize in Python, data analysis, and machine learning. Feel free to ask me about my work and projects!",
    "python": "Yes, Python is my primary programming language. I've used it extensively in my projects like the Signature Verification System and for data analysis with libraries like NumPy and Pandas.",
    "machine learning": "Machine learning is one of my core strengths! I've worked on projects involving LSTM, RNNs, and linear regression models. I also have certifications in ML from Deeplearning.AI.",
    "data analysis": "I'm proficient in data analysis using Python libraries like NumPy, Pandas, Matplotlib, and Seaborn. I've applied these skills in my ENSO prediction project and during my internship at Karunadu Technologies.",
    "flask": "I have experience with Flask for web development. I've used it in my Real Estate Price Prediction project and Signature Verification System to create user-friendly web interfaces.",
    "tensorflow": "I've worked with TensorFlow for deep learning, particularly in my ENSO Events prediction project where I achieved 86% accuracy using LSTM and RNN models.",
    "streamlit": "I've used Streamlit to build interactive dashboards, like in my ENSO Events prediction project where I created a real-time prediction dashboard.",
    "github": f"You can check out my code repositories on GitHub: {knowledge_base['personal_info']['github']}",
    "linkedin": f"You can connect with me on LinkedIn: {knowledge_base['personal_info']['linkedin']}",
    "bengaluru": "Yes, I'm based in Bengaluru, India, where I'm pursuing my B.E. in Computer Science & Engineering at Sambhram Institute of Technology.",
    "bangalore": "Yes, I'm based in Bengaluru (Bangalore), India, where I'm pursuing my B.E. in Computer Science & Engineering at Sambhram Institute of Technology.",
    "india": f"Yes, I'm from {knowledge_base['personal_info']['location']}.",
    "experience":"I interned at Karunadu Technologies (Oct 2023 – Nov 2023), where I worked on machine learning models, data analysis, and real-time data processing under expert mentorship.",
    "location": f"I'm currently in {knowledge_base['personal_info']['location']}.",
    "certification": "I have several certifications including Machine Learning Specialization from Deeplearning.AI, Programming with Python from Internshala, AI for Everyone from Deeplearning.AI, and Data Analysis & Machine Learning Bootcamp from Udemy.",
    "certificate": "I have several certifications including Machine Learning Specialization from Deeplearning.AI, Programming with Python from Internshala, AI for Everyone from Deeplearning.AI, and Data Analysis & Machine Learning Bootcamp from Udemy.",
    "project": "I've worked on several projects including ENSO Events prediction, Real Estate Price Prediction, and a Signature Verification System. Which one would you like to know more about?",
    "deep learning": "I've worked with deep learning models like LSTM and RNN in my ENSO Events prediction project. I'm also continuously expanding my knowledge in this area.",
    "resume": f"You can view my full resume on my portfolio website: {knowledge_base['personal_info']['portfolio']}",
    "open source": "I'm interested in contributing to open-source projects as part of my future goals. I believe in collaborative development and giving back to the community.",
    "chess": "Outside of coding, I enjoy playing chess. It helps me develop strategic thinking which is also useful in problem-solving as a developer.",
    "from": f"I'm from {knowledge_base['personal_info']['location']}.",
    "where": f"I'm located in {knowledge_base['personal_info']['location']}.",
    "phone": f"You can contact me through {knowledge_base['personal_info']['phone']}",
    "portfolio": f"Here is my Portfolio: {knowledge_base['personal_info']['portfolio']}",
    "how are you": "I'm doing well, thanks for asking! Always ready to chat about my projects, skills, and experience in computer science. How can I help you today?",
    "doing": "Currently, I'm focused on enhancing my skills in deep learning and exploring new applications for my projects. I'm also looking for opportunities to contribute to open-source projects.",
    "routine": "My typical day involves coding, learning new technologies, working on projects, and keeping up with the latest in AI and machine learning. I also make time for chess, which is one of my favorite hobbies.",
    "name": f"My name is {knowledge_base['personal_info']['name']}. I'm a Computer Science Engineer from Bengaluru, India.",
    "full name": f"My full name is {knowledge_base['personal_info']['full_name']}. I'm a Computer Science Engineer from Bengaluru, India.",
    "expertise": "My expertise is in Python programming, data analysis, and machine learning. I've applied these skills in projects like my ENSO prediction system and real estate price prediction tool.",
    "specialized": "I'm specialized in Python programming, data analysis, and machine learning, with a focus on practical applications and real-world problem-solving.",
    "interest": "I'm interested in AI, machine learning, data science, and playing chess. I'm passionate about using technology to solve real-world problems.",
    "message": "You can reach me by phone at +91 8971351314. OR Through my Instagram https://www.instagram.com/bhanu_17_02/",
    "birth" : "Feb 17th 2004"
}