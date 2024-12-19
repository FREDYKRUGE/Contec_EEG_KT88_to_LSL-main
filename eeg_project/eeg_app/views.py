from django.shortcuts import render
from pylsl import StreamInlet, resolve_stream
from datetime import datetime, timezone

def display_eeg_data(request):
    try:
        # Resolve the EEG stream
        streams = resolve_stream('type', 'EEG')
        if not streams:
            return render(request, 'eeg_app/eeg_data.html', {'error': 'No EEG streams found.'})

        # Create an inlet and pull a sample
        inlet = StreamInlet(streams[0])
        sample, lsl_timestamp = inlet.pull_sample(timeout=5.0)

        # Get the current system time in local timezone
        current_time = datetime.now()  # Local system time
        current_readable_timestamp = current_time.strftime('%Y-%m-%d %H:%M:%S')

        # Prepare channel names
        channels = [
            'Fp1', 'Fp2', 'F3', 'F4', 'C3', 'C4', 'P3', 'P4', 'O1', 'O2',
            'F7', 'F8', 'T3', 'T4', 'T5', 'T6', 'Fz', 'Pz', 'Cz', 'Pg1',
            'Pg2', 'EOGR', 'EOOGL', 'EMG', 'BR', 'ECG'
        ]

        # Split the data for left and right tables
        left_table_data = zip(channels[:len(channels) // 2], sample[:len(channels) // 2])
        right_table_data = zip(channels[len(channels) // 2:], sample[len(channels) // 2:])

        # Prepare data for the template
        context = {
            'current_readable_timestamp': current_readable_timestamp,
            'lsl_raw_timestamp': lsl_timestamp,
            'left_table_data': left_table_data,
            'right_table_data': right_table_data,
        }
        return render(request, 'eeg_app/eeg_data.html', context)
    except Exception as e:
        return render(request, 'eeg_app/eeg_data.html', {'error': f"An error occurred: {e}"})
