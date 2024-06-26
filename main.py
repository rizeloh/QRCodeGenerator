import qrcode


def generate_qr_code(data, file_path):
    """
    Generates a QR code for the given data and saves it to the specified file path.

    Parameters:
    data (str): The data to encode in the QR code.
    file_path (str): The path where the QR code image will be saved.

    Returns:
    None
    """
    # Create a QR Code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in pixels
        border=4,  # Thickness of the border (minimum is 4)
    )

    # Add data to the QR Code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill='black', back_color='white')

    # Save the image to the specified file path
    img.save(file_path)


if __name__ == "__main__":
    # Example data to encode
    data = input("Input Your data: ")

    # File path to save the QR code image
    file_path = "qrcode.png"

    # Generate and save the QR code
    generate_qr_code(data, file_path)

    print(f"QR code generated and saved to {file_path}")
