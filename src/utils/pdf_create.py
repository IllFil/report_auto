import json

from fpdf import FPDF


def sanitize_text(text) -> str:
        """
        If text is not a string, try to convert it (using json() if available),
        then encode the text in latin-1, ignoring characters that cannot be encoded,
        and decode it back to a string.
        """
        if not isinstance(text, str):
                try:
                        # If the object is a pydantic model, it likely has a .json() method.
                        text = text.json(indent=2)
                except Exception:
                        text = str(text)
        return text.encode("latin-1", errors="ignore").decode("latin-1")


def save_pdf_transcript(filename: str, title: str, content) -> None:
        pdf = FPDF()
        pdf.add_page()
        # Enable automatic page breaks with a margin of 15 mm
        pdf.set_auto_page_break(auto=True, margin=15)

        # Sanitize title and content to remove unsupported characters.
        title = sanitize_text(title)
        content = sanitize_text(content)

        # Set title font and add title
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, title, ln=True)

        pdf.ln(10)  # add some vertical space

        # Set content font and add content
        pdf.set_font("Arial", "", 12)
        pdf.multi_cell(0, 10, content)

        pdf.output(filename)
        print(f"Saved {filename}")


def model_report_pdf(filename: str, report) -> None:
        """
        Create a nicely formatted PDF report for the model output.

        `report` can be a LabReport pydantic model or a dictionary.
        """
        # If the report is not already a dict, try to convert it.
        if not isinstance(report, dict):
                try:
                        # For pydantic models, .dict() is usually available.
                        report = report.dict()
                except Exception:
                        # Otherwise, use json.loads of its json representation.
                        report = json.loads(report.json())

        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)

        # Define helper function to write a section with a heading and content.
        def write_section(heading: str, content, bullet: bool = False):
                # Write heading
                pdf.set_font("Arial", "B", 14)
                pdf.cell(0, 10, heading, ln=True)
                pdf.ln(2)
                pdf.set_font("Arial", "", 12)
                if isinstance(content, list):
                        # Write each item as a bullet point.
                        for item in content:
                                # Sanitize and indent bullet point.
                                line = "- " + sanitize_text(item)
                                pdf.multi_cell(0, 8, line)
                        pdf.ln(3)
                else:
                        # Assume content is a string.
                        text = sanitize_text(content)
                        pdf.multi_cell(0, 8, text)
                        pdf.ln(5)

        # Write the Title (centered)
        title = sanitize_text(report.get("title", ""))
        pdf.set_font("Arial", "B", 20)
        pdf.cell(0, 12, title, ln=True, align="C")
        pdf.ln(8)

        # Write each section. Adjust the order as desired.
        write_section("Summary", report.get("summary", []))
        write_section("Objectives", report.get("objectives", []))
        write_section("Step-by-Step Procedure", report.get("step_by_step_procedure", []))
        write_section("Key Points", report.get("key_points", []))
        write_section("Materials", report.get("materials", []))
        write_section("Methods", report.get("methods", []))
        write_section("Observations", report.get("observations", []))
        write_section("Results", report.get("results", []))
        write_section("Discussion", report.get("discussion", ""))
        write_section("Conclusion", report.get("conclusion", ""))

        pdf.output(filename)
        print(f"Saved pretty report as {filename}")
