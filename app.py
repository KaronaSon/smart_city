from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Knowledge base for smart city domains with rules
smart_city_domains = {
    "smart_governance": [
        {"condition": "engagement < 50", "action": "Increase Community Outreach"},
        {"condition": "engagement >= 50", "action": "Governance is Effective"}
    ],
    "smart_economy": [
        {"condition": "growth_rate < 2", "action": "Implement Economic Stimulus"},
        {"condition": "growth_rate >= 2", "action": "Economy is Stable"}
    ],
    "smart_mobility": [
        {"condition": "traffic > 80", "action": "Activate Redirection Plan"},
        {"condition": "traffic <= 80 and traffic > 50", "action": "Moderate Traffic Alerts"},
        {"condition": "traffic <= 50", "action": "Traffic is Smooth"}
    ],
    "smart_environment": [
        {"condition": "air_quality > 100", "action": "Issue Pollution Warning"},
        {"condition": "air_quality <= 100", "action": "Environment is Healthy"}
    ],
    "smart_living": [
        {"condition": "healthcare < 70", "action": "Expand Healthcare Services"},
        {"condition": "healthcare >= 70", "action": "Living Standards are Good"}
    ],
    "smart_people": [
        {"condition": "education < 60", "action": "Invest in Education Programs"},
        {"condition": "education >= 60", "action": "Community is Educated"}
    ]
}

# Generate real-time data simulation
def generate_city_data():
    return {
        "traffic": random.randint(0, 100),
        "engagement": random.randint(0, 100),
        "growth_rate": random.uniform(0, 5),
        "air_quality": random.randint(0, 200),
        "healthcare": random.randint(0, 100),
        "education": random.randint(0, 100)
    }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/city-data', methods=['GET'])
def get_city_data():
    data = generate_city_data()
    actions = {}

    for domain, rules in smart_city_domains.items():
        for rule in rules:
            if eval(rule["condition"], {}, data):
                actions[domain] = rule["action"]
                break

    response = {"data": data, "actions": actions}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
