import base64
import logging
from base64 import b64encode
import pytesseract
from .models import *
from Crypto.Cipher import AES


class AesAlgorithm:
    img = None
    key = None

    def __init__(self, image):
        self.img = image

    def hash_patient_id(self, patient):
        self.key = patient.to_bytes(2, 'big') + b'NUuRJbL0UMp8+UMCk2/vQA'

    def aes_encoding(self, patient):
        initial_value = patient.to_bytes(2, 'big') + b'NUuRJb'

        self.hash_patient_id(patient)

        cipher = AES.new(self.key, AES.MODE_OFB, b'agekmtpkHERLWIRJ')

        cipher_text = cipher.encrypt(self.img)

        hash_value = patient.to_bytes(2, 'big') + b'NUuRJbL0UMp8NUuRJbL0UMp8+UMCk2/vQA'

        MedicalImage.objects.filter(
            patient_id=patient
        ).update(
            hash_cipher={
                "cipher encryption": cipher_text,
                "hash value": + hash_value,
            }
        )

    def aes_decryption(self, patient):
        try:
            initial_value = patient.to_bytes(2, 'big') + b'NUuRJb'

            self.hash_patient_id(patient)

            cipher = AES.new(self.key, AES.MODE_OFB, b'agekmtpkHERLWIRJ')

            bit_value = b'NUuRJbL0UMp8NUuRJbL0UMp8+UMCk2/vQA'

            if (patient.to_bytes(2, 'big') + bit_value) == MedicalImage.objects.filter(
                    patient__exact=patient
            ).values_list(
                'hash_cypher',
                flat=True
            ).get(
                'hash value'
            ):
                decryption_text = MedicalImage.hash_cypher.get('cipher encryption')
                cipher_text = cipher.decrypt(decryption_text)

        except (ValueError, KeyError):
            logging.error("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            logging.error("Incorrect decryption")
            logging.error("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
