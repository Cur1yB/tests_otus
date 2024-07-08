import unittest
from unittest.mock import Mock
from email_example import EmailService

class TestEmailService(unittest.TestCase):

    def setUp(self):
        # Создаем mock-объект для smtp_client
        self.smtp_client = Mock()
        self.service = EmailService(self.smtp_client)

    def test_send_email(self):
        # Определяем параметры для теста
        recipient = "test@example.com"
        subject = "Test Subject"
        body = "This is a test email."

        # Вызываем метод send_email
        self.service.send_email(recipient, subject, body)

        # Проверяем, что метод send_message был вызван с правильными параметрами
        self.smtp_client.send_message.assert_called_with({
            "to": recipient,
            "subject": subject,
            "body": body
        })

if __name__ == "__main__":
    unittest.main()