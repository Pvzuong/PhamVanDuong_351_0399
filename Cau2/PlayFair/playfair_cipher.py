class PlayFairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        key = ''.join(ch for ch in key.upper() if ch.isalpha())
        key = key.replace("J", "I")

        matrix_chars = []
        for ch in key:
            if ch not in matrix_chars:
                matrix_chars.append(ch)

        for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
            if ch not in matrix_chars:
                matrix_chars.append(ch)

        return [matrix_chars[i:i+5] for i in range(0, 25, 5)]

    def find_letter_coords(self, matrix, letter):
        letter = letter.upper().replace("J", "I")
        for r in range(5):
            for c in range(5):
                if matrix[r][c] == letter:
                    return r, c
        return None

    def _prepare_text(self, text):
        text = ''.join(ch for ch in text.upper() if ch.isalpha())
        text = text.replace("J", "I")

        result = ""
        i = 0
        while i < len(text):
            a = text[i]
            b = text[i + 1] if i + 1 < len(text) else "X"

            if a == b:
                result += a + "X"
                i += 1
            else:
                result += a + b
                i += 2

        if len(result) % 2 != 0:
            result += "X"

        return result

    def playfair_encrypt(self, plain_text, matrix):
        plain_text = self._prepare_text(plain_text)
        encrypted = ""

        for i in range(0, len(plain_text), 2):
            a, b = plain_text[i], plain_text[i + 1]

            r1, c1 = self.find_letter_coords(matrix, a)
            r2, c2 = self.find_letter_coords(matrix, b)

            if r1 == r2:
                encrypted += matrix[r1][(c1 + 1) % 5]
                encrypted += matrix[r2][(c2 + 1) % 5]
            elif c1 == c2:
                encrypted += matrix[(r1 + 1) % 5][c1]
                encrypted += matrix[(r2 + 1) % 5][c2]
            else:
                encrypted += matrix[r1][c2]
                encrypted += matrix[r2][c1]

        return encrypted

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = ''.join(ch for ch in cipher_text.upper() if ch.isalpha())

        decrypted = ""

        for i in range(0, len(cipher_text), 2):
            a, b = cipher_text[i], cipher_text[i + 1]

            r1, c1 = self.find_letter_coords(matrix, a)
            r2, c2 = self.find_letter_coords(matrix, b)

            if r1 == r2:
                decrypted += matrix[r1][(c1 - 1) % 5]
                decrypted += matrix[r2][(c2 - 1) % 5]
            elif c1 == c2:
                decrypted += matrix[(r1 - 1) % 5][c1]
                decrypted += matrix[(r2 - 1) % 5][c2]
            else:
                decrypted += matrix[r1][c2]
                decrypted += matrix[r2][c1]

        return decrypted
