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

  def test13(self):
    aba="ada"
    hypernet = "adadc"
    self.assertTrue(hasBAB(hypernet, aba))

  def test14(self):
    ip = "bcbwbvyvqpozfig[twwsbwyhvfaddwo]jogvkczzowocmkwwlla[yedsazzkeklftvohfqz]tghtcjemmehumuyxar"
    self.assertTrue(supportsSSL(ip))

  def test15(self):
    ip = "gfgrgtizxajkaicjcc[mftrzuftzrgrwilsv]uckwgxywnamzjglbnts"
    self.assertFalse(supportsSSL(ip))

  def test16(self):
    ip = "hzqfveaxrqycvuolynx[ztsmaipixbuhbmv]ebvofyoeponbpip"
    self.assertFalse(supportsSSL(ip))

  def test17(self):
    ip = "vwwekuavrftztxb[aywyoempmajrdkxpsc]eibnjbszsfsapujqn[rxpcsihuzszefcdzl]gsahdvozzgxjhontxk"
    self.assertFalse(supportsSSL(ip))

  def test18(self):
    ip = "efuoofbuyjoaqjd[achnmlslfvovmgt]xcuyvikslsewgqlx[gjxolnhgqhhglojjqhy]iarxidejlgphqwaei"
    self.assertFalse(supportsSSL(ip))

  def test19(self):
    ip = "uxpcurtzqgpgtzkvp[mibqtgwackcedfri]otnnsgolldyzdpbew[tmgiijgjuvjykwahml]xxgjgzmnicxmywdubrb[hwhcgbzhuoankdubft]rxqzywfyuliatahn"
    self.assertFalse(supportsSSL(ip))

  def test20(self):
    ip = "abbhujqyoaphnruaih[yidrkxgrxeoarph]fvryghhzqrobkbsck[dnokdwmkbktlfoihxl]ttptfiadsswiwsfbvf"
    self.assertFalse(supportsSSL(ip))

  def test21(self):
    ip = "djwqivpbexyvdquh[qmmdydhjbmunyjixviv]nradabzesdavhasjbjs[lsabjblhocebvyhfee]hwbyvnzltgezasg"
    self.assertFalse(supportsSSL(ip))

  def test22(self):
    ip = "dxnkgspqhyejogxstsk[jfgckouqypxttst]axtisjbtaviwafh"
    self.assertFalse(supportsSSL(ip))

class DSMExamples(unittest.TestCase):
  foobar = [('slkisqowpneowabctk[ryhlzrkziabbnbnele]hvionqkbewzdbly\n', False),
      ('djekfwpsoiihcfd[hncjbxkkecscjvuzqo]akeczaajzyrqllj[bzfnzoikwvbxeryrwxb]dagmghjivjknvvgmm\n', False),
      ('pgstdunvpkygdhxf[nkcpvzkilrxjoie]mzahevvdtrwxytc[arwlmsgbyreyxpmprqx]hojyzxqqjylfjusttkq\n', False),
      ('yrmxbhvwfhllkihaep[nahzalqadgjfoflr]whnvkzquqklzkymykd[jgujzpbnzrbzafeh]kbqccktgyczgsfgcrie[rgdkferemxzfjhrj]cqncbhflmhtonlarf\n', False),
      ('pridigkxnsmwjnubj[tqyowmooyyzxxcoxp]bdatmjremximbvgkla[bymfroqflneczdyrj]qqfzxjwrpzxoiba[bdwgvaubttwwhkgzlvl]ybqpwobmbkwclvlit\n', False),
      ('hlqxlmjtkmjwjrxzvb[nwhgxypfvrlwznxmx]wjwddpfcprmkgmabb[plpqkkvhdboebwjcxi]pdonethdwrptyyfo\n', False),
      ('xlegdhcmxpzdzjlay[liydzajrkaufrswav]uemkomlqqoatvvntqj[kjktwnakakpceoy]yygdrowvnacguirorml\n', False),
      ('ftipvtztetqweblic[urqdmhfkxxfnrrcsib]awbpwyprdvmvwgzzepe[vkutvypzjyryaayih]nmrfmuniuzzkhluqgx\n', False),
      ('gilmfvvjrximlddz[vxvpnelnnkyzhnsljzi]mlhgdduohhvtyraxlu\n', False),
      ('xiiwosblocyedaexck[uibalcgupzlxmfj]pmcrxohfqmosqxbnnt\n', False),
      ('dtzqgkdzdxwltggn[vshtllabynzdzifr]gjzwjvbezsudnllkjb\n', True),
      ('olisquqoqosqhvpxrn[noqojsemxsklzfjd]xmirfofadjmjrur[syaizhzpmmwrqvnkwlk]dmcempjwxzbucpylcb\n', True),
      ('njdolrhgbbnxckxk[ydkpwcoijeozgessd]kcuekavfxreeouyc[eqceqfiwzxkrghgisl]amvuicsywffrdvjhhco[vosewgsiwozagpux]gocrhghscjbkypdg\n', True),
      ('asozoseeexjlnujfox[izozytydhsdtwnv]allqlztvpwabunjh\n', True),
      ('udfruyrgqsusxqc[ocqpcqumszwgunhju]qvposnnngjcjolnh[dlrivxihlkusulblxzb]yziglhmzfxyyluo\n', True),
      ('evaliqomffjqjmobfz[tcceyhouujtlcgvgujy]fdwjohlrxmtximkvgv\n', True),
      ('adgejfziulqubtv[kkhvflrrzzlpdqlqjqh]nqzlyincexbxbwakws[vzgkmpczegsfcewpft]nlreyilbmrcyrykqkwj[mehvkuhgphblsycjoi]lgzqxetzdqodirlqlkf\n', True),
      ('vueefgllnygexoagq[vlnoffjbojjloomfgf]zwgejsiuosklvzdva[frxlizqlpfzbzbe]phtllgfghshchbwjy[jhsqiybxyziobqnrgc]hqptbpfplshpshfkp\n', True),
      ('bevdijrwuekuzxeftyh[magmjngccsxxyre]ocionfzaxjarewqjeyw[gdnhfenokdklsbckv]jbiqkhvyhvddkdg\n', True),
      ('juamwbaymppduonwy[veisidgxqzjsndd]ouyigdcdjmeotgt[fnffnevbhtftewfu]ulkngkhascpefee[ypwcdcthzatxafpir]xybcxlqnmauyrezyfi\n', True),
      ('bcbdc[adadc]adaed', True),
      ('aba[abab]ad', True)]

  def testDSM(self):
    for ip, result in DSMExamples.foobar:
      with self.subTest(ip=ip):
        self.assertEqual(result, supportsSSL(ip))

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
  hypernet_pattern = re.compile(r'(.)(.)\1')
  m = hypernet_pattern.search(hypernet)
  while m:
    if m.group(1) == aba[1] and m.group(2) == aba[0]:
      return True
    m = hypernet_pattern.search(hypernet, m.start() + 1)
  return False


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
