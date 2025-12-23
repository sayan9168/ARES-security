from flask import Flask, render_template_string
import os

ALERT_LOG = "logs/alerts.log"

app = Flask(__name__)

HTML = """
<!doctype html>
<html>
<head>
  <title>ARES Dashboard</title>
  <style>
    body { font-family: Arial; background:#0f172a; color:#e5e7eb; padding:20px; }
    h1 { color:#38bdf8; }
    .card { background:#020617; padding:15px; border-radius:10px; margin-bottom:15px; }
    .high { color:#f87171; }
    .info { color:#34d399; }
    small { color:#94a3b8; }
  </style>
</head>
<body>
  <h1>ARES – Security Dashboard</h1>

  <div class="card">
    <h3>Recent Alerts</h3>
    {% if alerts %}
      <ul>
        {% for a in alerts %}
          <li class="high">{{ a }}</li>
        {% endfor %}
      </ul>
    {% else %}
      <small>No alerts found</small>
    {% endif %}
  </div>

  <div class="card">
    <h3>Status</h3>
    <p class="info">System running normally</p>
  </div>
</body>
</html>
"""

def read_alerts():
    if not os.path.exists(ALERT_LOG):
        return []
    with open(ALERT_LOG) as f:
        lines = f.readlines()
    return [l.strip() for l in lines[-10:]]

@app.route("/")
def index():
    alerts = read_alerts()
    return render_template_string(HTML, alerts=alerts)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
