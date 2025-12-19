import chainlit as cl
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

# Mock responses for testing deployment (no API key needed)
MOCK_RESPONSES = [
    "Hello! I'm LangunanGPT running in **mock mode** for deployment testing. This means I'm working without external API calls!",
    "Great question! I'm a test chatbot that helps you verify your Azure deployment is working correctly. 🚀",
    "I'm responding from your deployed application! This confirms that Chainlit is running properly on Azure Web App.",
    "Your deployment is successful! I can receive and respond to messages without needing any external API keys.",
    "Everything looks good! Your app is communicating correctly. Once you're ready, you can integrate with OpenAI or other LLMs.",
    "This is a mock response to help you test the deployment. All your infrastructure is working as expected! ✅",
]

@cl.on_chat_start
async def start():
    logger.info("New chat session started")
    await cl.Message(
        content="👋 Welcome to **LangunanGPT**! \n\n🧪 **Running in TEST MODE** - No API keys required.\n\nAsk me anything to test the deployment!"
    ).send()

@cl.on_message
async def handle_message(message: cl.Message):
    try:
        logger.info(f"Received message: {message.content[:50]}...")
        
        # Mock chatbot - responds with random pre-defined messages
        response_content = random.choice(MOCK_RESPONSES)
        
        # Add user's message length to make it feel interactive
        if len(message.content) > 100:
            response_content += "\n\n📝 I noticed you sent a longer message - the app is handling it perfectly!"
        
        logger.info("Successfully generated mock response")
        
        await cl.Message(
            content=response_content
        ).send()
        
    except Exception as e:
        logger.error(f"Error processing message: {str(e)}", exc_info=True)
        await cl.Message(
            content="❌ Sorry, I encountered an error processing your request. Please try again."
        ).send()
