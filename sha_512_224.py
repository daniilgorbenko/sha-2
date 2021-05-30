# константа для суммы по mod 2**32
VAL_MOD = 2 ** 64

def set_zero_in_end(bits, len_str):
    """ метод для вставки нулей в конец битовой последовательности"""
    while len(bits) % len_str != 0:
        bits += '0'
    return bits


def set_zero_in_start(bits, len_str):
    """ метод для вставки нулей в начало битовой последовательности"""
    while len(bits) % len_str != 0:
        bits = '0' + bits
    return bits


def set_len_str_in_end(bits, bits_len, max_mod=1024):
    """ метод для вставки в конец битовой последовательности текста длины сообщения"""
    while (len(bits) + len(bits_len)) % max_mod != 0:
        bits += '0'
    bits += bits_len
    return bits


def hex_to_bin(hex_num, len_bits=64):
    """ метод для перевода числа из 16-ричного представления в бинарное"""
    bits = bin(hex_num)[2:]
    # добавляем в начало нули для получения нужной длины последовательности
    while len(bits) < len_bits:
        bits = '0' + bits
    return bits


def str_to_bin(text):
    """ метод для перевода строки в бинарное представление """
    binary = ''
    # приводим текст к виде списка байт
    byte_array = bytearray(text, "utf8")
    # каждый байт преобразуем в битовую строчку
    for byte in byte_array:
        binary_repr = bin(byte)[2:]
        while len(binary_repr) < 8:
            binary_repr = '0' + binary_repr
        binary += binary_repr
    return binary


def rotate_right(list_bits, count):
    """ метод для циклического сдвига вправо бинарной последовательности"""
    for _ in range(count):
        list_bits = list_bits[-1] + list_bits[:-1]
    return list_bits


def shift_right(list_bits, count):
    """ метод для логического сдивга вправо бинарной последовательности"""
    for _ in range(count):
        list_bits = '0' + list_bits[:-1]
    return list_bits


def xor(list_bits1, list_bits2):
    """ метод для вычисления исключающего или"""
    # дополняем последовательности до одинаковой длины
    max_len = max(len(list_bits1), len(list_bits2))
    list_bits1 = '0' * (max_len - len(list_bits1)) + list_bits1
    list_bits2 = '0' * (max_len - len(list_bits2)) + list_bits2
    rez_bits = []
    # xor: 1 если хотя бы один бит 1, но не оба вместе, иначе 0
    for i in range(max_len):
        new_bit = '1' if list_bits1[i] != list_bits2[i] else '0'
        rez_bits.append(new_bit)
    return ''.join(rez_bits)


def log_and(bits1, bits2):
    """ метод для вычисления логического И """
    max_len = max(len(bits1), len(bits2))
    bits1 = '0' * (max_len - len(bits1)) + bits1
    bits2 = '0' * (max_len - len(bits2)) + bits2
    rez_bits = []
    # and: 1, если оба бита = 1, иначе 0
    for i in range(max_len):
        new_bit = '1' if bits1[i] == bits2[i] == '1' else '0'
        rez_bits.append(new_bit)
    return ''.join(rez_bits)


def summator(*list_bits):
    """ метод для суммирования битовых последовательностей"""
    summa = 0
    # для получения суммы всё переводится к обычным 10-чным числам
    for bit in list_bits:
        summa += int(bit, base=2)
    # в sha-256 сумма берется по mod 2**32
    summa = summa % VAL_MOD
    # приводим обратно к битовой последовательности
    binary = bin(summa)[2:]
    while len(binary) < 64:
        binary = '0' + binary
    return binary


def log_not(bits):
    """ метод для получения отрицания от битовой последовательности"""
    binary = ''
    for bit in bits:
        binary += '1' if bit == '0' else '0'
    return binary

