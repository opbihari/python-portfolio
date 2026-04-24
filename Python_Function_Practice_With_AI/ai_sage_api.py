"""
AI SAGE API SERVER
Python Flask backend for Python Ink website
Handles AI-powered code explanations, snippet generation, and interactive learning
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json
import re
from typing import Optional, Dict, Any
import logging

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ============================================================
# AI PROVIDER CONFIGURATION
# ============================================================
# Supports: "gemini", "openai", "anthropic", or "local"
AI_PROVIDER = os.getenv("AI_PROVIDER", "gemini")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")

# ============================================================
# AI SERVICE IMPLEMENTATIONS
# ============================================================

class AIService:
    """Base AI service interface"""
    def generate_snippet(self, prompt: str) -> Dict[str, Any]:
        raise NotImplementedError
    
    def explain_code(self, code: str, output: Optional[str] = None) -> str:
        raise NotImplementedError


class GeminiService(AIService):
    """Google Gemini AI implementation"""
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
    
    def _make_request(self, prompt: str, is_json: bool = False) -> str:
        import requests
        
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "systemInstruction": {
                "parts": [{
                    "text": "You are an expert Python AI Sage. Provide concise, accurate, and helpful code explanations and snippets. Use proper formatting and clear examples."
                }]
            }
        }
        
        if is_json:
            payload["generationConfig"] = {
                "responseMimeType": "application/json",
                "responseSchema": {
                    "type": "OBJECT",
                    "properties": {
                        "title": {"type": "STRING"},
                        "desc": {"type": "STRING"},
                        "code": {"type": "STRING"}
                    },
                    "required": ["title", "desc", "code"]
                }
            }
        
        headers = {
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.post(
                f"{self.base_url}?key={self.api_key}",
                json=payload,
                headers=headers,
                timeout=30
            )
            response.raise_for_status()
            data = response.json()
            return data["candidates"][0]["content"]["parts"][0]["text"]
        except requests.exceptions.RequestException as e:
            logger.error(f"Gemini API error: {e}")
            raise Exception(f"Failed to call Gemini API: {str(e)}")
    
    def generate_snippet(self, prompt: str) -> Dict[str, Any]:
        """Generate Python code snippet from natural language prompt"""
        full_prompt = f'Write a Python snippet for the following: "{prompt}". Return JSON with title, desc, and code fields.'
        response_text = self._make_request(full_prompt, is_json=True)
        
        try:
            result = json.loads(response_text)
            return {
                "success": True,
                "title": result.get("title", "Untitled"),
                "desc": result.get("desc", ""),
                "code": result.get("code", "# Code generation failed")
            }
        except json.JSONDecodeError:
            return {
                "success": False,
                "error": "Invalid JSON response from AI",
                "raw": response_text
            }
    
    def explain_code(self, code: str, output: Optional[str] = None) -> str:
        """Explain Python code with optional execution output"""
        prompt = f'Analyze this Python code:\n```python\n{code}\n```\n'
        if output and output != "// run the code to see output here":
            prompt += f'The console output is:\n```\n{output}\n```\n'
        prompt += 'Briefly explain what the code does. If there\'s an error, explain why and how to fix it.'
        
        return self._make_request(prompt, is_json=False)


class OpenAIService(AIService):
    """OpenAI GPT implementation"""
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.openai.com/v1/chat/completions"
    
    def _make_request(self, messages: list) -> str:
        import requests
        
        payload = {
            "model": "gpt-4-turbo-preview",
            "messages": messages,
            "temperature": 0.7
        }
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.post(
                self.base_url,
                json=payload,
                headers=headers,
                timeout=30
            )
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]
        except requests.exceptions.RequestException as e:
            logger.error(f"OpenAI API error: {e}")
            raise Exception(f"Failed to call OpenAI API: {str(e)}")
    
    def generate_snippet(self, prompt: str) -> Dict[str, Any]:
        """Generate Python code snippet"""
        messages = [
            {
                "role": "system",
                "content": "You are an expert Python AI Sage. Generate concise, well-documented Python code snippets. Respond in JSON format with 'title', 'desc', and 'code' fields."
            },
            {
                "role": "user",
                "content": f'Write a Python snippet for: "{prompt}". Return only valid JSON.'
            }
        ]
        
        response_text = self._make_request(messages)
        
        try:
            result = json.loads(response_text)
            return {
                "success": True,
                "title": result.get("title", "Untitled"),
                "desc": result.get("desc", ""),
                "code": result.get("code", "# Code generation failed")
            }
        except json.JSONDecodeError:
            return {
                "success": False,
                "error": "Invalid JSON response from AI",
                "raw": response_text
            }
    
    def explain_code(self, code: str, output: Optional[str] = None) -> str:
        """Explain Python code"""
        content = f'Analyze this Python code:\n```python\n{code}\n```\n'
        if output and output != "// run the code to see output here":
            content += f'Console output:\n```\n{output}\n```\n'
        content += 'Briefly explain what the code does. If there\'s an error, explain why and how to fix it.'
        
        messages = [
            {"role": "system", "content": "You are an expert Python instructor."},
            {"role": "user", "content": content}
        ]
        
        return self._make_request(messages)


class AnthropicService(AIService):
    """Anthropic Claude implementation"""
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.anthropic.com/v1/messages"
    
    def _make_request(self, prompt: str) -> str:
        import requests
        
        payload = {
            "model": "claude-3-sonnet-20240229",
            "max_tokens": 2048,
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
        
        headers = {
            "x-api-key": self.api_key,
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.post(
                self.base_url,
                json=payload,
                headers=headers,
                timeout=30
            )
            response.raise_for_status()
            data = response.json()
            return data["content"][0]["text"]
        except requests.exceptions.RequestException as e:
            logger.error(f"Anthropic API error: {e}")
            raise Exception(f"Failed to call Anthropic API: {str(e)}")
    
    def generate_snippet(self, prompt: str) -> Dict[str, Any]:
        """Generate Python code snippet"""
        request_prompt = f"""Write a Python snippet for: "{prompt}"

