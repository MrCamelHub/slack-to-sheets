# YouTube Video Analysis Pipeline

This project implements a pipeline that:
1. Downloads YouTube videos
2. Extracts frames at regular intervals
3. Analyzes the frames using GPT-4 Vision API
4. Provides a detailed summary of the video content

## Prerequisites

- Python 3.8 or higher
- OpenAI API key with access to GPT-4 Vision API
- Required Python packages (listed in requirements.txt)

## Installation

1. Clone this repository
2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the script:
```bash
python main.py
```

When prompted, enter the YouTube video URL you want to analyze.

## Features

- Automatic video download using pytube
- Frame extraction at configurable intervals
- GPT-4 Vision API integration for video analysis
- Detailed summary generation of video content

## Notes

- The script creates a temporary directory to store downloaded videos
- Frame extraction interval can be adjusted in the code (default: every 30 frames)
- Make sure you have sufficient API credits for GPT-4 Vision API usage

## Error Handling

The script includes basic error handling for:
- Video download failures
- Frame extraction issues
- API communication problems

## License

MIT License 