# заполняем список первоначальных констант
h0 = hex_to_bin(0x8C3D37C819544DA2)
h1 = hex_to_bin(0x73E1996689DCD4D6)
h2 = hex_to_bin(0x1DFAB7AE32FF9C82)
h3 = hex_to_bin(0x679DD514582F9FCF)
h4 = hex_to_bin(0x0F6D2B697BD44DA8)
h5 = hex_to_bin(0x77E36F7304C48942)
h6 = hex_to_bin(0x3F9D85A86A1D36C8)
h7 = hex_to_bin(0x1112E6AD91D692A1)
# таблица констант
# первые 64 бита дробных частей кубических корней первых 80 простых чисел
constants = [
    hex_to_bin(0x428a2f98d728ae22), hex_to_bin(0x7137449123ef65cd), hex_to_bin(0xb5c0fbcfec4d3b2f), hex_to_bin(0xe9b5dba58189dbbc),
    hex_to_bin(0x3956c25bf348b538), hex_to_bin(0x59f111f1b605d019), hex_to_bin(0x923f82a4af194f9b), hex_to_bin(0xab1c5ed5da6d8118),

    hex_to_bin(0xd807aa98a3030242), hex_to_bin(0x12835b0145706fbe), hex_to_bin(0x243185be4ee4b28c), hex_to_bin(0x550c7dc3d5ffb4e2),
    hex_to_bin(0x72be5d74f27b896f), hex_to_bin(0x80deb1fe3b1696b1), hex_to_bin(0x9bdc06a725c71235), hex_to_bin(0xc19bf174cf692694),

    hex_to_bin(0xe49b69c19ef14ad2), hex_to_bin(0xefbe4786384f25e3), hex_to_bin(0x0fc19dc68b8cd5b5), hex_to_bin(0x240ca1cc77ac9c65),
    hex_to_bin(0x2de92c6f592b0275), hex_to_bin(0x4a7484aa6ea6e483), hex_to_bin(0x5cb0a9dcbd41fbd4), hex_to_bin(0x76f988da831153b5),

    hex_to_bin(0x983e5152ee66dfab), hex_to_bin(0xa831c66d2db43210), hex_to_bin(0xb00327c898fb213f), hex_to_bin(0xbf597fc7beef0ee4),
    hex_to_bin(0xc6e00bf33da88fc2), hex_to_bin(0xd5a79147930aa725), hex_to_bin(0x06ca6351e003826f), hex_to_bin(0x142929670a0e6e70),

    hex_to_bin(0x27b70a8546d22ffc), hex_to_bin(0x2e1b21385c26c926), hex_to_bin(0x4d2c6dfc5ac42aed), hex_to_bin(0x53380d139d95b3df),
    hex_to_bin(0x650a73548baf63de), hex_to_bin(0x766a0abb3c77b2a8), hex_to_bin(0x81c2c92e47edaee6), hex_to_bin(0x92722c851482353b),

    hex_to_bin(0xa2bfe8a14cf10364), hex_to_bin(0xa81a664bbc423001), hex_to_bin(0xc24b8b70d0f89791), hex_to_bin(0xc76c51a30654be30),
    hex_to_bin(0xd192e819d6ef5218), hex_to_bin(0xd69906245565a910), hex_to_bin(0xf40e35855771202a), hex_to_bin(0x106aa07032bbd1b8),

    hex_to_bin(0x19a4c116b8d2d0c8), hex_to_bin(0x1e376c085141ab53), hex_to_bin(0x2748774cdf8eeb99), hex_to_bin(0x34b0bcb5e19b48a8),
    hex_to_bin(0x391c0cb3c5c95a63), hex_to_bin(0x4ed8aa4ae3418acb), hex_to_bin(0x5b9cca4f7763e373), hex_to_bin(0x682e6ff3d6b2b8a3),

    hex_to_bin(0x748f82ee5defb2fc), hex_to_bin(0x78a5636f43172f60), hex_to_bin(0x84c87814a1f0ab72), hex_to_bin(0x8cc702081a6439ec),
    hex_to_bin(0x90befffa23631e28), hex_to_bin(0xa4506cebde82bde9), hex_to_bin(0xbef9a3f7b2c67915), hex_to_bin(0xc67178f2e372532b),
    # новые значения
    hex_to_bin(0xca273eceea26619c), hex_to_bin(0xd186b8c721c0c207), hex_to_bin(0xeada7dd6cde0eb1e), hex_to_bin(0xf57d4f7fee6ed178),
    hex_to_bin(0x06f067aa72176fba), hex_to_bin(0x0a637dc5a2c898a6), hex_to_bin(0x113f9804bef90dae), hex_to_bin(0x1b710b35131c471b),

    hex_to_bin(0x28db77f523047d84), hex_to_bin(0x32caab7b40c72493), hex_to_bin(0x3c9ebe0a15c9bebc), hex_to_bin(0x431d67c49c100d4c),
    hex_to_bin(0x4cc5d4becb3e42b6), hex_to_bin(0x597f299cfc657e2a), hex_to_bin(0x5fcb6fab3ad6faec), hex_to_bin(0x6c44198c4a475817),
]

# НАЧАЛО АЛГОРИТМА
# сообщение для хэширования
msg = "Euler is held to be one of the greatest mathematicians in history."
# переводим сообщение в битовую последовательность
m = str_to_bin(msg)
# добавляем в конец '1'
m = m + "1"

