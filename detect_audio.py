from pydub import AudioSegment
import numpy as np

# Function to detect quarter beats in the audio
def detect_quarter_beats(audio_file_path, output_txt_path):
    # Load the audio file
    audio = AudioSegment.from_file(audio_file_path)

    # Convert audio to mono if it's stereo
    if audio.channels > 1:
        audio = audio.set_channels(1)

    # Calculate the sample rate
    sample_rate = audio.frame_rate

    # Convert audio to numpy array
    audio_data = np.array(audio.get_array_of_samples())

    # Define a threshold for note detection (adjust as needed)
    threshold = 1000

    # Find quarter beats
    quarter_beats = []
    for i in range(0, len(audio_data), sample_rate // 4):
        segment = audio_data[i:i + sample_rate // 4]
        if np.max(np.abs(segment)) > threshold:
            quarter_beats.append(i / sample_rate)

    # Write the quarter beats to a text file
    with open(output_txt_path, 'w') as txt_file:
        for beat_time in quarter_beats:
            txt_file.write(f"{beat_time:.2f}\n")

# if __name__ == "__main__":
audio_file_path = "test_map.mp3"  # Replace with your audio file path
output_txt_path = "audio_test.txt"    # Replace with the desired output file path

detect_quarter_beats(audio_file_path, output_txt_path)
print("Quarter beats detected and saved to quarter_beats.txt")
