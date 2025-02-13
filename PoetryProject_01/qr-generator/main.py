import qrcode
import uuid
from faker import Faker
from pathlib import Path
from datetime import datetime

fake = Faker()

class QRGenerator:
    def __init__(self, output_dir="qrcodes"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def generate_qr_code(self, data=None):
        unique_id = str(uuid.uuid4())

        if data is None:
            data = {
                "name": fake.name(),
                "id": unique_id,
                "email": fake.email(),
                "phone": fake.phone_number(),
                "address": fake.address(),
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4)
        qr.add_data(str(data))
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        filename = f"{unique_id}.png"
        filepath = self.output_dir / filename
        img.save(filepath)

        return filepath

# Move these outside the class
def main():
    qr_generator = QRGenerator()
    filepath = qr_generator.generate_qr_code()
    print(f"QR code saved to {filepath}")

if __name__ == "__main__":
    main()
