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

        # Prepare data for the template
        context = {
            'timestamp': timestamp,
            'sample': sample,
        }
        return render(request, 'eeg_app/eeg_data.html', context)
    except Exception as e:
        return render(request, 'eeg_app/eeg_data.html', {'error': f"An error occurred: {e}"})
