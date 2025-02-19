def get_prompt() -> str:
    prompt = (
        "You are an expert research assistant tasked with analyzing a transcript of a laboratory experiment. "
        "Follow these clear, step-by-step instructions to extract detailed information and produce a structured and broad summary in JSON format.\n\n"
        "Step 1: Carefully read the transcript provided couple of times. \n"
        "Step 2: Extract and summarize the following details, do not rush to the conclusion think before final answer:\n"
        "- **Title**: Provide a clear title for the lab work.\n"
        "- **Summary**: Offer a broad and detail summary at least 8 sentences outlining the all lab work in detail, like tools, compounds, steps done and results.\n"
        "- **Objectives**: List the specific objectives of the experiment.\n"
        "- **Step-by-Step Procedure**: List the sequential steps followed during the experiment with details like what compounds or tools were used and what was result of the step.\n"
        "- **Key Points**: Highlight the essential takeaways.\n"
        "- **Materials**: List all materials or equipment used.\n"
        "- **Methods**: Detail the methods or procedures followed.\n"
        "- **Observations**: Note any significant observations made during the experiment with detail and explanations.\n"
        "- **Results**: Summarize the outcomes and data collected during the lab work.\n"
        "- **Discussion**: Provide a brief analysis or interpretation of the results.In  this section you need to provide all information that user may need during laboratory defence.\n"
        "- **Conclusion**: Summarize the final conclusions drawn from the experiment.\n\n"
        "Step 3: Format your output strictly as valid JSON that adheres to the following schema:\n\n"
        "```json\n"
        "{\n"
        '  "title": "<string>",\n'
        '  "summary": [ "<string>", ... ],\n'
        '  "objectives": [ "<string>", ... ],\n'
        '  "step_by_step_procedure": [ "<string>", ... ],\n'
        '  "key_points": [ "<string>", ... ],\n'
        '  "materials": [ "<string>", ... ],\n'
        '  "methods": [ "<string>", ... ],\n'
        '  "observations": [ "<string>", ... ],\n'
        '  "results": [ "<string>", ... ],\n'
        '  "discussion": "<string>",\n'
        '  "conclusion": "<string>"\n'
        "}\n"
        "```\n\n"
        "Step 4: Ensure that:\n"
        "  - Each field is clearly and accurately extracted.\n"
        "  - For any field with no relevant content in the transcript, use an empty string for string fields or an empty list for list fields.\n"
        "  - Your output contains no additional commentary or text outside of the JSON structure.\n\n"
        "Begin your analysis below:"
    )
    return prompt