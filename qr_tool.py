
"""qrCode.ipynb
Original file: https://colab.research.google.com/drive/1UB1-61O9fDrOOJm7eLNrP59uFEhN235o
"""

# qr_tool.py - Simple QR Code Generator & Scanner

import qrcode
from pyzbar import pyzbar
import cv2
import os


class QRCodeGenerator:
    """Simple QR Code Generator"""

    def __init__(self):
        self.ec_levels = {
            'L': qrcode.constants.ERROR_CORRECT_L,    
            'M': qrcode.constants.ERROR_CORRECT_M,    
            'Q': qrcode.constants.ERROR_CORRECT_Q,    
            'H': qrcode.constants.ERROR_CORRECT_H  
        }

    def generate(self, data, filename='qr_code.png', error_correction='M',
                 box_size=10, border=4):
        try:
            qr = qrcode.QRCode(
                version=None,  #1-40; determines the size
                error_correction=self.ec_levels.get(error_correction,
                                                    qrcode.constants.ERROR_CORRECT_M),
                box_size=box_size,
                border=border,
            )

            # Add data
            qr.add_data(data)
            qr.make(fit=True)

            # Create image
            img = qr.make_image(fill_color="black", back_color="white")

            # Save image
            img.save(filename)

            print(f"\n QR code generated successfully!")
            print(f"  File: {filename}")
            print(f"  Version: {qr.version}")
            print(f"  Size: {qr.modules_count}x{qr.modules_count} modules")
            print(f"  Error Correction: {error_correction} ({['7%', '15%', '25%', '30%'][['L','M','Q','H'].index(error_correction)]})")

            return filename

        except Exception as e:
            print(f"\n Error generating QR code: {e}")
            return None


class QRCodeScanner:
    """Simple QR Code Scanner"""

    def scan(self, filename):
        try:
            if not os.path.exists(filename):
                print(f"\n File not found: {filename}")
                return []

            # Read image
            img = cv2.imread(filename)

            if img is None:
                print(f"\n Could not read image: {filename}")
                return []

            # Decode QR codes
            decoded_objects = pyzbar.decode(img)

            if not decoded_objects:
                print("\n No QR code found in the image")
                return []

            # Extract results
            results = []
            for i, obj in enumerate(decoded_objects, 1):
                data = obj.data.decode('utf-8')
                qr_type = obj.type
                rect = obj.rect

                result = {
                    'data': data,
                    'type': qr_type,
                    'position': (rect.left, rect.top, rect.width, rect.height)
                }
                results.append(result)

                print(f"--- QR Code #{i} ---")
                print(f"Type: {qr_type}")
                print(f"Data: {data}")
                print(f"Position: x={rect.left}, y={rect.top}")
                print(f"Size: {rect.width}x{rect.height} pixels")
                print()

            return results

        except Exception as e:
            print(f"\n Error scanning QR code: {e}")
            return []


def print_header():
    """Print application header"""
    print("\n" + "=" * 60)
    print(" " * 15 + "QR CODE GENERATOR & SCANNER")
    print("=" * 60)


def print_menu():
    """Print main menu"""
    print("\n" + "=" * 60)
    print("MAIN MENU")
    print("-" * 60)
    print("1. Generate QR Code")
    print("2. Scan QR Code from Image")
    print("3. Exit")
    print("-" * 60)


def generate_qr_menu(generator):
    """Handle QR code generation"""
    print("\n" + "=" * 60)
    print("QR CODE GENERATOR")
    print("=" * 60)

    # Get data
    data = input("\nEnter data to encode: ").strip()

    if not data:
        print("Data cannot be empty.")
        return

    # Get filename
    filename = input("Enter output filename (press Enter for 'qr_code.png'): ").strip()
    if not filename:
        filename = "qr_code.png"

    # Ensure .png extension
    if not filename.lower().endswith('.png'):
        filename += '.png'

    # Generating the qr
    print("\nGenerating QR code...")
    result = generator.generate(data, filename)

    if result:
        print(f"\n SUCCESS! QR code saved to: {os.path.abspath(filename)}")


def scan_qr_menu(scanner):
    """Handle QR code scanning"""
    print("\n" + "=" * 60)
    print("QR CODE SCANNER")
    print("=" * 60)

    # Get filename
    filename = input("\nEnter image filename to scan: ").strip()

    if not filename:
        print(" Filename cannot be empty.")
        return

    # Check if file exists
    if not os.path.exists(filename):
        print(f" File not found: {filename}")
        print(f"   Looking in: {os.path.abspath('.')}")
        return

    # Scan
    print(f"\nScanning {filename}...")
    results = scanner.scan(filename)

    if results:
        print("=" * 60)
        print("SCAN RESULTS")
        print("=" * 60)

        for i, result in enumerate(results, 1):
            print(f"\nQR Code #{i}:")
            print(f"  Decoded Data: {result['data']}")
            print(f"  Type: {result['type']}")

        print("\n" + "=" * 60)
        print(f"✓ Successfully decoded {len(results)} QR code(s)!")
        print("=" * 60)


def main():
    """Main application loop"""
    generator = QRCodeGenerator()
    scanner = QRCodeScanner()

    print_header()

    while True:
        print_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            generate_qr_menu(generator)

        elif choice == '2':
            scan_qr_menu(scanner)

        elif choice == '3':
            print("\n" + "=" * 60)
            print("Thank you for using QR Code Tool!")
            print("=" * 60 + "\n")
            break

        else:
            print("\n Invalid choice! Please enter 1, 2, or 3.")


if __name__ == '__main__':
    main()
