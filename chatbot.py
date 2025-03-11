import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from knowledge_base import knowledge_base, patterns, faqs, keywords

# Download NLTK resources (uncomment first time)
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

# Create training data for the vectorizer
training_data = []
for pattern, _ in patterns.items():
    # Clean pattern and add to training data
    cleaned_pattern = re.sub(r'[()[\]?|]', '', pattern)
    cleaned_pattern = re.sub(r'(?i)', '', cleaned_pattern)
    cleaned_pattern = re.sub(r'\s+', ' ', cleaned_pattern).strip()
    if cleaned_pattern:
        training_data.append(cleaned_pattern)

# Add all keywords to training data
for keyword in keywords.keys():
    training_data.append(keyword)

# Add FAQ questions to training data
for faq in faqs:
    training_data.append(faq["question"])

# Create and fit TF-IDF vectorizer
vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
tfidf_matrix = vectorizer.fit_transform(training_data)

# Function to preprocess text
def preprocess_text(text):
    # Tokenize and lowercase
    tokens = word_tokenize(text.lower())
    
    # Remove stopwords and lemmatize
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    
    processed_tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalpha() and token not in stop_words]
    return " ".join(processed_tokens)

def generate_response(response_type):
    # Existing response types
    if response_type == 'personal_info_intro':
        return knowledge_base["personal_info"]["introduction"]
    
    elif response_type == 'contact_info':
        return f"You can reach me via email at {knowledge_base['personal_info']['email']} or connect with me on LinkedIn: {knowledge_base['personal_info']['linkedin']} and GitHub: {knowledge_base['personal_info']['github']}. Check out my portfolio at {knowledge_base['personal_info']['portfolio']} for more details!"
    
    elif response_type == 'education_info':
        return knowledge_base["education"]["description"]
    
    elif response_type == 'skills_info':
        return knowledge_base["skills"]["description"]
    
    elif response_type == 'projects_info':
        projects = knowledge_base["projects"]
        response = "Sure! Here are some of my key projects:\n\n"
        
        for i, project in enumerate(projects, 1):
            response += f"{i}️⃣ **{project['name']}**\n"
            response += f"* {project['description']}\n\n"
        
        response += f"Check out my GitHub for project code: {knowledge_base['personal_info']['github']}"
        return response
    
    elif response_type == 'internship_info':
        internships = knowledge_base["internships"]
        if internships:
            return internships[0]["description"]
        return "I'm currently seeking internship opportunities."
    
    elif response_type == 'certification_info':
        certifications = knowledge_base["certifications"]
        response = "Yes! Here are some of my certifications:\n\n"
        
        for cert in certifications:
            response += f"* **{cert['name']}** – {cert['provider']}\n"
        
        return response
    
    elif response_type == 'future_goals':
        return knowledge_base["future_goals"]["description"]
    
    elif response_type == 'interests_info':
        return knowledge_base["interest_description"]
    
    elif response_type == 'location_info':
        return f"I'm from {knowledge_base['personal_info']['location']}. I'm pursuing my education at {knowledge_base['education']['institution']}."
    
    elif response_type == 'phone_info':
        return f"You can reach me by phone at {knowledge_base['personal_info']['phone']}."
    
    elif response_type == 'greeting':
        return f"Hello! I'm {knowledge_base['personal_info']['name']}. How can I help you today?"
    
    elif response_type == 'farewell':
        return "Thanks for chatting! Feel free to reach out anytime you want to know more about my work."
    
    elif response_type == 'thanks':
        return "You're welcome! If you have any more questions, I'm happy to help."
    
    elif response_type == 'how_are_you':
        return "I'm doing well, thanks for asking! Always ready to chat about my projects, skills, and experience in computer science. How can I help you today?"
    
    elif response_type == 'current_activity':
        return "Currently, I'm focused on enhancing my skills in deep learning and exploring new applications for my projects. I'm also looking for opportunities to contribute to open-source projects."
    
    elif response_type == 'full_name':
        return f"My full name is {knowledge_base['personal_info']['full_name']}. I'm a Computer Science Engineer from Bengaluru, India."
    
    elif response_type == 'specialization':
        return knowledge_base["personal_info"]["specialization"]
    
    elif response_type == 'daily_routine':
        return knowledge_base["personal_info"]["daily_routine"]
    
    elif response_type == 'what_do_you_do':
        return "I am a computer science student."
    
    elif response_type == 'programming_languages':
        return "I know Python, including data analytics and visualization libraries, and SQL."
    
    elif response_type == 'subjects_studied':
        return knowledge_base["education"]["subjects"]
    
    elif response_type == 'technologies_frameworks':
        return knowledge_base["skills"]["technologies"]
    
    elif response_type == 'signature_verification':
        return knowledge_base["projects"][2]["details"]
    
    elif response_type == 'most_challenging_project':
        return knowledge_base["projects"][0]["challenge"]
    
    elif response_type == 'ml_ai_projects':
        return "Yes, I have worked on multiple ML-based projects."
    
    elif response_type == 'favorite_programming_topics':
        return knowledge_base["favorites"]["programming_topics"]
    
    elif response_type == 'prefer_frontend_backend':
        return "I prefer back-end development."
    
    elif response_type == 'career_goals':
        return knowledge_base["future_goals"]["career_goals"]
    
    elif response_type == 'motivation':
        return knowledge_base["motivation"]
    
    elif response_type == 'favorite_books_movies':
        return knowledge_base["favorites"]["books_movies"]
    
    elif response_type == 'tech_product':
        return "I have built projects like a chatbot and a signature verification system."
    
    elif response_type == 'dream_job':
        return "AI and data-driven roles."
    
    elif response_type == 'advice':
        return knowledge_base["advice"]
    
    elif response_type == 'fun_fact':
        return f"Fun fact: {knowledge_base['fun_facts']['beard']} Also, {knowledge_base['fun_facts']['personality']}"
    
    # New response types
    elif response_type == 'field_of_study':
        return knowledge_base["field_of_study"]
    
    elif response_type == 'sql_experience':
        return knowledge_base["sql_experience"]
    
    elif response_type == 'favorite_books_movies':
        return knowledge_base["favorite_books_movies"]
    
    elif response_type == 'advice_for_beginners':
        return knowledge_base["advice_for_beginners"]
    
    elif response_type == 'learning_approach':
        return knowledge_base["learning_approach"]
    
    elif response_type == 'enso_event_prediction':
        return knowledge_base["enso_event_prediction"]
    
    else:
        return "I'm not sure I understand that question. Could you try rephrasing or ask me about my education, skills, projects, or experience?"

