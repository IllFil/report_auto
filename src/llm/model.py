from pydantic import BaseModel
from openai import OpenAI
import os
from src.llm.prompt import get_prompt
client = OpenAI()

def get_model_res(model_name, transcript_text):
    prompt = get_prompt()
    class ResearchPaperExtraction(BaseModel):
        title: str
        summary: list[str]
        step_by_step_procedure: list[str]  # Listing steps as a list for clarity
        key_points: list[str]
        hypothesis: str  # The initial hypothesis being tested
        objectives: list[str]  # Clear objectives of the experiment
        materials: list[str]  # List of materials or equipment used
        methods: list[str]  # Detailed methods used in the experiment
        observations: list[str]  # Notable observations during the experiment
        results: list[str]  # Results or data points collected
        discussion: str  # Analysis or discussion of the results
        conclusion: str  # Final conclusions drawn from the experiment
        references: list[str]  # Any references or citations used

    completion = client.beta.chat.completions.parse(
        messages=[
            {"role": "system",
             "content": prompt},
            {"role": "user", "content": transcript_text}
        ],
        model=model_name,
        response_format=ResearchPaperExtraction,
    )

    research_paper = completion.choices[0].message.parsed

    return research_paper