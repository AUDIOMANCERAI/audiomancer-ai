from flask import Flask, jsonify
from flask_cors import CORS

# 1. CORE APPLICATION INSTANCE
app = Flask(__name__) 

# CRITICAL: Replace 'YOUR_VERCEL_FRONTEND_URL' with your actual public Vercel URL
CORS(app, resources={r"/*": {"origins": "https://vercel.com/mike-hutchings-projects/audiomancer-aii/8rw89P8aayLg8WWggpoMxJAjLbBC"}})

# 2. SIMPLE ROOT ROUTE
@app.route('/', methods=['GET'])
def home():
    return "Audiomancer Backend is Running! (Clean Version)", 200

# 3. PLACEHOLDER API ENDPOINT 
@app.route('/mix_tracks', methods=['POST'])
def mix_tracks():
    return jsonify({"message": "Backend connected successfully. Ready for further logic."}), 200

# 4. LOCAL RUNNER
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)