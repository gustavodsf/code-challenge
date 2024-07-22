
class TestCreditCard(unittest.TestCase):

    def test_mastercard(self):
      self.assertEqual(is_valid_credit_card("5555555555554444"), "mastercard")
      self.assertEqual(is_valid_credit_card("5105105105105100"), "mastercard")

    def test_visa(self):
      self.assertEqual(is_valid_credit_card("4111111111111111"), "visa") 
      self.assertEqual(is_valid_credit_card("4012888888881881"), "visa")  

    def test_discover(self):
      self.assertEqual(is_valid_credit_card("6011111111111117"), "discover") 
      self.assertEqual(is_valid_credit_card("6011000990139424"), "discover")  

    def test_amex(self):
      self.assertEqual(is_valid_credit_card("378282246310005"), "amex") 
      self.assertEqual(is_valid_credit_card("371449635398431"), "amex")  

    def test_invalid(self):
      self.assertEqual(is_valid_credit_card("5600000000000000"), "invalid")
if __name__ == '__main__':
    unittest.main()


def is_valid_credit_card(credit_card_number: str ) -> str:
  if credit_card_number[0:2] in ["34","37"]  and len(credit_card_number) == 15:
    return "amex"
  if credit_card_number[0:4] == "6011" and len(credit_card_number) == 16:
    return "discover"
  if credit_card_number[0:2] in ["51","52","53","54", "55"]  and len(credit_card_number) == 16:
    return "mastercard"
  if credit_card_number[0] == '4' and (len(credit_card_number) in [13, 16] ):
    return "visa"
  return "invalid"

def luhn_algorightm(credit_card_number: str) -> bool:
  counter = 0;
  for idx in range(len(credit_card_number), 0 , -1):
    if(idx % 2 == 0):
      counter += int(credit_card_number[idx-1])
    else: 
      aux = str(int(credit_card_number[idx-1]) * 2)
      if(len(aux) == 1):
        counter += int(aux)
      else:
        counter += int(aux[0])
        counter += int(aux[1])

  return (counter % 10 == 0 ); 

#print(luhn_algorightm("56000000000000000"))
#print(luhn_algorightm("4417123456789112"))

print(luhn_algorightm("4222222222222"))