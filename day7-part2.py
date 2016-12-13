import unittest
import re
import sys

class Day7Part2(unittest.TestCase):
  def test1(self):
    ip = "aba[bab]xyz"
    self.assertTrue(supportsSSL(ip))

  def test2(self):
    ip = "xyx[xyx]xyx"
    self.assertFalse(supportsSSL(ip))

  def test3(self):
    ip = "aaa[kek]eke"
    self.assertTrue(supportsSSL(ip))

  def test4(self):
    ip = "zazbz[bzb]cdb"
    self.assertTrue(supportsSSL(ip))

  def test5(self):
    supernet = "aba"
    self.assertTrue(getABA(supernet))

  def test6(self):
    supernet = "xyx"
    self.assertTrue(getABA(supernet))

  def test7(self):
    supernet = "aaa"
    self.assertFalse(getABA(supernet))

  def test8(self):
    supernet = "zazbz"
    self.assertTrue(getABA(supernet))

  def test9(self):
    aba = "aba"
    hypernet = "bab"
    self.assertTrue(hasBAB(hypernet, aba))

  def test10(self):
    aba = "xyx"
    hypernet = "xyx"
    self.assertFalse(hasBAB(hypernet, aba))

  def test11(self):
    aba = "eke"
    hypernet = "kek"
    self.assertTrue(hasBAB(hypernet, aba))

  def test12(self):
    aba = "zbz"
    hypernet = "bzb"
    self.assertTrue(hasBAB(hypernet, aba))

class DSMExamples(unittest.TestCase):
  def __init__(self, ip, supportsSSL):
    super(DSMExamples, self).__init__("testDSM")
    self.ip = ip
    self. supportsSSL = supportsSSL

  def testDSM(self):
    self.assertEqual(self.supportsSSL, supportsSSL(self.ip))

def load_tests(loader, tests, pattern):
  foobar = [('luqpeubugunvgzdqk[jfnihalscclrffkxqz]wvzpvmpfiehevybbgpg[esjuempbtmfmwwmqa]rhflhjrqjbbsadjnyc\n', False),
            ('eyunqqdlsaasqfbhwpc[fpmanqdfvhrosxaptp]aeyfdxouzzuuuxteclt[ganxlwtfygldvdhoquf]paymaxgcegdvovaqxya[ylnriprhjdnkuntzp]oqfodnpayolcntvpo\n', True),
            ('xdsqxnovprgovwzkus[fmadbfsbqwzzrzrgdg]aeqornszgvbizdm\n', False),
            ('uxpvoytxfazjjhi[qogwhtzmwxvjwxreuz]zduoybbzxigwggwu[lamifchqqwbphhsqnf]qrjdjwtnhsjqftnqsk[bsqinwypsnnvougrs]wfmhtjkysqffllakru\n', True),
            ('pbpsdnornxrjozbhegt[olfscmqufczzthv]sjrnzixklvlzapmv[boflyiiyupvpoyyo]gagojlnkgjkidipsfc\n', False),
            ('piurduvwvigtuwnjnpj[mirushebmxoukqttq]nksxdnhcjfaymiuua[dkihhehyhjvenynticl]nmrfbzilhhvjfobbof[jqahcpebhcbqyvostx]mnyaeppulzktgjgki\n', False)]
  test_suite = unittest.TestSuite()
  test_suite.addTest(Day7Part2())
  for ip, result in foobar:
    test_suite.addTest(DSMExamples(ip, result))
  return test_suite

def getABA(supernet):
  print("  getABA()")
  print("    supernet:", supernet)
  supernet_pattern = r'(.)(.)\1'
  m = re.search(supernet_pattern, supernet)
  if m and m.group(1) != m.group(2):
    return m.group(0)
  return None

def getAllABA(supernet):
  sub = supernet
  aba = getABA(sub)
  while aba:
    yield aba
    sub = sub[sub.find(aba) + 1:]
    aba = getABA(sub)

def hasBAB(hypernet, aba):
  hypernet_pattern = r'(.)(.)\1'
  m = re.search(hypernet_pattern, hypernet)
  return m and m.group(1) == aba[1] and m.group(2) == aba[0]


def supportsSSL(ip):
  print("\nsupportsSSL()")
  print("  ip:", ip)
  supernetRegex = re.compile(r'[^[]*')
  hypernetRegex = re.compile(r'\[([^]]*)\]')
  aba_list = []
  hypernet_list = []

  m = supernetRegex.match(ip)
  while m:
    aba_list.extend(getAllABA(m.group(0)))
    m = hypernetRegex.match(ip, m.end())
    if m:
      hypernet_list.append(m.group(1))
      m = supernetRegex.match(ip, m.end())

  print("  aba_list:", aba_list)
  print("  hypernet_list:", hypernet_list)
  has_bab_list = [hasBAB(hypernet, aba) for hypernet in hypernet_list for aba in aba_list]
  print("  has_bab_list:", has_bab_list)
  return any(has_bab_list)

def main():
  print("\n******** main() ********")
  print(sum(supportsSSL(ip.strip()) for ip in sys.stdin))

if __name__ == "__main__":
  if unittest.main(exit=False).result.wasSuccessful():
    main()
