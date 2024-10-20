import random
import numpy as np
import csv

# Time segments (in minutes)
relaxing_time = 10
exercising_time = 20
resting_time = 10
sleeping_time = 10
walking_time = 10

# Transition time between activities (in seconds)
transition_time = 60  # 1 minute for smooth transition

# Function to generate BPM based on activity
def generate_bpm(activity, duration, bpm_range):
    return [random.randint(bpm_range[0], bpm_range[1]) for _ in range(duration * 60)]

# Function to create a smooth transition between two BPM ranges
def smooth_transition(bpm_start, bpm_end, duration):
    return np.linspace(bpm_start, bpm_end, duration).tolist()

# BPM ranges for each activity
bpm_ranges = {
    'relaxing': (60, 80),
    'exercising': (120, 160),
    'resting': (60, 80),
    'sleeping': (50, 70),
    'walking': (80, 110)
}

# Generate BPM data for each activity phase
bpm_relaxing = generate_bpm('relaxing', relaxing_time, bpm_ranges['relaxing'])
bpm_exercising = generate_bpm('exercising', exercising_time, bpm_ranges['exercising'])
bpm_resting = generate_bpm('resting', resting_time, bpm_ranges['resting'])
bpm_sleeping = generate_bpm('sleeping', sleeping_time, bpm_ranges['sleeping'])
bpm_walking = generate_bpm('walking', walking_time, bpm_ranges['walking'])

# Gradual transitions between activities
transition_relaxing_to_exercising = smooth_transition(bpm_relaxing[-1], bpm_exercising[0], transition_time)
transition_exercising_to_resting = smooth_transition(bpm_exercising[-1], bpm_resting[0], transition_time)
transition_resting_to_sleeping = smooth_transition(bpm_resting[-1], bpm_sleeping[0], transition_time)
transition_sleeping_to_walking = smooth_transition(bpm_sleeping[-1], bpm_walking[0], transition_time)

# Combine BPM data with transitions
bpm_data = (
    bpm_relaxing +
    transition_relaxing_to_exercising +
    bpm_exercising +
    transition_exercising_to_resting +
    bpm_resting +
    transition_resting_to_sleeping +
    bpm_sleeping +
    transition_sleeping_to_walking +
    bpm_walking
)

# Save data to a CSV file with integer values
with open('heart_rate_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['BPM'])  # Write the header
    for bpm in bpm_data:
        writer.writerow([int(round(bpm))])  # Write each BPM value as an integer

print("Heart rate data has been saved to 'heart_rate_data.csv'.")
