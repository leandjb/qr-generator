import qrcode
from datetime import date


def get_name_date():
    return "QR_" + str(date.today().isoformat()) + ".png"


class MyQR:
    def __init__(self, size: int, padding: int):
        self.size = size
        self.padding = padding
        self.qr = qrcode.QRCode(box_size=size, border=padding)

    def create_qr(self, filename: str, fg_color: str, bg_color: str, text: str):
        user_input = input('Enter URL:')

        try:
            if not user_input:
                print("Error: Please enter a valid text.")
                return

            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fill_color=fg_color,
                                          back_color=bg_color)
            qr_image.save(filename)
            print('QR code created successfully!')
        except Exception as e:
            print("Error: ", e)


def main():
    myqr = MyQR(10, 4)
    myqr.create_qr(get_name_date(), 'black', 'blue',
                   text='https://www.inter.it/')


if __name__ == '__main__':
    main()
