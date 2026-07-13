from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app) # Allows your website to securely talk to this backend

# BIMS Hospital Knowledge Base
HOSPITAL_DATA = {
    "contact": "You can reach BIMS Hospital at 0278-6644 444 or 0278-6644 445. For mobile inquiries, call 072279 89828.",
    "emergency": "For 24/7 Emergency & Ambulance services, immediately call 0278-6644 444 or 0278-6644 446.",
    "location": "BIMS Hospital is located at Jail Road, Opposite Sir T Hospital, Panwadi, Bhavnagar, Gujarat - 364001.",
    "email": "You can email us at info@bimshospital.com.",
    "specialties": "We specialize in Cardiology, Cardiovascular Surgery, Neurosurgery, Neurology, Medical/Surgical Oncology, Urosurgery, Nephrology (with Dialysis), Robotic Joint Replacement, Spine Surgery, Sports Injury, and Laparoscopic GI Surgery.",
    "appointment": "To book an appointment, please visit our 'Book Appointment' page on the website or call our reception desk at 0278-6644 444.",
    "doctors": "Our expert team includes Dr. Ajay Krishnan (Spine), Dr. Sanjiv Ravisaheb (Robotic Joint Replacement), Dr. Bharat Dabhi (Physician), Dr. Snehal Ravisaheb (Gynecology), and Dr. Harshvardhan Jadeja (Sports Medicine)."
}

def get_bot_response(user_message):
    msg = user_message.lower()
    
    if re.search(r'(hi|hello|hey|greetings)', msg):
        return "Hello! Welcome to BIMS Hospital Support. How can I assist you today?"
    elif re.search(r'(emergency|accident|ambulance|serious)', msg):
        return f"🚨 EMERGENCY: {HOSPITAL_DATA['emergency']}"
    elif re.search(r'(appointment|book|opd|consult)', msg):
        return HOSPITAL_DATA["appointment"]
    elif re.search(r'(where|location|address|address|map|situated)', msg):
        return f"📍 Location: {HOSPITAL_DATA['location']}"
    elif re.search(r'(phone|call|contact|number|mobile)', msg):
        return HOSPITAL_DATA["contact"]
    elif re.search(r'(doctor|specialist|surgeon)', msg):
        return f"Our doctors include: {HOSPITAL_DATA['doctors']}"
    elif re.search(r'(specialty|specialities|department|treat|cardio|ortho|neuro)', msg):
        return f"Our major departments include: {HOSPITAL_DATA['specialties']}"
    elif re.search(r'(email|mail)', msg):
        return f"📧 {HOSPITAL_DATA['email']}"
    else:
        return "I'm sorry, I didn't quite catch that. You can ask me about appointments, emergency numbers, location, or available medical specialties. Alternatively, please call our reception at 0278-6644 444."

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    if not user_message:
        return jsonify({"response": "Please say something!"}), 400
    
    bot_reply = get_bot_response(user_message)
    return jsonify({"response": bot_reply})

if __name__ == '__main__':
    # Run server locally. Change to 0.0.0.0 for live hosting.
    app.run(port=5000, debug=True)