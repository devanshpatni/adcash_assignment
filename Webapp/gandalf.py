from flask import Flask, render_template    # Importing important modules for Server,
from datetime import datetime               # Time,
import pytz                                 # Timezone
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST  # Prometheus Client                            

app = Flask(__name__)

request_hits = Counter("endpoint_requested", "Total Number of times endpoint is requested", ["URI"])


# Route for Gandalf Image
@app.route("/gandalf")
def wizard():
    request_hits.labels(URI="/gandalf").inc() # incrementing counter
    return render_template("gandalf.html")    # Rendering Template

# Route for colombo time
@app.route("/colombo")
def colombo():
    request_hits.labels(URI="/colombo").inc()                       # incrementing counter
    colombo_timeZone = pytz.timezone("Asia/Colombo")                # Colombo Timezone
    time = datetime.now(colombo_timeZone).strftime("%I:%M:%S %p")   # Current TIme in Colombo
    return render_template("colombo.html" , time=time)

# Metrics path for prometheus
@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}  # Generating data for prometheus exporter

if __name__ == "__main__":
    app.run('0.0.0.0',port=80)