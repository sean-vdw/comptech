from flask import Flask, jsonify, request
import anthropic
from dotenv import load_dotenv
import os

app = Flask(__name__)

@app.route('/api/message', methods=['POST'])
def get_message():
    load_dotenv()

    user_message = request.json.get('message', '')

    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        temperature=0.0,
        system="You are the leading compliance consultant for RIAs, Wealth Management firms, and broker dealers. These companies pay you top dollar in order to identify and suggest changes to text, audio, and image content marketing that would pose any sort of regulatory risk. For a piece of content provided, which may be text, audio, or image, provided via a URL, pdf, word file, video file, or other file type, identify any language that is in violation of any SEC or other regulator rules surrounding marketing content. If needed, please also provide the suggested revision in text, whether the content should be removed altogether, or a disclaimer that would allow the content to remain in the marketing piece as-is. Finally, be sure to identify which rules this may be in violation of, or potentially in conflict with.",
        messages=[
            {
              "role": "user", 
              "content": user_message
            }
        ]
    )

    return jsonify(message.content)