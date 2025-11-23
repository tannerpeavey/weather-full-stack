from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/weather")
def weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "City parameter is required"}), 400

    url = f"https://wttr.in/{city}?format=j1"
    try:
        response = requests.get(url, timeout=10)  # 10 second timeout
        data = response.json()

        return jsonify({
            "area": data["nearest_area"][0]["areaName"][0]["value"],
            "region": data["nearest_area"][0]["region"][0]["value"],
            "country": data["nearest_area"][0]["country"][0]["value"],
            "temp_F": data["current_condition"][0]["temp_F"],
            "desc": data["current_condition"][0]["weatherDesc"][0]["value"]
        })

    except requests.exceptions.RequestException as e:
        # Return a clean error instead of crashing
        return jsonify({"error": "Failed to reach weather service", "details": str(e)}), 502

if __name__ == "__main__":
    app.run(debug=True)
