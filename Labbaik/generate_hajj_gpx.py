import math
import datetime

# --- Configuration ---
KAABA_LAT, KAABA_LNG = 21.422487, 39.826206
SAFA_LAT, SAFA_LNG = 21.421877, 39.828608
MARWA_LAT, MARWA_LNG = 21.425263, 39.825889

# Settings
TAWAF_RADIUS_METERS = 80  # Realistic distance from Kaaba (was 45, increased for better testing)
WALKING_SPEED_MPS = 1.4   # ~5 km/h

def create_gpx_header():
    return '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n' \
           '<gpx version="1.1" creator="HajjSimulator">\n' \
           '<trk>\n<name>Hajj Simulation</name>\n<trkseg>\n'

def create_gpx_footer():
    return '</trkseg>\n</trk>\n</gpx>'

def meters_to_lat_degrees(meters):
    return meters / 111320.0

def meters_to_lng_degrees(meters, lat):
    return meters / (40075000.0 * math.cos(math.radians(lat)) / 360.0)

def generate_tawaf_gpx(filename):
    with open(filename, 'w') as f:
        f.write(create_gpx_header())
        
        start_time = datetime.datetime.now()
        # 7 Laps - COUNTER-CLOCKWISE (Islamic requirement)
        for lap in range(7):
            # Start at 0° (North) and go counter-clockwise to 360°
            # FIXED: Changed to range(360, 0, -5) for counter-clockwise
            for angle in range(0, 360, 5):
                # For counter-clockwise, we negate the angle
                rad = math.radians(-angle)  # Negative for counter-clockwise
                d_lat = meters_to_lat_degrees(TAWAF_RADIUS_METERS * math.sin(rad))
                d_lng = meters_to_lng_degrees(TAWAF_RADIUS_METERS * math.cos(rad), KAABA_LAT)
                
                lat = KAABA_LAT + d_lat
                lng = KAABA_LNG + d_lng
                
                # Timestamp (important for speed simulation)
                # Circumference = 2*pi*r ≈ 502m (at 80m radius). 5 degrees ≈ 7m. Time = 7/1.4 ≈ 5 sec
                time_offset = (lap * 360 + angle) / 5 * 5
                point_time = start_time + datetime.timedelta(seconds=time_offset)
                time_str = point_time.strftime("%Y-%m-%dT%H:%M:%SZ")
                
                f.write(f'<trkpt lat="{lat:.7f}" lon="{lng:.7f}">\n'
                        f'  <time>{time_str}</time>\n'
                        f'</trkpt>\n')
        
        f.write(create_gpx_footer())
    print(f"Generated {filename}")
    print(f"  - 7 laps counter-clockwise around Kaaba")
    print(f"  - Radius: {TAWAF_RADIUS_METERS}m")
    print(f"  - Total points: {7 * 72}")

def generate_sai_gpx(filename):
    with open(filename, 'w') as f:
        f.write(create_gpx_header())
        start_time = datetime.datetime.now()
        current_seconds = 0
        
        # 7 Trips (Safa -> Marwa is 1, Marwa -> Safa is 2, etc.)
        points = [
            (SAFA_LAT, SAFA_LNG), 
            (MARWA_LAT, MARWA_LNG)
        ]
        
        steps = 40  # Number of points between hills for smoothness
        
        for trip in range(7):
            start_idx = trip % 2
            end_idx = (trip + 1) % 2
            
            p1 = points[start_idx]
            p2 = points[end_idx]
            
            # Add a pause at the start of each trip (simulating reaching the hill)
            if trip > 0:
                current_seconds += 5  # 5 second pause
            
            for i in range(steps + 1):
                t = i / steps
                lat = p1[0] + (p2[0] - p1[0]) * t
                lng = p1[1] + (p2[1] - p1[1]) * t
                
                # Distance approx 450m. Each step ~11m. Time ~8 sec
                current_seconds += 8
                point_time = start_time + datetime.timedelta(seconds=current_seconds)
                time_str = point_time.strftime("%Y-%m-%dT%H:%M:%SZ")
                
                f.write(f'<trkpt lat="{lat:.7f}" lon="{lng:.7f}">\n'
                        f'  <time>{time_str}</time>\n'
                        f'</trkpt>\n')

        f.write(create_gpx_footer())
    print(f"Generated {filename}")
    print(f"  - 7 trips between Safa and Marwa")
    print(f"  - Total points: {7 * (steps + 1)}")

if __name__ == "__main__":
    print("Generating Hajj GPS simulation files...\n")
    generate_tawaf_gpx("tawaf_test.gpx")
    print()
    generate_sai_gpx("sai_test.gpx")
    print("\n✅ Done! Use these GPX files to test the ritual tracker.")
    print("\nHow to use:")
    print("  1. Load GPX file in iOS Simulator or Android Emulator")
    print("  2. Enable GPS auto-tracking in the app")
    print("  3. Play the GPX route and watch the counter increment!")