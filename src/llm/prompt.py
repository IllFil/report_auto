def get_prompt() -> str:
    prompt = (
        "You are an AI tasked with analyzing a transcript of a laboratory experiment. "
        "Extract and summarize the key elements of the experiment according to the following structure:\n\n"
        "- **Title**: Provide a clear title for the lab work.\n"
        "- **Summary**: Offer a brief summary in bullet points outlining the main aspects.\n"
        "- **Step-by-Step Procedure**: List the sequential steps followed during the experiment.\n"
        "- **Key Points**: Highlight the essential takeaways.\n"
        "- **Hypothesis**: Describe the initial hypothesis of the experiment.\n"
        "- **Objectives**: List the specific objectives of the experiment.\n"
        "- **Materials**: List all materials or equipment used.\n"
        "- **Methods**: Detail the methods or procedures followed.\n"
        "- **Observations**: Note any significant observations made during the experiment.\n"
        "- **Results**: Summarize the outcomes or data collected.\n"
        "- **Discussion**: Provide a brief analysis or interpretation of the results.\n"
        "- **Conclusion**: Summarize the final conclusions drawn from the experiment.\n"
        "- **References**: Include any references or citations mentioned.\n\n"
        "Please extract the above information in a structured JSON format that matches the provided data model. "
        "Ensure clarity, conciseness, and completeness in your summary."
    )
    return prompt

