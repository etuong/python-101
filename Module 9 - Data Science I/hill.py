import numpy as np

modulus = 26


class MatrixNotInvertible(Exception):
    pass


def is_square(K):
    """
    Check if a matrix is square
    """
    return K.shape[0] == K.shape[1]


def determinant(K):
    """
    Accepts a matrix, calculates and returns its determinant
    """
    return int(np.linalg.det(K))


def invertible(K) -> bool:
    """
    Calls determinant() and returns True if the matrix is invertible and False otherwise
    """
    return False if determinant(K) == 0 else True


def mod_inverse(a):
    """
    Accepts a number n (determinant) and a modulus m and returns the modular multiplicative inverse of n modulo m
    """
    for x in range(1, modulus):
        if ((a % modulus) * (x % modulus)) % modulus == 1:
            return x
    return -1


def matrix_to_text(C):
    """
    Get cipher text from matrix by decoding ASCII
    """
    cipher_text = ""
    for i in range(C.shape[0]):
        for j in range(C.shape[1]):
            cipher_text += (chr(C[i, j] + 65))
    return cipher_text


def encrypt(K, P):
    # Convert the plain text into an integer array
    array = list()
    for p in P:
        array.append(ord(p) - 65)  # Subtract by 65 because A = 65
    array = np.array(array)

    # Resize message array for the matrix key
    n = K.shape[1]
    array = array.reshape(int(len(P) / n), n).T
    print(array)

    # Encrypt message
    C = np.dot(K, array)
    for i in range(C.shape[0]):
        for j in range(C.shape[1]):
            C[i, j] = np.mod(C[i, j], modulus)

    print(f"\r\nCiphertext: {matrix_to_text(C.T)}")
    print(C)

    return C


def decrypt(K, P):
    # Calculates the modular multiplicative inverse of the determinant of K
    det = determinant(K)
    mod_mul_inv = mod_inverse(det)

    a = K[0, 0]
    b = K[0, 1]
    c = K[1, 0]
    d = K[1, 1]
    K[0, 0] = mod_mul_inv * (d % modulus) % modulus
    K[1, 0] = mod_mul_inv * (-c % modulus) % modulus
    K[0, 1] = mod_mul_inv * (-b % modulus) % modulus
    K[1, 1] = mod_mul_inv * (a % modulus) % modulus

    # Decrypt message
    P = np.dot(K, P)
    for i in range(P.shape[0]):
        for j in range(P.shape[1]):
            P[i, j] = np.mod(P[i, j], modulus)

    print(f"\r\nPlaintext: {matrix_to_text(P.T)}")
    print(P)

    return P


if __name__ == '__main__':
    inputs = []
    inputs.append(("ATTACKATDAWN", np.array([[19, 8, 4], [3, 12, 7]])))
    inputs.append(("ATTACKATDAWN", np.array([[7, 8], [11, 11]])))
    inputs.append(("ATTACKATDAWN", np.array([[5, 15], [4, 12]])))
    inputs.append(("HELP", np.array([[3, 3], [2, 5]])))
    counter = 1

    for input in inputs:
        P = input[0]
        K = input[1]

        print(f"\nINPUT {counter}")
        counter += 1
        if not is_square(K):
            # raise MatrixNotInvertible('The matrix is not square')
            print('The matrix is not square')
            continue

        if not invertible(K):
            # raise MatrixNotInvertible('The determinant = 0.')
            print('The determinant = 0.')
            continue

        print('The matrix is invertible')
        print(f"Plaintext: {P}")

        C = encrypt(K, P)
        decrypted_message = decrypt(K, C)
