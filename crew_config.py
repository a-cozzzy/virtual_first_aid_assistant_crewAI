import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Define Agents with concise outputs
user_interaction_agent = Agent(
    role="First Aid Guide",
    goal="Provide concise first aid advice based on user symptoms.",
    verbose=True,
    llm=LLM(model="gemini/gemini-2.0-flash", api_key=GEMINI_API_KEY),
    backstory="A virtual assistant delivering clear, brief first aid advice."
)

severity_classifier = Agent(
    role="Symptom Severity Evaluator",
    goal="Classify symptom severity on a 1-10 scale and determine physical/mental nature.",
    verbose=True,
    llm=LLM(model="gemini/gemini-2.0-flash", api_key=GEMINI_API_KEY),
    backstory="Evaluates symptom severity and classifies physical vs mental nature."
)

physical_health_agent = Agent(
    role="Physical Health Assistant",
    goal="Provide concise first aid guidance for minor physical issues.",
    verbose=True,
    llm=LLM(model="gemini/gemini-2.0-flash", api_key=GEMINI_API_KEY),
    allow_delegation=False,
    backstory="Provide step-by-step guidance for physical health issues."
)

mental_health_agent = Agent(
    role="Mental Health Support Assistant",
    goal="Offer empathetic support and coping strategies for emotional challenges.",
    verbose=True,
    llm=LLM(model="gemini/gemini-2.0-flash", api_key=GEMINI_API_KEY),
    allow_delegation=False,
    backstory="Offer emotional support and coping strategies for mental health."
)

# New agent to condense the output into 5-6 key points
# post_processing_agent = Agent(
#     role="Output Condenser",
#     goal="Condense the output from all agents into 5-6 key points with clear and simple instructions.",
#     verbose=False,
#     llm=LLM(model="gemini/gemini-2.0-flash", api_key=GEMINI_API_KEY),
#     backstory="Condenses detailed information into a simplified list of 5-6 key instructions."
# )
post_processing_agent = Agent(
    role="Output Condenser",
    goal="Condense the output from all agents into 5-6 key points with clear and simple instructions.",
    verbose=True,
    llm=LLM(model="gemini/gemini-2.0-flash", api_key=GEMINI_API_KEY),
    backstory="Condenses detailed information into a simplified list of 5-6 key instructions."
)


# Build tasks with concise outputs
def build_tasks(user_input: str):
    return [
        Task(
            name="Symptom Analysis",
            description=f"Analyze symptoms: {user_input}. Identify conditions and give a disclaimer if necessary.",
            agent=user_interaction_agent,
            expected_output="Condition analysis with a disclaimer."
        ),
        Task(
            name="Symptom Severity Assessment",
            description=f"Assess severity of symptoms: {user_input}. Classify severity (1-10) and whether physical or mental.",
            agent=severity_classifier,
            expected_output="Severity (1-10) and classification (physical/mental)."
        ),
        Task(
            name="Physical Health First Aid Support",
            description=f"Provide first aid advice for physical issues: {user_input}. Include 3-5 simple steps.",
            agent=physical_health_agent,
            expected_output="3-5 first aid steps, with a disclaimer."
        ),
        Task(
            name="Mental Health Emotional Support",
            description=f"Provide emotional support and coping strategies for: {user_input}. Include 3 strategies if necessary.",
            agent=mental_health_agent,
            expected_output="3 coping strategies, with a disclaimer if mental health issues are identified."
        ),
        # Task(
        #     name="Post-Processing",
        #     description="Condense all previous outputs into 5-6 key actionable points.",
        #     agent=post_processing_agent,
        #     expected_output="5-6 actionable, concise instructions."
        # )
        Task(
            name="Post-Processing",
            description="""
            Condense all previous outputs into 5-6 key actionable points.
            Format each point with:
            1. A number
            2. A brief, bold title with a relevant emoji
            3. A short, clear instruction
            
            Example format:
            **🚨 1. Seek Medical Help:** Get immediate medical attention if symptoms worsen.
            **💊 2. Medication:** Take recommended dosage of pain reliever if appropriate.
            
            Start with the most urgent/important points.
            """,
            agent=post_processing_agent,
            expected_output="""
            5-6 formatted points, each containing:
            **[EMOJI] [NUMBER]. [TITLE]:** [Instruction]
            """
        )
    ]

# Entrypoint for running the Crew
def run_crew(user_symptoms: str):
    crew = Crew(
        agents=[user_interaction_agent, severity_classifier, physical_health_agent, mental_health_agent, post_processing_agent],
        tasks=build_tasks(user_symptoms),
        process=Process.sequential,
        verbose=True
    )
    return crew.kickoff(inputs={"user_symptoms": user_symptoms})

if __name__ == "__main__":
    user_symptoms = input("Please describe your symptoms: ")
    output = run_crew(user_symptoms)
    print(output)
