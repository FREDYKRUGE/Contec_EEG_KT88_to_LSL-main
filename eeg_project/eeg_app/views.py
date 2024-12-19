from django.shortcuts import render
from pylsl import StreamInlet, resolve_stream

def display_eeg_data(request):
    try:
        # Resolve the EEG stream
        streams = resolve_stream('type', 'EEG')
        if not streams:
            return render(request, 'eeg_app/eeg_data.html', {'error': 'No EEG streams found.'})

        # Create an inlet and pull a sample
        inlet = StreamInlet(streams[0])
        sample, timestamp = inlet.pull_sample(timeout=5.0)

        if sample is None:
            return render(request, 'eeg_app/eeg_data.html', {'error': 'No EEG data available.'})

        # Channel names
        channel_names = ['Fp1', 'Fp2', 'F3', 'F4', 'C3', 'C4', 'P3', 'P4', 'O1', 'O2',
                         'F7', 'F8', 'T3', 'T4', 'T5', 'T6', 'Fz', 'Pz', 'Cz', 'Pg1', 'Pg2',
                         'EOGR', 'EOOGL', 'EMG', 'BR', 'ECG']

        # Split data into two lists
        left_table_data = zip(channel_names[:len(sample)//2], sample[:len(sample)//2])
        right_table_data = zip(channel_names[len(sample)//2:], sample[len(sample)//2:])

        # Prepare data for the template
        context = {
            'timestamp': timestamp,
            'left_table_data': left_table_data,
            'right_table_data': right_table_data,
        }
        return render(request, 'eeg_app/eeg_data.html', context)
    except Exception as e:
        return render(request, 'eeg_app/eeg_data.html', {'error': f"An error occurred: {e}"})
