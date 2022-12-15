import Crypto
import Crypto.PublicKey import RSA

random_generator = Crypto.Random.new().read
private_key = RSA.generate(random_generator)

print(random_generator)
print(private_key)