# добавляем в коней исходную длину сообщения в виде 128 битной последователньости
bits_len = set_zero_in_start(bin(len(msg) * 8)[2:], 128)
# добавляем в конец длину строки
m = set_len_str_in_end(m, bits_len)
print(len(m))
print(m)
# исходной сообщение обрабатывается частями по 1024 бита
for i in range(0, len(m), 1024):
    part = m[i:i + 1024]
    parts = []
    # разибваем исходное сообщение на 16 кусочкой длиной 64 бита
    for j in range(0, 1024, 64):
        parts.append(part[j:j + 64])

    # генерируем дополнительные 64 слова для хэширования
    for k in range(16, 80):
        # sigma0 = right_rotate(parts[k-15], 1) xor right_rotate(parts[k-15], 8) xor shift_right(parts[k-15], 7)
        rr1 = rotate_right(parts[k - 15], 1)
        rr2 = rotate_right(parts[k - 15], 8)
        sr = shift_right(parts[k - 15], 7)
        x1 = xor(rr1, rr2)
        s0 = xor(x1, sr)
        # sigma1 = right_rotate(parts[k-2], 19) xor right_rotate(parts[k-2], 61) xor shift_right(parts[k-2], 6)
        rr1 = rotate_right(parts[k - 2], 19)
        rr2 = rotate_right(parts[k - 2], 61)
        sh = shift_right(parts[k - 2], 6)
        x1 = xor(rr1, rr2)
        s1 = xor(x1, sh)
        # новое слово: parts[k - 16] + sigma0 + parts[k - 7] + sigma1
        new_part = summator(parts[k - 16], s0, parts[k - 7], s1)
        parts.append(new_part)
    # инициализируем дополнительные переменные
    a = h0
    b = h1
    c = h2
    d = h3
    e = h4
    f = h5
    g = h6
    h = h7

    # весь алгоритм хэширования выполняется 80 раза
    for k in range(80):
        # sigma1 = rotate_right(e, 14) xor rotate_right(e, 18) xor rotate_right(e, 41)
        rr1 = rotate_right(e, 14)
        rr2 = rotate_right(e, 18)
        rr3 = rotate_right(e, 41)
        x1 = xor(rr1, rr2)
        s1 = xor(x1, rr3)
        # ch = log_and(e, f) xor log_and(log_not(e), g)
        rr1 = log_and(e, f)
        rr3 = log_and(log_not(e), g)
        ch = xor(rr1, rr3)
        # temp1 = h + s1 + ch + constants[k] + parts[k]
        t1 = summator(h, s1, ch, constants[k], parts[k])
        # sigma0 = rotate_right(a, 28) xor rotate_right(a, 34) xor rotate_right(a, 39)
        rr1 = rotate_right(a, 28)
        rr2 = rotate_right(a, 34)
        rr3 = rotate_right(a, 39)
        x1 = xor(rr1, rr2)
        s0 = xor(x1, rr3)
        # maj = log_and(a, b) xor log_and(a, c) xor log_and(b, c)
        rr1 = log_and(a, b)
        rr2 = log_and(a, c)
        rr3 = log_and(b, c)
        x1 = xor(rr1, rr2)
        maj = xor(x1, rr3)
        # temp2 = sigma0 + maj
        t2 = summator(s0, maj)
        # теперь необходимо изменить значения временных переменных
        h = g
        g = f
        f = e
        e = summator(d, t1)
        d = c
        c = b
        b = a
        a = summator(t1, t2)
    # в конце необходимо изменить начальные переменные для хранения хеша
    h0 = summator(h0, a)
    h1 = summator(h1, b)
    h2 = summator(h2, c)
    h3 = summator(h3, d)
    h4 = summator(h4, e)
    h5 = summator(h5, f)
    h6 = summator(h6, g)
    h7 = summator(h7, h)

print(hex(int(h0, base=2)))
print(hex(int(h1, base=2)))
print(hex(int(h2, base=2)))
print(hex(int(h3, base=2)))
print(hex(int(h4, base=2)))
print(hex(int(h5, base=2)))
print(hex(int(h6, base=2)))
print(hex(int(h7, base=2)))

sha512_224_bin = h0+h1+h2+h3+h4+h5+h6+h7
sha512_224_bin = sha512_224_bin[:224]
sha512_224_text = (hex(int(sha512_224_bin, base=2))[2:])
print(sha512_224_text)
print(len(sha512_224_text))


