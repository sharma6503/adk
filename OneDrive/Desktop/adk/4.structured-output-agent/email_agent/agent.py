from google.adk.agents import Agent
from pydantic import BaseModel, Field
from typing import List, Optional

class EmailContent(BaseModel):
    subject: str = Field(..., description="The subject of the email. Should be concise and relevant.")
    body: str = Field(..., description="The body content of the email. Should be clear and informative.")
    recipients: List[str] = Field(..., description="List of email addresses to send the email to. Should be valid email addresses.")

root_agent = Agent(
    name="email_agent",
    model="gemini-2.0-flash",
    description="An agent that helps users draft and send emails Professionally with structured content.",
    instruction="You are an email drafting agent. Use the provided structured input to create a well-formatted email. Ensure the subject is clear, the body is informative and business-like, and the recipients are valid email addresses." \
    "IMPORTANT:Your response should be a valid JSON object that matches this structure." \
    "{'subject': 'Your email subject here', 'body': 'Your email body here', 'recipients': ['recipient1@example.com', 'recipient2@example.com']}",
    output_schema=EmailContent,
    output_key="email_content"
)