import wave
import audioop

def vad(audio_file, threshold=500, buffer_size=1024):
    """
    Perform Voice Activity Detection (VAD) on a WAV audio file.

    Parameters:
        audio_file (str): Path to the audio file.
        threshold (int): Energy threshold to detect speech.
        buffer_size (int): Number of frames to read at a time.

    Returns:
        list of tuples: Detected speech segments as (start_time, end_time).
    """
    # Open the audio file
    audio = wave.open(audio_file, 'rb')
    frame_rate = audio.getframerate()
    sample_width = audio.getsampwidth()

    speech_segments = []
    start_time = None

    while True:
        frames = audio.readframes(buffer_size)
        if not frames:
            # End of file
            if start_time is not None:
                # Handle last segment
                end_time = audio.tell() / frame_rate
                speech_segments.append((start_time, end_time))
            break

        # Calculate the energy of the current frame
        energy = audioop.rms(frames, sample_width)

        if energy > threshold:
            if start_time is None:
                # Start of a new speech segment
                start_time = audio.tell() / frame_rate - (len(frames) / frame_rate)
        else:
            if start_time is not None:
                # End of current speech segment
                end_time = audio.tell() / frame_rate
                speech_segments.append((start_time, end_time))
                start_time = None

    # Close the audio file
    audio.close()
    return speech_segments


# Example usage
if __name__ == "__main__":
    audio_file = 'sample.wav'
    detected_segments = vad(audio_file)

    if detected_segments:
        print("Detected Speech Segments:")
        for i, (start, end) in enumerate(detected_segments, start=1):
            print(f"Segment {i}: {start:.2f}s - {end:.2f}s")
    else:
        print("No speech detected.")
