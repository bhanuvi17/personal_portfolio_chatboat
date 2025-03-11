# 🏆 Portfolio Chatbot

This is a **Portfolio Chatbot** built using Flask and Scikit-learn. The chatbot responds to user queries about personal information, project details, and FAQs by matching input patterns with a predefined knowledge base.

## 📌 Features
✅ Responds to personal queries  
✅ Handles FAQs with contextual understanding  
✅ Uses TF-IDF and cosine similarity for pattern matching  
✅ Interactive web interface using Flask  
✅ Supports session management for better context retention  
✅ Logs errors for debugging  

## 📂 Project Structure
```
portfolio_chatbot/
│── app.py                  # Flask app (main file)
│── chatbot.py              # Chatbot logic
│── knowledge_base.py       # Knowledge base and patterns
│── utils.py                # Utility functions
│── templates/
│   └── index.html          # Frontend UI
│── tests/
│   └── test_chatbot.py     # Unit tests
│── requirements.txt        # Dependencies
│── README.md               # Project info
│── __pycache__/            # Compiled Python files
```

## 🛠 Prerequisites
- Python 3.x installed (recommended: Python 3.8 or later)  
- pip installed (comes with Python)  

## 🎯 Technologies Used
- **Backend:** Flask  
- **Natural Language Processing:** Scikit-learn, NLTK  
- **Deployment:** Render  

## 🔧 Installation & Setup

### 🔹 Clone the Repository
```sh
git clone https://github.com/bhanuvi17/personal_portfolio_chatboat.git
cd personal_portfolio_chatboat
```

### 🔹 Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate  # On Windows
```

### 🔹 Install Dependencies
```sh
pip install -r requirements.txt
```

### 🔹 Run the Flask App
```sh
python app.py
```

🔗 Open in your browser: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## 🚀 Live Website
🚧 **Available Soon** 🚧

## 🚀 Deploying on Render

### 1️⃣ Push Code to GitHub
```sh
git add .
git commit -m "Initial commit"
git push origin main
```
## 🖼️ Screenshots
- **Web Interface**  
![Screenshot](https://github.com/bhanuvi17/personal_portfolio_chatboat/blob/8080731f7058e38512b13ad65e3b72e3b439d8e2/Screenshot%202025-03-11%20172400.png)

## 🏆 Future Enhancements
✅ Add a chatbot training model using deep learning  
✅ Add more conversational depth and context retention  
✅ Improve UI with interactive animations
✅ Add speech conversation

## 📝 License
This project is open-source under the **MIT License**.

## 💡 Need Help?
Feel free to open an issue or contribute to improve this project! 😊

⭐ If you like this project, give it a star on GitHub! ⭐
