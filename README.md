# av1-converter
This tool allows users to convert MP4 files to the AV1 format using `ffmpeg` and then calculates the VMAF and PSNR scores for the output
## Prerequisites

- **AWS CLI**: Ensure that it's set up and configured with the necessary credentials.
- **Python**: The project uses Python 3.x.
- **FFmpeg**: Necessary for video conversion.

## Setup & Installation

1. **Clone the Repository**:

``` git clone https://github.com/hoichoi-opensource/av1-converter/ ```

2. **Navigate into the Project Directory**:

   ``` cd av1-converter ```

3. **Install Required Python Packages**:

``` pip install flask boto3 ```

4. **Configuration**: Edit `config.py` with your appropriate AWS details and customize FFmpeg parameters if necessary.

5. **Run the Flask Application**:

``` python app.py ```

6. **Access the Web Interface**: Open your preferred web browser and navigate to:

``` http://127.0.0.1:5000/ ```

## Usage

1. **File Input**: In the web interface, input the filename from your source S3 bucket.
2. **Conversion**: Click on the "Convert" button.
3. **Completion**: Wait for the conversion to finish. Once done, the converted file will be uploaded back to the designated S3 bucket, retaining the original filename for easy identification.

## Contributing

Contributions to improve the tool are welcome! For significant changes, kindly open an issue first to discuss your proposed updates or enhancements.

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
