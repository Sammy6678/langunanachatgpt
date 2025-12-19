from flask import Flask, render_template, request, jsonify
import os
import logging
from dotenv import load_dotenv
import random

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Get port from environment (Azure provides PORT env variable)
PORT = int(os.getenv("PORT", 8000))

app = Flask(__name__)

# Mock responses for testing deployment
MOCK_RESPONSES = [
    "Hello! I'm LangunanGPT running in **mock mode** for deployment testing. This means I'm working without external API calls!",
    "Great question! I'm a test chatbot that helps you verify your Azure deployment is working correctly. 🚀",
    "I'm responding from your deployed application! This confirms that the app is running properly on Azure Web App.",
    "Your deployment is successful! I can receive and respond to messages without needing any external API keys.",
    "Everything looks good! Your app is communicating correctly. Once you're ready, you can integrate with OpenAI or other LLMs.",
    "This is a mock response to help you test the deployment. All your infrastructure is working as expected! ✅",
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        
        logger.info(f"Received message: {user_message[:50]}...")
        
        # Mock chatbot response
        response = random.choice(MOCK_RESPONSES)
        
        if len(user_message) > 100:
            response += "\n\n📝 I noticed you sent a longer message - the app is handling it perfectly!"
        
        logger.info("Successfully generated mock response")
        
        return jsonify({
            'success': True,
            'response': response
        })
        
    except Exception as e:
        logger.error(f"Error processing message: {str(e)}", exc_info=True)
        return jsonify({
            'success': False,
            'response': "❌ Sorry, I encountered an error processing your request. Please try again."
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=False)
