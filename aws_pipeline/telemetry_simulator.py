import json, time, random

def generate_fake_telemetry():
    return {
        'machine_id': 'M123',
        'temperature': round(random.uniform(65, 85), 2),
        'vibration': round(random.uniform(0.1, 0.8), 3),
        'rpm': random.randint(1500, 2000),
        'timestamp': time.time()
    }

while True:
    print(json.dumps(generate_fake_telemetry()))
    time.sleep(10)