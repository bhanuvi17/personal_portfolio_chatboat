import unittest
from chatbot import generate_response

class TestChatbot(unittest.TestCase):
    def test_project_query(self):
        response = generate_response("Tell me about the ENSO project")
        self.assertIn("LSTM", response)
        self.assertIn("86% accuracy", response)

    def test_greeting(self):
        response = generate_response("Hello")
        self.assertIn("Hello! I'm Bhanuprakash", response)

    def test_what_do_you_do(self):
        response = generate_response("What do you do?")
        self.assertIn("I am a computer science student.", response)

    def test_programming_languages(self):
        response = generate_response("What programming languages do you know?")
        self.assertIn("Python", response)
        self.assertIn("SQL", response)

    def test_fun_fact(self):
        response = generate_response("Can you tell a fun fact about yourself?")
        self.assertIn("don’t have a beard", response)
    def test_field_of_study(self):
        response = generate_response("What is your field of study?")
        self.assertIn("Computer Science Engineering", response)

    def test_sql_experience(self):
        response = generate_response("Do you have experience with SQL?")
        self.assertIn("Yes, I have experience with SQL", response)

    def test_favorite_books_movies(self):
        response = generate_response("What kind of books or movies do you enjoy?")
        self.assertIn("machine learning books", response)
        self.assertIn("science fiction movies", response)

    def test_advice_for_beginners(self):
        response = generate_response("What advice would you give to beginners in programming?")
        self.assertIn("learn by coding", response)

    def test_learning_approach(self):
        response = generate_response("How do you approach learning new technologies?")
        self.assertIn("structured online courses", response)

    def test_enso_event_prediction(self):
        response = generate_response("What is ENSO Event Prediction?")
        self.assertIn("LSTM and RNN models", response)

if __name__ == '__main__':
    unittest.main()