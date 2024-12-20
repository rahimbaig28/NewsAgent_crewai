from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Call the gemini models
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Ensure the LLM provider is specified
llm_provider = 'google'  # Specify the correct provider here

# Creating a senior researcher agent with memory and verbose mode
news_researcher = Agent(
    role="Senior Researcher",
    goal='Uncover groundbreaking technologies in {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of "
        "innovation, eager to explore and share knowledge that could change "
        "the world."
    ),
    tools=[tool],
    llm=llm,
    llm_provider=llm_provider,  # Include the provider here
    allow_delegation=True
)

# Creating a writer agent with custom tools responsible for writing news blogs
news_writer = Agent(
    role='Writer',
    goal='Narrate compelling tech stories about {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft "
        "engaging narratives that captivate and educate, bringing new "
        "discoveries to light in an accessible manner."
    ),
    tools=[tool],
    llm=llm,
    llm_provider=llm_provider,  # Include the provider here
    allow_delegation=False
)