Return ONLY valid JSON with these fields:
{{"title": "...", "desc": "...", "code": "..."}}"""
        
        response_text = self._make_request(request_prompt)
        
        try:
            # Try to extract JSON if there's surrounding text
            json_match = re.search(r'\{[\s\S]*\}', response_text)
            if json_match:
                result = json.loads(json_match.group())
            else:
                result = json.loads(response_text)
            
            return {
                "success": True,
                "title": result.get("title", "Untitled"),
                "desc": result.get("desc", ""),
                "code": result.get("code", "# Code generation failed")
            }
        except json.JSONDecodeError:
            return {
                "success": False,
                "error": "Invalid JSON response from AI",
                "raw": response_text
            }
    
    def explain_code(self, code: str, output: Optional[str] = None) -> str:
        """Explain Python code"""
        prompt = f'Analyze this Python code:\n```python\n{code}\n```\n'
        if output and output != "// run the code to see output here":
            prompt += f'Console output:\n```\n{output}\n```\n'
        prompt += 'Briefly explain what the code does. If there\'s an error, explain why and how to fix it.'
        
        return self._make_request(prompt)


class MockService(AIService):
    """Mock AI service for testing without API keys"""
    def generate_snippet(self, prompt: str) -> Dict[str, Any]:
        """Mock snippet generation"""
        prompt_lower = prompt.lower()
        
        snippets = {
            "reverse": {
                "title": "Reverse a List",
                "desc": "Reverse a list in multiple ways",
                "code": "lst = [1, 2, 3, 4, 5]\nprint(lst[::-1])      # [5, 4, 3, 2, 1]\nprint(list(reversed(lst)))  # [5, 4, 3, 2, 1]\nlst.reverse()\nprint(lst)            # [5, 4, 3, 2, 1]"
            },
            "fibonacci": {
                "title": "Fibonacci Generator",
                "desc": "Generate fibonacci sequence",
                "code": "def fibonacci(n):\n    a, b = 0, 1\n    for _ in range(n):\n        yield a\n        a, b = b, a + b\n\nfor num in fibonacci(10):\n    print(num, end=' ')"
            },
            "json": {
                "title": "Read and Parse JSON",
                "desc": "Load JSON data from a string",
                "code": "import json\ndata = '{\"name\": \"Alice\", \"age\": 30}'\nparsed = json.loads(data)\nprint(parsed['name'])  # Alice"
            },
            "default": {
                "title": "Simple Python Program",
                "desc": "A basic Python example",
                "code": "def greet(name):\n    return f'Hello, {name}!'\n\nprint(greet('Pythonista'))"
            }
        }
        
        # Try to find a matching snippet
        for key, snippet in snippets.items():
            if key in prompt_lower:
                return {"success": True, **snippet}
        
        return {"success": True, **snippets["default"]}
    
    def explain_code(self, code: str, output: Optional[str] = None) -> str:
        """Mock code explanation"""
        lines = len(code.split('\n'))
        explanation = f"This Python code snippet contains {lines} lines. It demonstrates basic Python concepts and good coding practices."
        
        if output:
            explanation += f"\n\nWhen executed, it produces the following output:\n```\n{output}\n```"
        
        return explanation


# ============================================================
# SERVICE FACTORY
# ============================================================

def get_ai_service() -> AIService:
    """Factory function to get configured AI service"""
    provider = AI_PROVIDER.lower()
    
    if provider == "gemini" and GEMINI_API_KEY:
        return GeminiService(GEMINI_API_KEY)
    elif provider == "openai" and OPENAI_API_KEY:
        return OpenAIService(OPENAI_API_KEY)
    elif provider == "anthropic" and ANTHROPIC_API_KEY:
        return AnthropicService(ANTHROPIC_API_KEY)
    else:
        logger.warning(f"No valid API key for {provider}, falling back to mock service")
        return MockService()


# ============================================================
# API ROUTES
# ============================================================

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    service = get_ai_service()
    return jsonify({
        "status": "healthy",
        "ai_provider": AI_PROVIDER,
        "service": service.__class__.__name__
    }), 200


@app.route('/api/generate-snippet', methods=['POST'])
def generate_snippet():
    """
    Generate a Python code snippet from a natural language prompt
    """
    try:
        data = request.get_json()
        
        if not data or "prompt" not in data:
            return jsonify({
                "success": False,
                "error": "Missing 'prompt' field in request body"
            }), 400
        
        prompt = data.get("prompt", "").strip()
        if not prompt or len(prompt) < 3:
            return jsonify({
                "success": False,
                "error": "Prompt must be at least 3 characters long"
            }), 400
        
        service = get_ai_service()
        result = service.generate_snippet(prompt)
        
        if result.get("success"):
            return jsonify(result), 200
        else:
            return jsonify(result), 500
    
    except Exception as e:
        logger.error(f"Error in generate_snippet: {e}")
        return jsonify({
            "success": False,
            "error": f"Server error: {str(e)}"
        }), 500


@app.route('/api/explain-code', methods=['POST'])
def explain_code():
    """
    Explain Python code with optional execution output
    """
    try:
        data = request.get_json()
        
        if not data or "code" not in data:
            return jsonify({
                "success": False,
                "error": "Missing 'code' field in request body"
            }), 400
        
        code = data.get("code", "").strip()
        if not code or len(code) < 3:
            return jsonify({
                "success": False,
                "error": "Code must be at least 3 characters long"
            }), 400
        
        output = data.get("output", None)
        
        service = get_ai_service()
        explanation = service.explain_code(code, output)
        
        return jsonify({
            "success": True,
            "explanation": explanation
        }), 200
    
    except Exception as e:
        logger.error(f"Error in explain_code: {e}")
        return jsonify({
            "success": False,
            "error": f"Server error: {str(e)}"
        }), 500


@app.route('/api/refactor-code', methods=['POST'])
def refactor_code():
    """
    Suggest refactoring improvements for Python code
    """
    try:
        data = request.get_json()
        
        if not data or "code" not in data:
            return jsonify({
                "success": False,
                "error": "Missing 'code' field in request body"
            }), 400
        
        code = data.get("code", "").strip()
        if not code:
            return jsonify({
                "success": False,
                "error": "Code cannot be empty"
            }), 400
        
        service = get_ai_service()
        
                
        service = get_ai_service()
        
        # Construct the refactoring prompt
        prompt = f"Review this Python code and suggest improvements for readability, efficiency, and PEP 8 compliance:\n\n```python\n{code}\n```\n\nProvide the refactored code and a brief explanation of the changes."
        
        # Use the explain_code method as a general-purpose text generator for now
        refactored_response = service.explain_code(code, output="REFACTOR_REQUEST: " + prompt)
        
        return jsonify({
            "success": True,
            "refactored_content": refactored_response
        }), 200
    
    except Exception as e:
        logger.error(f"Error in refactor_code: {e}")
        return jsonify({
            "success": False,
            "error": f"Server error: {str(e)}"
        }), 500


if __name__ == '__main__':
    # Get port from environment variable or default to 5001
    port = int(os.getenv("PORT", 5001))
    app.run(host='0.0.0.0', port=port, debug=True)
