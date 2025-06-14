# 🚀 LinkedIn Post Generator

An AI-powered tool that generates LinkedIn posts based on your preferences for length, language, and topic tags. This project uses machine learning to analyze existing posts and generate new, relevant content.

![LinkedIn Post Generator](images/linkedin_post.png) 
![Try it out yourself](images/linkedin_post_internship.png)

## ✨ Features

- **Smart Post Generation**: AI-powered content creation based on existing LinkedIn posts
- **Customizable Parameters**: Choose from different lengths, languages, and topics
- **Tag-based Filtering**: Select from automatically extracted and unified tags
- **Multi-language Support**: English, Hinglish (Hindi + English), and Hindi
- **Interactive Web Interface**: Easy-to-use Streamlit application

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**<br>
   git clone https://github.com/shrutiiiiin/LinkedinPostGenerator.git<br>
   cd linkedin-post-generator
2. **Install dependencies**<br>
   pip install -r requirements.txt
3. **Setup your data**<br>
    python process_posts.py
4. **Configure your LLM**<br>
   Update llm_helper.py with your AI model configuration.<br>
   Add your API keys if using external services
5. **Run the Application**<br>
    streamlit run main.py