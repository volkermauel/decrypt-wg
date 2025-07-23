import importlib.machinery

loader = importlib.machinery.SourceFileLoader('decrypt_wg', 'decrypt-wg.py')
mod = loader.load_module()

kek = bytes.fromhex('000102030405060708090A0B0C0D0E0F')
plain = bytes.fromhex('00112233445566778899AABBCCDDEEFF')
wrapped = bytes.fromhex('1FA68B0A8112B447AEF34BD8FB5A7B829D3E862371D2CFE5')

def test_wrap():
    assert mod.aes_wrap_key(kek, plain) == wrapped

def test_unwrap():
    assert mod.aes_unwrap_key(kek, wrapped, iv=0xa6a6a6a6a6a6a6a6) == plain
