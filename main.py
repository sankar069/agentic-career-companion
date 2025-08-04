from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI()

class UserInput(BaseModel):
    skills: str
    interests: str

@app.post("/career-recommend")
def get_career_path(user: UserInput):
    prompt = f"""
    I have skills in {user.skills} and I'm interested in {user.interests}.
    Suggest a suitable career path with job titles, tools to learn, and online courses.
    """

    url = "https://us-south.ml.cloud.ibm.com/ml/v1/text-generation"
    headers = {
        "Authorization": f"Bearer {os.getenv('IBM_API_KEY')}",
        "Content-Type": "application/json"
    }

    print("🧠 Headers being sent to IBM:", headers)

    data = {
        "model_id": "granite-3-3-8b-instruct",
        "input": prompt
    }

    response = requests.post(url, headers=headers, json=data)

    try:
        print("🧾 IBM Response Text:", response.text)
        result = response.json()

        if "results" in result:
            return {"career_path": result["results"][0]["generated_text"]}
        else:
            return {"career_path": f"⚠️ Unexpected response from IBM API: {result}"}

    except Exception as e:
        return {"career_path": f"❌ Error parsing response: {str(e)}"}