def get_response(user_input):
    # First check patterns (explicit rules)
    for pattern, response_type in patterns.items():
        if re.search(pattern, user_input):
            return generate_response(response_type)
    
    # Then try similarity-based responses (more advanced approach)
    similarity_response = get_similarity_response(user_input)
    if similarity_response:
        return similarity_response
    
    # If no match found, try keyword matching
    return keyword_based_response(user_input)

def get_similarity_response(user_input):
    # Preprocess user input
    processed_input = preprocess_text(user_input)
    
    # Check if we have any content after preprocessing
    if not processed_input:
        return None
    
    # Transform user input using the vectorizer
    user_vector = vectorizer.transform([processed_input])
    
    # Calculate similarity with FAQs
    faq_similarities = []
    for i, faq in enumerate(faqs):
        faq_vector = vectorizer.transform([preprocess_text(faq["question"])])
        similarity = cosine_similarity(user_vector, faq_vector)[0][0]
        faq_similarities.append((similarity, i))
    
    # Find best matching FAQ if exists
    best_match = max(faq_similarities, key=lambda x: x[0])
    
    # If similarity is high enough, use FAQ answer - LOWERED THRESHOLD
    if best_match[0] > 0.3:  # Lowered threshold from 0.5 to 0.3
        return faqs[best_match[1]]["answer"]
    
    return None

def keyword_based_response(user_input):
    user_input = user_input.lower()
    
    # Check for specific project inquiries
    for project in knowledge_base["projects"]:
        if project["name"].lower() in user_input:
            technologies = ", ".join(project["technologies"])
            return f"**{project['name']}**: {project['description']}\n\nTechnologies used: {technologies}"
    
    # Check for keywords
    matched_keywords = []
    for keyword, response in keywords.items():
        if keyword.lower() in user_input:
            matched_keywords.append((keyword, response))
    
    # If multiple keywords match, prioritize longer keywords as they are likely more specific
    if matched_keywords:
        best_match = max(matched_keywords, key=lambda x: len(x[0]))
        return best_match[1]
    
    # Generate a more helpful fallback response
    return "I'd be happy to tell you about my skills, projects, or experience. Feel free to ask about my education, technical skills, projects like ENSO prediction or real estate price prediction, or my experience and interests in computer science and machine learning."

def generate_contextual_response(user_input, chat_history=None):
    """Generate a response based on the current query and chat history"""
    if not chat_history:
        chat_history = []
    
    # Check if this is a follow-up question
    is_followup = False
    pronouns = ["it", "this", "that", "they", "them", "these", "those"]
    
    if any(pronoun in user_input.lower().split() for pronoun in pronouns) and chat_history:
        is_followup = True
        
    if is_followup and chat_history:
        # Get the last exchange context
        last_exchange = chat_history[-1]
        combined_context = last_exchange['bot'] + " " + user_input
        # Try to get a response for the combined context
        return get_response(combined_context)
    
    # Regular processing if not a follow-up
    return get_response(user_input)